# RootCause AI — Hidden Cause Discovery Agent

An interactive, beginner-friendly offline troubleshooting demo built with Python and Streamlit.

## Features
- Five sample problems: Python syntax error, website not loading, laptop overheating, student portal login failure, and slow computer.
- Clear guided steps and interactive diagnostic clues.
- Ranked possible causes, relative scores, explanations, and recommended next steps.
- Responsive, modern dark UI with clearer step-by-step guidance.
- Try-a-sample button, clear/reset controls, hover feedback, and interactive diagnostic clues.
- No API key or account required.

## Run on Windows
1. Download and extract this ZIP.
2. Install Python 3.9 or newer from https://www.python.org/downloads/ if needed. During setup, tick **Add Python to PATH**.
3. Open the extracted `RootCause_AI_Friendly` folder.
4. Double-click `run_windows.bat`.
5. Wait for the browser to open. If it does not, open the URL shown in the terminal, usually http://localhost:8501.

## Run manually
Open Command Prompt in the project folder and run:

```bash
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

If `python` is not recognized, try replacing `python` with `py`.

## Important note
This is an educational rule-based prototype. Percentages are illustrative relative scores from a small knowledge base, not verified real-world probabilities and not a replacement for expert diagnosis.
