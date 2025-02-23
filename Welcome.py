from pathlib import Path

import streamlit as st
from streamlit import session_state as ss

st.set_page_config(page_title="Guided Problem-Solving Experiment", page_icon=":computer:",
                   initial_sidebar_state='expanded')

with st.sidebar:
    ss.theme = st.selectbox(
        "Editor Theme",
        ["monokai", "github", "solarized_dark", "solarized_light", "dracula"]
    )
    ss.font_size = st.slider("Font Size", 12, 24, 14)
    ss.show_gutter = st.checkbox("Show Line Numbers", value=True)

st.title("Welcome to the Guided Problem-Solving Experiment")

st.markdown(
    '##### This experiment is part of our research: **Guiding, Not Giving: Analyzing the Effectiveness of Guided Problem-Solving in CS Education**')
st.markdown('#### Abstract : ')

st.markdown(
    """This project develops an AI assistant to help students solve programming assignments by providing guidance and hints. The assistant encourages critical thinking, explains concepts, and breaks down problems into manageable parts. It avoids giving direct answers and instead promotes research and self-learning. The assistant uses a retrieval-augmented generation (RAG) model to provide context-specific hints based on assignment instructions. The system integrates a vector store for efficient document retrieval, enabling personalized assistance for each query.""")

st.markdown('#### Experiment Instructions : ')
st.markdown(""" In this experiment, you will be presented with two labs: **easy** and **hard**.  You will have **45 minutes** to complete both labs.  Following the labs, you will be asked to complete a short survey.

You can utilize the integrated ChatGPT assistant within the lab environment for help.""")

st.markdown("""<p style="color:red; font-weight:bold;">
!!! IMPORTANT : Your changes are not saved unless you press save code button. Also saved code won't be reloaded, saving is only for our internal stats. Please do not refresh the screen.!!!
</p>""", unsafe_allow_html=True)

st.markdown(""" Feel free to ask any questions you have.

**Good luck!**
""")

# Define the path to easy_problem.py
easy_problem_path = Path("pages") / "easy_problem.py"


# Function to load and execute the easy_problem.py script
def start_lab():
    if easy_problem_path.exists():
        with open(easy_problem_path) as f:
            exec(f.read())


# You can add a button or link to start the labs here:
if st.button("Start the Labs"):
    # Redirect to the lab pages or trigger the lab content
    st.write("Starting the labs...")

    # Run the easy_problem.py script
    st.switch_page("pages/Easy_Problem.py")
