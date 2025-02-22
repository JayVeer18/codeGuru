import os
import subprocess

import streamlit as st
from dotenv import load_dotenv
from streamlit import session_state as ss
from streamlit_ace import st_ace

from chatbot import Chatbot

# ollama run llama3.1:8b
# Get the directory of the current script (where this Python file is located)
script_dir = os.path.dirname(os.path.abspath(__file__))

# Specify the path of the file
env_path = os.path.normpath(os.path.join(script_dir, ".env"))

# load environment variables from .env file
load_dotenv(dotenv_path=env_path, verbose=True, override=True)


class App:
    def __init__(self, section_name, instr_file_path, pgm_file_path, session_key,
                 page_title="Code Editor with Chatbot"):
        self.page_title = page_title
        self.section_name = section_name
        self.instr_file_path = instr_file_path
        self.pgm_file_path = pgm_file_path
        self.session_key = session_key

        # Initialize chatbot
        self.chatbot = Chatbot(file_path=self.instr_file_path, api_key=os.environ.get("OPENAI_API_KEY"),
                               framework="openai",
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
        st.markdown(
            """
            <style>
            .centered-heading {
                text-align: center;
                color: #2980b9 ; /* Example color */
                font-family: 'Georgia', serif; /* Example font */
                font-size: 2.2em;
                padding: 15px;
                text-shadow: 1px 1px 2px #333; /* Example text shadow */
            }
            .centered-heading h1 { /* Style the h1 within the class */
                margin-bottom: 0; /* Remove default h1 margin */
            }
            </style>
            """,
            unsafe_allow_html=True,
        )

        st.markdown("<div class='centered-heading'><h1>Drona: Your Guided Coding Companion</h1></div>",
                    unsafe_allow_html=True)

        # st.markdown(self.section_name)

        if f"messages_{self.session_key}" not in st.session_state:
            st.session_state[f"messages_{self.session_key}"] = []

    def display_chat_history(self):
        for message in reversed(st.session_state[f"messages_{self.session_key}"]):
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

    def execute_code(self, code):
        result = subprocess.run(['python', '-c', code], capture_output=True, text=True)
        return result

    def run(self):

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
                py_code = st_ace(value=pgm_code, language='python', theme=ss.theme, font_size=ss.font_size,
                                 show_gutter=ss.show_gutter, auto_update=False, key="editor")

            st.warning("**Please press the Apply button at  the end of the editor before running the code.**")
            # Create two columns for the buttons (side by side)
            button_col1, button_col2 = st.columns(2)

            with button_col1:
                # Run Code button
                if st.button('Run Code'):
                    result = self.execute_code(py_code)
                    if result.returncode == 0:
                        code_output = result.stdout
                        st.success("Code executed successfully!")
                    else:
                        code_output = result.stderr
                        st.error(
                            "An error occurred while executing the code. Please check the code for syntax errors and try again.")

            with button_col2:
                # Save Code button
                try:
                    # Save the content of the code editor to a file
                    file_name = self.session_key + '.py'
                    with open(file_name, "w") as file:
                        file.write(py_code)
                    st.success(f"Code successfully saved to {file_name}!")
                except Exception as e:
                    st.error(f"An error occurred while saving the code: {e}")

        # Right column: Chatbot area
        with chatbot_col:
            st.subheader('Drona: codeGuru')
            with st.container(height=container_height, key='chat_history', border=True):
                # Query input
                if query := st.chat_input("I'm here to help you out with the coding assignment", key='chat_input'):
                    # st.chat_message("user").markdown(query)

                    with st.spinner("Querying... please wait..."):
                        response = self.chatbot.invoke(query)
                        # st.markdown(response)

                    # Add assistant response to chat history
                    st.session_state[f"messages_{self.session_key}"].append({"role": "assistant", "content": response})

                    # Add user message to chat history
                    st.session_state[f"messages_{self.session_key}"].append({"role": "user", "content": query})

                self.display_chat_history()

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
