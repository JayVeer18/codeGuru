import contextlib

import streamlit as st
from streamlit_ace import st_ace
from chatbot import Chatbot
from dotenv import load_dotenv
import os, io, sys
import subprocess

# ollama run llama3.1:8b
# Get the directory of the current script (where this Python file is located)
script_dir = os.path.dirname(os.path.abspath(__file__))

# Specify the path of the README.md file
env_path = os.path.normpath(os.path.join(script_dir,".env"))

# load environment variables from .env file
load_dotenv(dotenv_path=env_path, verbose=True, override=True)

class App:
    def __init__(self, section_name, instr_file_path, pgm_file_path, session_key, page_title="Code Editor with Chatbot"):
        self.page_title = page_title
        self.section_name = section_name
        self.instr_file_path = instr_file_path
        self.pgm_file_path = pgm_file_path
        self.session_key = session_key

        # Initialize chatbot
        self.chatbot = Chatbot(file_path=self.instr_file_path, api_key=os.environ.get("OPENAI_API_KEY"), framework="openai",
                               model_name="gpt-4o-mini", chain_type='RAG')

        # self.chatbot = Chatbot(self.instr_file_path, api_key=os.environ.get("HUGGINGFACE_ACCESS_TOKEN"),
        #                        framework="huggingface", chain_type="RAG")

        # Initialize session state
        self.init_session_state()
    
    def read_file(self, file_path):
        if os.path.exists(file_path):
            try:
                with open(file_path, "r", encoding="utf-8") as file:
                    return file.read()
            except UnicodeDecodeError:
                st.error("Could not decode the file. Please check if the file is UTF-8 encoded.")
        else:
            st.error(f"The file not found at: {file_path}")

    def init_session_state(self):
        # Set up page configuration
        st.set_page_config(page_title=self.page_title, page_icon=":computer:", layout="wide")
        # Sidebar settings for editor
        st.sidebar.markdown('# Colorado State University')
        st.markdown("# Welcome to Drona, the codeGuru")
        st.markdown(self.section_name)

        if f"messages_{self.session_key}" not in st.session_state:
            st.session_state[f"messages_{self.session_key}"] = []
        # self.load()

    def chat_with_document(self):
        # Display chat history before the input box
        self.display_chat_history()

        # Query input
        if query := st.chat_input("I'm here to help you out with the coding assignment"):
            st.chat_message("user").markdown(query)
            
            # Add user message to chat history
            st.session_state[f"messages_{self.session_key}"].append({"role": "user", "content": query})

            with st.spinner("Querying... please wait..."), st.chat_message("assistant"):
                response = self.chatbot.invoke(query)
                st.markdown(response)

            # Add assistant response to chat history
            st.session_state[f"messages_{self.session_key}"].append({"role": "assistant", "content": response})
            
     

    def display_chat_history(self):
        for message in st.session_state[f"messages_{self.session_key}"]:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

    def execute_code(self, code):
        result = subprocess.run(['python', '-c', code], capture_output=True, text=True)
        return result

    def run(self):
        with st.sidebar:
            theme = st.selectbox(
                "Editor Theme",
                ["monokai", "github", "solarized_dark", "solarized_light", "dracula"]
            )
            font_size = st.slider("Font Size", 12, 24, 14)
            show_gutter = st.checkbox("Show Line Numbers", value=True)


        # Display instructions with images
        instructions = self.read_file(self.instr_file_path) 
        st.markdown(instructions, unsafe_allow_html=True)

        # Initialize code_output
        code_output = ""
        # Split layout for py_code editor and chatbot
        editor_col, chatbot_col = st.columns(2)
        container_height = 650
        # Left column: Code editor
        with editor_col:
            st.subheader("Code Editor")
            with st.container(height=container_height):
                # Display py_code editor with loaded file content
                pgm_code = self.read_file(self.pgm_file_path)
                py_code = st_ace(value=pgm_code, language='python', theme=theme, font_size=font_size, show_gutter=show_gutter, auto_update=False, key="editor")

            st.warning("**Please press the Apply button at  the end of the editor before running the code.**")
            if st.button('Run Code'):

                result = self.execute_code(py_code)
                if result.returncode == 0:
                    code_output = result.stdout
                    st.success("Code executed successfully!")
                else:
                    code_output = result.stderr
                    st.error("An error occurred while executing the code. Please check the code for syntax errors and try again.")

        # Right column: Chatbot area
        with chatbot_col:
            st.subheader('Drona codeGuru')
            with st.container(height=container_height):
                self.chat_with_document()
            # st.button('save chat',on_click=self.save_chat)
    
        # Display the output console below the split layout
        # st.markdown(f"<div class='console-output'>{code_output}</div>", unsafe_allow_html=True)
        st.subheader("Output Console:")
        st.code(code_output, language="python")


# Example usage
# app = App(
#     section_name="Section Name",
#     instr_file_path="path/to/instructions.md",
#     pgm_file_path="path/to/program.py",
#     session_key="session_key"
# )
# app.run()