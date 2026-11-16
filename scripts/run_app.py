"""Launcher for the RAG Demo Web Interface."""

import subprocess
import sys
import shutil

def main():
    if shutil.which("streamlit"):
        print("Launching Streamlit demo on http://localhost:8501 ...")
        subprocess.run(["streamlit", "run", "app.py"])
    else:
        print("Streamlit not found on PATH. Install via: pip install streamlit")
        print("Running CLI query fallback:")
        subprocess.run([sys.executable, "scripts/ask.py", "--question", "What are penalties for plagiarism?"])

if __name__ == "__main__":
    main()
