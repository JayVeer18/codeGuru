import io
import json
import os
import re
import runpy
import sys

import streamlit as st
from dotenv import load_dotenv
from streamlit import session_state as ss
from streamlit.components.v1 import html
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

        ss.pgm_code = self.read_file(self.pgm_file_path)

    def display_chat_history(self):
        for message in reversed(st.session_state[f"messages_{self.session_key}"]):
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

    def execute_code(self, code):
        # print('executing code')
        file = self.save_file(code)
        # result = subprocess.run(['python', '-c', code], capture_output=True, text=True)

        # Capture output
        output_buffer = io.StringIO()
        sys.stdout = output_buffer  # Redirect stdout

        try:
            # Run the script
            runpy.run_path(file, run_name="__main__")
        except Exception as e:
            st.error(f"An error occurred while executing the code: {e}")
        finally:
            # Restore original stdout
            sys.stdout = sys.__stdout__

        # Get the captured output
        result = output_buffer.getvalue()

        if result:
            return result
        else:
            st.warning("No output generated. Please check your script for print statements.")
            return "No output"

    # Function to extract Mermaid code and split instructions into three parts
    def split_instructions(self, instructions: str) -> tuple:
        # Regex to extract the Mermaid code block
        match = re.search(r'```mermaid\n(.*?)\n```', instructions, re.DOTALL)

        if match:
            # Split instructions before, mermaid code, and after
            before_mermaid = instructions[:match.start()]  # Part before Mermaid code
            mermaid_code = match.group(1)  # The Mermaid code
            after_mermaid = instructions[match.end():]  # Part after Mermaid code
            return before_mermaid, mermaid_code, after_mermaid
        return instructions, "", ""  # If no Mermaid code is found, return all as before part

    # Function to render Mermaid code
    def mermaid(self, code: str) -> None:
        html(
            f"""
            <pre class="mermaid">
                {code}
            </pre>

            <script type="module">
                import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs';
                mermaid.initialize({{ startOnLoad: true }});
            </script>
            """, height=700
        )

    def run(self):

        # Display instructions with images
        instructions = self.read_file(self.instr_file_path)

        # Split the instructions into before, mermaid code, and after parts
        before_mermaid, mermaid_code, after_mermaid = self.split_instructions(instructions)

        # Display the part before the Mermaid diagram
        st.markdown(before_mermaid, unsafe_allow_html=True)

        # If there's any Mermaid code, render it
        if mermaid_code:
            self.mermaid(mermaid_code)

        # Display the part after the Mermaid diagram
        st.markdown(after_mermaid, unsafe_allow_html=True)

        # Initialize code_output
        code_output = ""
        # Split layout for py_code editor and chatbot
        editor_col, chatbot_col = st.columns(2)
        container_height = 650
        # Left column: Code editor
        with editor_col:
            st.subheader("Drona Lab")
            with st.container(height=container_height):
                # Display py_code editor with loaded file content
                ss.pgm_code = py_code = st_ace(value=ss.pgm_code, language='python', theme=ss.theme,
                                               font_size=ss.font_size,
                                               show_gutter=ss.show_gutter, auto_update=False, key="editor")

            st.warning("**Please press the Apply button at  the end of the editor before running the code.**")
            # Create two columns for the buttons (side by side)
            button_col1, button_col2 = st.columns(2)

            with button_col1:
                # Run Code button
                if st.button('Run Code'):
                    code_output = self.execute_code(py_code)

            with button_col2:
                if st.button('Save Code'):
                    # Save Code button
                    file_name = self.save_file(py_code)
                    st.success(f"Code successfully saved to {file_name}!")

        # Right column: Chatbot area
        with chatbot_col:
            st.subheader('DronaHint: Get Clues, Not Solutions')
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

    def save_file(self, py_code):
        try:
            # Save the content of the code editor to a file
            file_name = self.session_key + '_chat.json'
            with open(file_name, "w", encoding="utf-8") as file:
                json.dump(st.session_state[f"messages_{self.session_key}"], file, indent=4, ensure_ascii=False)

            file_name = self.session_key + '.py'
            with open(file_name, "w") as file:
                file.write(py_code)
            return file_name
        except Exception as e:
            st.error(f"An error occurred while saving the code: {e}")

# Example usage
# app = App(
#     section_name="Section Name",
#     instr_file_path="path/to/instructions.md",
#     pgm_file_path="path/to/program.py",
#     session_key="session_key"
# )
# app.run()
