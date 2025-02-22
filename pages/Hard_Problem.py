from pathlib import Path

from base_app import App

# Get the path to the current file (app.py)
current_file_path = Path(__file__).resolve()

# Navigate up two directories (CodeGuru)
base_dir = current_file_path.parents[1]  # parents[0] is 'pages', parents[1] is 'CodeGuru'

instruction_file_path = base_dir / 'files' / 'hard_problem.md'

code_file_path = base_dir / 'files' / 'PerfectionistPancakes.py'

app = App("### Easy Problem: Try Again", instruction_file_path, code_file_path, "hard_lab")
app.run()
