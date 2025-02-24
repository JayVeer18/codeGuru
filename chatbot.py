import os

from langchain.chains import ConversationalRetrievalChain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains.retrieval import create_retrieval_chain
from langchain.prompts import ChatPromptTemplate
from langchain_community.document_loaders import PyPDFLoader, UnstructuredMarkdownLoader
from langchain_community.vectorstores.faiss import FAISS
from langchain_core.messages import HumanMessage
from langchain_core.prompts import MessagesPlaceholder
from langchain_huggingface import HuggingFaceEmbeddings, HuggingFaceEndpoint
from langchain_openai import OpenAIEmbeddings, ChatOpenAI


# find models here https://ollama.com/library?sort=popular
class Chatbot:
    def __init__(self, file_path, api_key=None, framework="huggingface", model_name="microsoft/Phi-3-mini-4k-instruct",
                 chain_type="RAG"):
        """
        Initializes the Chatbot class.

        Args:
            framework (str): must be either openai or ollama
            model_name (str): Name of the language model to use.
            api_key (str): API key for the OpenAI service.
            file_path (str): Path to the PDF file for context.
            chain_type (str): Type of chat chain ('RAG' or 'conversation').
        """
        self.file_path = file_path
        self.chain_type = chain_type
        self.framework = framework
        self.file_name = os.path.splitext(os.path.basename(file_path))[0]
        self.chat_history = []

        # Initialize core components
        if self.framework == 'openai':
            self.embeddings = OpenAIEmbeddings(api_key=api_key)
            self.llm = ChatOpenAI(model_name=model_name, api_key=api_key)
        else:
            self.embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
            self.llm = HuggingFaceEndpoint(repo_id=model_name,
                                           max_new_tokens=512,
                                           top_k=10,
                                           temperature=0.01,
                                           huggingfacehub_api_token=api_key
                                           )
        self.chain = self._initialize_chain()

    def _initialize_chain(self):
        """Initialize the appropriate chain based on the selected chain type."""
        retriever = self._load_vector_store_as_retriever()
        if self.chain_type == 'RAG':
            return self._create_RAG_chain(retriever)
        return ConversationalRetrievalChain.from_llm(
            llm=self.llm, retriever=retriever, return_source_documents=True
        )

    def _file_load_and_split(self):
        """Load and split PDF document into chunks."""
        file_extension = os.path.splitext(self.file_path)[1]
        if file_extension == '.md':
            loader = UnstructuredMarkdownLoader(self.file_path)
        elif file_extension == '.pdf':
            loader = PyPDFLoader(self.file_path)
        else:
            raise ValueError("Unsupported file format. Only PDF and Markdown are supported.")
        return loader.load_and_split()

    def _load_vector_store_as_retriever(self):
        """Load or create a vector store, and return it as a retriever."""
        index_path = f"./faiss_db/{self.file_name}.faiss"
        if os.path.exists(index_path):
            vector_store = FAISS.load_local(folder_path="./faiss_db", index_name=self.file_name,
                                            embeddings=self.embeddings, allow_dangerous_deserialization=True)
        else:
            doc_chunks = self._file_load_and_split()
            vector_store = FAISS.from_documents(documents=doc_chunks, embedding=self.embeddings)
            vector_store.save_local(folder_path="./faiss_db", index_name=self.file_name)
        return vector_store.as_retriever()

    # Convert loaded documents into strings by concatenating their content and ignoring metadata
    def _format_docs(self, docs):
        return "\n\n".join(doc.page_content for doc in docs)

    def _create_RAG_chain(self, retriever):
        """Create a RAG-based conversational chain."""
        prompt_template = """
            You are an intelligent assistant designed to help students with their programming assignments by providing hints and guidance.
             Your goal is to help them understand the concepts and solve the problems on their own without giving them the direct answers no matter what. 
             The instructions for the assignment are provided in a file. Here are the guidelines you should follow:
            
            1. Encourage Critical Thinking: Ask questions that guide the student to think about the problem and the steps needed to solve it.
            2. Provide Conceptual Hints: Offer hints that explain the underlying concepts without revealing the exact solution.
            3. Break Down Problems: Help the student break down complex problems into smaller, manageable parts.
            4. Use Examples: Provide examples that illustrate similar concepts or problems without directly solving the assignment question.
            5. Encourage Research: Suggest resources or topics the student can research to find the solution on their own.
            6. Avoid Direct Answers: Do not provide the exact code or solution to the assignment questions.
            7. Sample Code Snippets: If asked about certain code examples, you can provide basic syntax of how they look so that user can use it as a reference.
            
            Here is the content of the shared file with the assignment instructions:
            {context}
            
             Previous Conversations:
            {chat_history}
            
            Based on these guidelines and the information in the file, please provide hints and guidance for the following question from the assignment:
            {question}
            """
        qa_system_prompt = """
            You are an intelligent assistant designed to help students with their programming assignments by providing hints and guidance.
             Your goal is to help them understand the concepts and solve the problems on their own without giving them the direct answers no matter what. 
             The instructions for the assignment are provided in a file. Here are the guidelines you should follow:
            
            1. Encourage Critical Thinking: Ask questions that guide the student to think about the problem and the steps needed to solve it.
            2. Provide Conceptual Hints: Offer hints that explain the underlying concepts without revealing the exact solution.
            3. Break Down Problems: Help the student break down complex problems into smaller, manageable parts.
            4. Use Examples: Provide examples that illustrate similar concepts or problems without directly solving the assignment question.
            5. Encourage Research: Suggest resources or topics the student can research to find the solution on their own.
            6. Avoid Direct Answers: Do not provide the exact code or solution to the assignment questions.
            7. Sample Code Snippets: If asked about certain code examples, you can provide basic syntax of how they look so that user can use it as a reference 
                                        but no matter what you should not give the exact code to solve the problem.
            
            Here is the content of the shared file with the assignment instructions, **you should provide hints and guidance** only based on it:
            {context} """

        # prompt = ChatPromptTemplate.from_template(prompt_template)

        # Chain includes retriever -> formatting -> LLM
        # chain = (
        #         {"context": retriever | self._format_docs, "question": RunnablePassthrough(), "chat_history": self.chat_history}
        #         | prompt
        #         | self.llm
        #         | StrOutputParser()
        # )

        qa_prompt = ChatPromptTemplate.from_messages(
            [
                ("system", qa_system_prompt),
                MessagesPlaceholder("chat_history"),
                ("human", "{input}"),
            ]
        )
        question_answer_chain = create_stuff_documents_chain(self.llm, qa_prompt)
        rag_chain = create_retrieval_chain(retriever=retriever, combine_docs_chain=question_answer_chain)

        return rag_chain

    # def _create_RAG_chain(self, retriever):
    #     """Create a RAG-based conversational chain."""
    #     prompt_template = """
    #         You are an intelligent assistant designed to help students with their programming assignments by providing hints and guidance.
    #          Your goal is to help them understand the concepts and solve the problems on their own without giving them the direct answers no matter what.
    #          The instructions for the assignment are provided in a file. Here are the guidelines you should follow:
    #
    #         1. Encourage Critical Thinking: Ask questions that guide the student to think about the problem and the steps needed to solve it.
    #         2. Provide Conceptual Hints: Offer hints that explain the underlying concepts without revealing the exact solution.
    #         3. Break Down Problems: Help the student break down complex problems into smaller, manageable parts.
    #         4. Use Examples: Provide examples that illustrate similar concepts or problems without directly solving the assignment question.
    #         5. Encourage Research: Suggest resources or topics the student can research to find the solution on their own.
    #         6. Avoid Direct Answers: Do not provide the exact code or solution to the assignment questions.
    #
    #         Here is the content of the shared file with the assignment instructions:
    #         {context}
    #
    #         Based on these guidelines and the information in the file, please provide hints and guidance for the following question from the assignment:
    #         {question}
    #         """
    #
    #     prompt = ChatPromptTemplate.from_template(prompt_template)
    #
    #
    #     chain = (
    #             {"context": retriever | self._format_docs, "question": RunnablePassthrough()}
    #             | prompt
    #             | self.llm
    #             | StrOutputParser()
    #     )
    #
    #
    #
    #     return chain

    def invoke(self, query):
        """Invoke the chain based on the selected chain type."""
        return self._invoke_with_history(query)

    def _invoke_without_history(self, query):
        """Invoke the chain without chat history for RAG-based responses. Need to create the chain accordingly without history"""
        print('query:', query)
        # Pass the correct values into the chain
        response = self.chain.invoke(query)
        print(response)
        self.chat_history.append((query, response))
        return response

    def _invoke_with_history(self, query):
        """Invoke the chain with chat history for conversational responses."""
        response = self.chain.invoke({"input": query, "chat_history": self.chat_history})
        self.chat_history.extend([HumanMessage(content=query), response["answer"]])
        print(self.chat_history)
        return response["answer"]
