# RootCause AI — Hidden Cause Discovery Agent

A beginner-friendly offline troubleshooting project built with Python and Streamlit.

## Features
- Five demo problems: Python syntax error, website not loading, laptop overheating, student website login failure, and slow computer.
- Select diagnostic clues and see causes ranked dynamically.
- Relative scores, explanations, and suggested next steps.
- No API key required.

## Requirements
- Python 3.9 or newer
- Streamlit (installed by the launcher)

## Run on Windows
1. Extract this ZIP.
2. Install Python from https://www.python.org/downloads/ if needed. During installation, tick **Add Python to PATH**.
3. Open the extracted `RootCause_AI_Project` folder.
4. Double-click `run_windows.bat`.
5. Wait for the browser to open. If it does not, visit the URL printed in the terminal, usually http://localhost:8501.

## Run manually
Open Command Prompt in this folder and run:

```bash
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

If `python` is not recognized, try `py -m pip install -r requirements.txt` and `py -m streamlit run app.py`.

## Important note
This is an educational prototype. Percentages are illustrative relative scores from a small rule-based knowledge base, not verified real-world probabilities or a replacement for expert diagnosis.
