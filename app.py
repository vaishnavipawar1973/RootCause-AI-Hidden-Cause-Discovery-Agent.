import streamlit as st
from collections import OrderedDict

st.set_page_config(page_title="RootCause AI", page_icon="🧠", layout="wide")

SCENARIOS = {
    "Python Syntax Error": {
        "description": "A Python script stops before running because its code cannot be parsed.",
        "symptoms": ["SyntaxError message", "Program does not start", "Error points to a line"],
        "causes": OrderedDict([
            ("Missing colon", (0.36, "Python requires a colon after if, for, while, class, and def.", "Add ':' at the end of the statement header.")),
            ("Unmatched brackets", (0.28, "An opening parenthesis, bracket, or brace may not have a matching closer.", "Check matching parentheses, square brackets, and braces.")),
            ("Incorrect indentation", (0.18, "A block may not be indented consistently.", "Use consistent indentation, usually four spaces per level.")),
            ("Invalid expression or keyword", (0.18, "A keyword may be misspelled or the expression may not follow Python grammar.", "Review the reported line and the line immediately before it.")),
        ]),
        "tests": {
            "An if/for/while/def/class line has no colon": {"Missing colon": 3.2},
            "An opening bracket has no matching closing bracket": {"Unmatched brackets": 3.5},
            "The code block indentation looks inconsistent": {"Incorrect indentation": 3.0},
            "A keyword is misspelled or the expression looks invalid": {"Invalid expression or keyword": 3.0},
            "I have not checked yet": {},
        }
    },
    "Website Not Loading": {
        "description": "A website does not open or keeps showing a loading/error screen.",
        "symptoms": ["Browser error", "Long loading time", "Other websites may still work"],
        "causes": OrderedDict([
            ("Internet connection problem", (0.30, "A weak or disconnected network can prevent the browser reaching the site.", "Open another website and reconnect Wi-Fi/mobile data if needed.")),
            ("DNS lookup problem", (0.22, "The domain name may not be resolving to an IP address.", "Try another network or restart the router.")),
            ("Website server is down", (0.24, "The website itself may be temporarily unavailable.", "Check the service status page or try again later.")),
            ("Browser cache or extension issue", (0.14, "Cached files or an extension can interfere with loading.", "Try a private window or another browser.")),
            ("Incorrect URL", (0.10, "A typo in the address can send the browser to the wrong location.", "Check the spelling and domain in the address bar.")),
        ]),
        "tests": {
            "Other websites also fail to open": {"Internet connection problem": 3.4},
            "Other websites work, but this domain fails on multiple devices": {"DNS lookup problem": 2.0, "Website server is down": 2.7},
            "The website works on another network": {"DNS lookup problem": 2.8, "Internet connection problem": 1.4},
            "It works in a private window or another browser": {"Browser cache or extension issue": 3.5},
            "The address may have a spelling mistake": {"Incorrect URL": 3.5},
            "I have not checked yet": {},
        }
    },
    "Laptop Overheating": {
        "description": "A laptop becomes unusually hot, loud, or slow during use.",
        "symptoms": ["Fan runs loudly", "Device feels hot", "Performance slows down"],
        "causes": OrderedDict([
            ("Blocked vents or dust", (0.30, "Restricted airflow can stop heat from escaping.", "Use a hard surface and have vents cleaned safely if needed.")),
            ("High CPU/GPU workload", (0.28, "Games, video rendering, or many apps can generate extra heat.", "Check Task Manager and close unnecessary heavy tasks.")),
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
        }
    },
    "Student Website Login Failure": {
        "description": "A student cannot log in to a college portal or learning website.",
        "symptoms": ["Login rejected", "Page loops back to login", "Password reset may fail"],
        "causes": OrderedDict([
            ("Incorrect username or password", (0.32, "A typo or old password can cause rejection.", "Re-enter the official username and use password reset if needed.")),
            ("Account inactive or locked", (0.20, "New or repeatedly failed accounts may need activation or unlocking.", "Check activation instructions or contact college IT support.")),
            ("Portal server issue", (0.18, "A server outage can prevent valid logins.", "Try again later or check the college notice page.")),
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
        }
    },
    "Slow Computer": {
        "description": "A computer takes a long time to start or apps respond slowly.",
        "symptoms": ["Slow startup", "Apps freeze", "High disk or memory usage"],
        "causes": OrderedDict([
            ("Too many startup/background apps", (0.28, "Many apps can consume memory and CPU after startup.", "Disable unneeded startup apps and close unused programs.")),
            ("Low available memory", (0.22, "Many open tabs and apps can exhaust RAM.", "Close unused apps/tabs and consider an upgrade if consistently needed.")),
            ("Low disk space", (0.18, "A nearly full drive can affect updates and temporary files.", "Remove unneeded files after backing up important data.")),
            ("Storage drive issue", (0.16, "A failing or slow drive can cause long load times.", "Back up important files and run the operating system drive health tools.")),
            ("Pending updates or scan", (0.16, "Updates and scans can temporarily use significant resources.", "Check update status and allow maintenance to finish.")),
        ]),
        "tests": {
            "Many apps open automatically at startup": {"Too many startup/background apps": 3.4},
            "Memory usage is nearly full": {"Low available memory": 3.5},
            "The main drive has very little free space": {"Low disk space": 3.5},
            "The drive makes unusual noises or files are unreadable": {"Storage drive issue": 3.5},
            "The slowdown started during an update or security scan": {"Pending updates or scan": 3.5},
            "I have not checked yet": {},
        }
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
        key=lambda item: item[1], reverse=True
    )

st.title("🧠 RootCause AI")
st.subheader("Hidden Cause Discovery Agent")
st.write("An offline troubleshooting assistant that ranks possible causes from symptoms and diagnostic clues.")
st.info("Educational demo: percentages are illustrative relative scores from a small rule-based knowledge base, not guaranteed real-world probabilities.")

with st.sidebar:
    st.header("Choose a problem")
    scenario = st.selectbox("Problem type", list(SCENARIOS.keys()))
    st.divider()
    st.caption("No API key required. The app runs locally on your computer.")

data = SCENARIOS[scenario]
st.header(scenario)
st.write(data["description"])
left, right = st.columns(2)
with left:
    st.markdown("**Common symptoms**")
    for symptom in data["symptoms"]:
        st.write("• " + symptom)
with right:
    st.markdown("**Agent workflow**")
    st.write("1. Starts with baseline cause weights.\n2. Uses your clues to adjust scores.\n3. Ranks possible causes and suggests next steps.")

st.divider()
st.subheader("1. Select diagnostic clues")
st.write("Tick any checks you have already done.")
options = list(data["tests"].keys())
selected = []
cols = st.columns(2)
for i, clue in enumerate(options):
    with cols[i % 2]:
        if st.checkbox(clue, key=scenario + "_" + clue):
            selected.append(clue)

ranked = rank_causes(scenario, selected)
top_name, top_score, top_evidence, top_fix = ranked[0]
st.subheader("2. Results")
m1, m2, m3 = st.columns(3)
m1.metric("Top suspected cause", top_name)
m2.metric("Relative score", f"{top_score * 100:.1f}%")
m3.metric("Clues selected", len(selected))

st.markdown("#### Ranked possible causes")
for i, (name, score, evidence, fix) in enumerate(ranked, start=1):
    with st.container(border=True):
        st.markdown(f"**{i}. {name}**")
        st.progress(float(score), text=f"Relative score: {score * 100:.1f}%")
        st.write("**Evidence:** " + evidence)
        if i == 1:
            st.success("**Suggested next step:** " + fix)

st.subheader("3. Agent explanation")
if selected:
    st.write("The agent began with baseline weights, then multiplied the scores of causes related to your selected clues. It normalized the scores to total 100%.")
    st.write("Selected clues: " + "; ".join(selected))
else:
    st.write("No clues selected. The ranking is based on baseline weights. Select clues above to update the results.")

with st.expander("Project details and viva preparation"):
    st.markdown("""
    **Objective:** rank possible hidden causes of a problem from observed symptoms.

    **AI technique:** rule-based diagnostic reasoning with weighted evidence scoring. It is inspired by Bayesian reasoning, but it is not a trained machine-learning model and scores are not calibrated probabilities.

    **Input:** problem category and diagnostic clues.  
    **Output:** ranked causes, relative scores, evidence explanations, and suggested next steps.  
    **Technology:** Python and Streamlit.  
    **Future scope:** expert-verified knowledge, calibrated probabilities, user feedback, and a proper Bayesian network or machine-learning model.
    """)

st.caption("RootCause AI • College project prototype • Offline demo")
