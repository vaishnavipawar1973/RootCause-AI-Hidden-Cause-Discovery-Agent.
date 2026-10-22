import streamlit as st
from collections import OrderedDict

st.set_page_config(
    page_title="RootCause AI | Smart Troubleshooter",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded",
)

SCENARIOS = {
    "Python Syntax Error": {
        "icon": "🐍",
        "category": "CODING",
        "description": "Your Python program stops before it can run.",
        "symptoms": ["A SyntaxError message appears", "The program does not start", "Python points to a line number"],
        "causes": OrderedDict([
            ("Missing colon", (0.36, "Python expects a colon after statements such as if, for, while, def, and class.", "Add a colon (:) at the end of the statement header.")),
            ("Unmatched brackets", (0.28, "An opening parenthesis, square bracket, or brace may not have a matching closing symbol.", "Check (), [], and {} around the reported line and the line above it.")),
            ("Incorrect indentation", (0.18, "A code block may use inconsistent spaces or tabs.", "Use consistent indentation, usually four spaces per level.")),
            ("Invalid expression or keyword", (0.18, "A keyword may be misspelled or an expression may not follow Python syntax.", "Review the reported line and the line immediately before it.")),
        ]),
        "tests": {
            "An if/for/while/def/class line has no colon": {"Missing colon": 3.2},
            "An opening bracket has no matching closing bracket": {"Unmatched brackets": 3.5},
            "The code block indentation looks inconsistent": {"Incorrect indentation": 3.0},
            "A keyword is misspelled or the expression looks invalid": {"Invalid expression or keyword": 3.0},
            "I have not checked yet": {},
        },
        "quick_tip": "Start by reading the exact error message. The real cause can be on the line just before the highlighted line.",
    },
    "Website Not Loading": {
        "icon": "🌐",
        "category": "NETWORK",
        "description": "A website will not open, or it stays on a loading/error screen.",
        "symptoms": ["A browser error appears", "The page loads very slowly", "Other websites may still work"],
        "causes": OrderedDict([
            ("Internet connection problem", (0.30, "A weak or disconnected network can stop the browser reaching the website.", "Open another website and reconnect Wi-Fi or mobile data if needed.")),
            ("DNS lookup problem", (0.22, "The domain name may not be resolving to an IP address.", "Try another network or restart the router.")),
            ("Website server is down", (0.24, "The website itself may be temporarily unavailable.", "Check the service status page or try again later.")),
            ("Browser cache or extension issue", (0.14, "Cached files or a browser extension may interfere with loading.", "Try a private window or another browser.")),
            ("Incorrect URL", (0.10, "A typo in the address can send the browser to the wrong location.", "Check the spelling and domain in the address bar.")),
        ]),
        "tests": {
            "Other websites also fail to open": {"Internet connection problem": 3.4},
            "Other websites work, but this domain fails on multiple devices": {"DNS lookup problem": 2.0, "Website server is down": 2.7},
            "The website works on another network": {"DNS lookup problem": 2.8, "Internet connection problem": 1.4},
            "It works in a private window or another browser": {"Browser cache or extension issue": 3.5},
            "The address may have a spelling mistake": {"Incorrect URL": 3.5},
            "I have not checked yet": {},
        },
        "quick_tip": "Test another trusted website first. This helps separate a local connection problem from a website-specific problem.",
    },
    "Laptop Overheating": {
        "icon": "💻",
        "category": "DEVICE",
        "description": "Your laptop becomes unusually hot, loud, or slow.",
        "symptoms": ["The fan runs loudly", "The device feels very hot", "Performance becomes slow"],
        "causes": OrderedDict([
            ("Blocked vents or dust", (0.30, "Restricted airflow can stop heat from escaping.", "Use a hard, flat surface and have vents cleaned safely if needed.")),
            ("High CPU/GPU workload", (0.28, "Games, video rendering, or many applications can generate extra heat.", "Check Task Manager and close unnecessary heavy tasks.")),
            ("Poor ventilation or hot room", (0.18, "Soft surfaces and high room temperature reduce cooling.", "Move to a cool, flat surface with space around the vents.")),
            ("Fan or cooling hardware fault", (0.14, "A failing fan may not remove heat effectively.", "If overheating persists, power down and arrange a qualified service check.")),
            ("Background process", (0.10, "Unexpected processes can keep the processor busy.", "Review running processes and run a reputable security scan.")),
        ]),
        "tests": {
            "The vents are blocked or full of dust": {"Blocked vents or dust": 3.3},
            "CPU usage is high when no heavy app is open": {"Background process": 2.8, "High CPU/GPU workload": 1.4},
            "It gets hot mainly during gaming or editing": {"High CPU/GPU workload": 3.4},
            "It sits on a bed, blanket, or soft surface": {"Poor ventilation or hot room": 3.5},
            "The fan makes unusual noises or does not spin": {"Fan or cooling hardware fault": 3.5},
            "I have not checked yet": {},
        },
        "quick_tip": "If the laptop becomes extremely hot, smells unusual, or shuts down repeatedly, turn it off and seek qualified help.",
    },
    "Student Website Login Failure": {
        "icon": "🎓",
        "category": "COLLEGE PORTAL",
        "description": "You cannot sign in to a college portal or learning website.",
        "symptoms": ["Login is rejected", "The page returns to the login screen", "Password reset may fail"],
        "causes": OrderedDict([
            ("Incorrect username or password", (0.32, "A typo or old password can cause the portal to reject the login.", "Re-enter the official username and use the official password reset if needed.")),
            ("Account inactive or locked", (0.20, "A new account may need activation, or repeated failed attempts may lock it.", "Check activation instructions or contact college IT support.")),
            ("Portal server issue", (0.18, "A server outage can prevent even valid users from logging in.", "Try again later or check the college notice page.")),
            ("Browser cookies/cache issue", (0.16, "Session cookies may be blocked or stale.", "Try a private window or another browser.")),
            ("Network or VPN restriction", (0.14, "Some portals require a specific network or restrict VPN routes.", "Try the college-approved network and disable an unneeded VPN.")),
        ]),
        "tests": {
            "Password reset says the account details are not recognized": {"Incorrect username or password": 2.3, "Account inactive or locked": 2.0},
            "Classmates also cannot log in": {"Portal server issue": 3.4},
            "It works in a private window or different browser": {"Browser cookies/cache issue": 3.5},
            "It works only on the college network": {"Network or VPN restriction": 3.5},
            "The account is new or was locked after repeated attempts": {"Account inactive or locked": 3.5},
            "I have not checked yet": {},
        },
        "quick_tip": "Never share your password or OTP with anyone. Use only the official college portal and support contact.",
    },
    "Slow Computer": {
        "icon": "⚡",
        "category": "PERFORMANCE",
        "description": "Your computer starts slowly or applications take too long to respond.",
        "symptoms": ["Slow startup", "Apps freeze or lag", "High disk or memory usage"],
        "causes": OrderedDict([
            ("Too many startup/background apps", (0.28, "Many apps can consume memory and CPU after startup.", "Disable unneeded startup apps and close unused programs.")),
            ("Low available memory", (0.22, "Many open tabs and apps can exhaust RAM.", "Close unused apps and tabs; consider an upgrade if consistently needed.")),
            ("Low disk space", (0.18, "A nearly full drive can affect updates and temporary files.", "Back up important files before removing unneeded files.")),
            ("Storage drive issue", (0.16, "A failing or slow drive can cause long load times.", "Back up important files and use the operating system's drive-health tools.")),
            ("Pending updates or scan", (0.16, "Updates and scans can temporarily use significant resources.", "Check update status and allow maintenance to finish.")),
        ]),
        "tests": {
            "Many apps open automatically at startup": {"Too many startup/background apps": 3.4},
            "Memory usage is nearly full": {"Low available memory": 3.5},
            "The main drive has very little free space": {"Low disk space": 3.5},
            "The drive makes unusual noises or files are unreadable": {"Storage drive issue": 3.5},
            "The slowdown started during an update or security scan": {"Pending updates or scan": 3.5},
            "I have not checked yet": {},
        },
        "quick_tip": "Open Task Manager and check CPU, Memory, and Disk usage before installing any cleaner app.",
    },
}

def rank_causes(scenario, selected_clues):
    causes = SCENARIOS[scenario]["causes"]
    scores = {name: max(0.01, details[0]) for name, details in causes.items()}
    for clue in selected_clues:
        for cause, multiplier in SCENARIOS[scenario]["tests"][clue].items():
            scores[cause] *= multiplier
    total = sum(scores.values()) or 1
    return sorted(
        [(name, score / total, causes[name][1], causes[name][2]) for name, score in scores.items()],
        key=lambda item: item[1],
        reverse=True,
    )

def reset_clues():
    st.session_state.selected_clues = []

st.markdown("""
<style>
:root { color-scheme: dark; }
.stApp { background: radial-gradient(circle at 10% 0%, #18263b 0%, #0b1020 45%, #0a0e18 100%); }
.block-container { max-width: 1250px; padding-top: 2rem; padding-bottom: 3rem; }
[data-testid="stSidebar"] { background: #111827; border-right: 1px solid #26344a; }
.hero { padding: 1.55rem 1.7rem; border: 1px solid #2b4260; border-radius: 22px;
        background: linear-gradient(120deg, rgba(44,78,124,.42), rgba(24,34,56,.58)); margin-bottom: 1.1rem; }
.hero-kicker { color: #8db8ff; text-transform: uppercase; letter-spacing: .13em; font-size: .76rem; font-weight: 800; }
.hero h1 { font-size: clamp(2rem, 4vw, 3rem); margin: .35rem 0 .35rem 0; color: #f8fbff; }
.hero p { color: #c5d4e9; font-size: 1.02rem; margin: 0; }
.section-card { border: 1px solid #26364d; border-radius: 18px; padding: 1.2rem 1.3rem; background: rgba(17,26,43,.82); }
.small-muted { color: #a8b7cc; font-size: .9rem; }
.pill { display: inline-block; background: #203a5b; color: #b9d7ff; border-radius: 999px; padding: .3rem .65rem; font-size: .76rem; font-weight: 800; letter-spacing: .04em; }
div.stButton > button[kind="primary"] { border: 0; border-radius: 12px; min-height: 3rem; font-weight: 750; }
div[data-testid="stMetric"] { background: #111c2e; border: 1px solid #2b3b52; border-radius: 15px; padding: 1rem; }
div[data-testid="stProgressBar"] > div { border-radius: 999px; }
hr { border-color: #28384e; }
</style>
""", unsafe_allow_html=True)

if "selected_clues" not in st.session_state:
    st.session_state.selected_clues = []
if "analysis_done" not in st.session_state:
    st.session_state.analysis_done = False
if "last_scenario" not in st.session_state:
    st.session_state.last_scenario = None

with st.sidebar:
    st.markdown("## 🧠 RootCause AI")
    st.caption("HIDDEN CAUSE DISCOVERY AGENT")
    st.divider()
    scenario = st.selectbox("What problem are you facing?", list(SCENARIOS.keys()), format_func=lambda x: f"{SCENARIOS[x]['icon']}  {x}")
    st.markdown("### Quick guide")
    st.markdown("1. Choose a problem\n2. Tick the clues you observed\n3. Analyze the evidence\n4. Follow the recommended next step")
    st.divider()
    st.markdown("**Runs offline**")
    st.caption("No API key or account required.")
    if st.button("↺ Start over", use_container_width=True):
        st.session_state.selected_clues = []
        st.session_state.analysis_done = False
        st.session_state.last_scenario = scenario
        st.rerun()

if st.session_state.last_scenario != scenario:
    st.session_state.selected_clues = []
    st.session_state.analysis_done = False
    st.session_state.last_scenario = scenario

data = SCENARIOS[scenario]
st.markdown(f"""
<div class="hero">
  <div class="hero-kicker">Offline diagnostic assistant · {data['category']}</div>
  <h1>{data['icon']} RootCause AI</h1>
  <p>Find the likely reason behind a problem — one clue at a time.</p>
</div>
""", unsafe_allow_html=True)

intro, status = st.columns([2.1, 1])
with intro:
    st.markdown(f"## {data['icon']} {scenario}")
    st.write(data["description"])
    st.markdown('<p class="small-muted">This is a guided troubleshooting demo, not a replacement for an expert.</p>', unsafe_allow_html=True)
with status:
    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.markdown("**YOUR SESSION**")
    st.markdown(f"**{len(data['symptoms'])}** common symptoms")
    st.markdown(f"**{len(data['causes'])}** possible causes")
    st.markdown("**Offline** · No API key")
    st.markdown('</div>', unsafe_allow_html=True)

with st.expander("👀 What are the common symptoms?", expanded=False):
    for symptom in data["symptoms"]:
        st.markdown(f"- {symptom}")

st.divider()
st.markdown("## 1 · Tell the agent what you observed")
st.write("Select every clue that matches what you have already checked. If you are unsure, leave them unchecked.")

options = list(data["tests"].keys())
selected = []
with st.container(border=True):
    st.markdown("**Diagnostic clues**")
    clue_cols = st.columns(2, gap="large")
    for i, clue in enumerate(options):
        with clue_cols[i % 2]:
            checked = st.checkbox(clue, value=clue in st.session_state.selected_clues, key=f"clue_{scenario}_{i}")
            if checked:
                selected.append(clue)
    st.session_state.selected_clues = selected
    st.caption(f"{len(selected)} clue{'s' if len(selected) != 1 else ''} selected")

button_col, hint_col = st.columns([1, 2])
with button_col:
    analyze = st.button("🔎 Analyze my clues", type="primary", use_container_width=True)
with hint_col:
    st.caption("Your results update when you analyze. You can change clues and analyze again.")

if analyze:
    st.session_state.analysis_done = True

if st.session_state.analysis_done:
    ranked = rank_causes(scenario, st.session_state.selected_clues)
    top_name, top_score, top_evidence, top_fix = ranked[0]
    st.divider()
    st.markdown("## 2 · Your diagnostic report")
    st.success(f"Most likely cause to investigate first: **{top_name}**")
    m1, m2, m3 = st.columns(3)
    m1.metric("Top-ranked cause", top_name)
    m2.metric("Relative score", f"{top_score * 100:.1f}%")
    m3.metric("Clues used", len(st.session_state.selected_clues))

    st.markdown("### Possible causes, ranked")
    st.caption("Higher scores mean a closer match within this demo's small rule set — not a verified real-world probability.")
    for i, (name, score, evidence, fix) in enumerate(ranked, start=1):
        with st.container(border=True):
            heading, score_col = st.columns([3, 1])
            with heading:
                st.markdown(f"**{i}. {name}**")
            with score_col:
                st.markdown(f"**{score * 100:.1f}% relative score**")
            st.progress(float(score))
            st.markdown(f"**Why it may fit:** {evidence}")
            if i == 1:
                st.info(f"**Recommended next step:** {fix}")
            else:
                with st.expander("See suggested action"):
                    st.write(fix)

    st.markdown("### 🧭 Agent reasoning")
    if st.session_state.selected_clues:
        st.write("The agent starts with baseline weights, adjusts the related causes using your selected clues, then normalizes the scores and ranks the results.")
        st.markdown("**Clues considered:**")
        for clue in st.session_state.selected_clues:
            st.markdown(f"- {clue}")
    else:
        st.warning("No clues were selected. This ranking uses only the baseline weights. Select clues above for a more useful result.")

    st.markdown("### 💡 Helpful reminder")
    st.info(data["quick_tip"])
else:
    st.markdown("""
    <div class="section-card">
      <h4>✨ Your report will appear here</h4>
      <p class="small-muted">Choose the clues above, then press <b>Analyze my clues</b>. The agent will rank possible causes and suggest a next action.</p>
    </div>
    """, unsafe_allow_html=True)

with st.expander("🎓 Project details & viva preparation"):
    st.markdown("""
**Objective:** identify and rank possible hidden causes of a problem using symptoms and diagnostic clues.

**AI technique:** rule-based diagnostic reasoning with weighted evidence scoring. It is inspired by Bayesian reasoning, but it is not a trained machine-learning model and its scores are not calibrated probabilities.

**Input:** problem category and diagnostic clues.  
**Output:** ranked causes, relative scores, evidence explanations, and suggested next steps.  
**Technology:** Python and Streamlit.  
**Future scope:** expert-verified knowledge, calibrated probabilities, user feedback, or a Bayesian network / machine-learning model.
""")

st.divider()
st.caption("RootCause AI · College project prototype · Offline demo")
