import os
from base_app import App

# Get the directory of the current script (where this Python file is located)
script_dir = os.path.dirname(os.path.abspath(__file__))

# Specify the path of the README.md file
readme_path = os.path.normpath(os.path.join(script_dir,"README.md"))

# Specify the path of the Python file
file_path = os.path.normpath(os.path.join(script_dir,"OperationStation.py"))

app = App("### Lab:4 Operation Station", readme_path, file_path, "lab4")
app.run()