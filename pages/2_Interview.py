import streamlit as st
import os
from openai import OpenAI

# ---------- OPENAI CLIENT ----------
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# ---------- PAGE CONFIG ----------
st.set_page_config(
    page_title="AI Interview",
    page_icon="🧠",
    layout="centered"
)

# ---------- BLOCK DIRECT ACCESS ----------
if "skill" not in st.session_state or "level" not in st.session_state:
    st.switch_page("app.py")

# ---------- STYLE ----------
st.markdown("""
<style>
[data-testid="stSidebar"] { display: none; }
[data-testid="stAppViewContainer"] { background-color: #ffffff; }
h1, h2, h3, p { color: #000000; }
</style>
""", unsafe_allow_html=True)

# ---------- RESET WHEN SKILL / LEVEL CHANGES ----------
context = f"{st.session_state.skill}_{st.session_state.level}"

if "context" not in st.session_state or st.session_state.context != context:
    st.session_state.context = context
    st.session_state.questions = []
    st.session_state.q_index = 0
    st.session_state.feedback = None
    st.session_state.total_score = 0

# ---------- AI QUESTION ----------
def generate_question(skill, level, asked):
    prompt = f"""
You are a professional technical interviewer.

Skill: {skill}
Level: {level}

Already asked questions:
{asked}

Ask ONE new commonly asked interview question.
Return only the question.
"""
    res = client.responses.create(
        model="gpt-4.1-mini",
        input=prompt
    )
    return res.output_text.strip()

# ---------- AI EVALUATION ----------
def evaluate_answer(question, answer):
    prompt = f"""
You are an interviewer.

Question:
{question}

Candidate Answer:
{answer}

Give:
1. Short feedback (2 lines)
2. Score out of 10

Format:
Feedback: ...
Score: X/10
"""
    res = client.responses.create(
        model="gpt-4.1-mini",
        input=prompt
    )
    return res.output_text.strip()

# ---------- LOAD QUESTION ----------
if st.session_state.q_index == len(st.session_state.questions):
    q = generate_question(
        st.session_state.skill,
        st.session_state.level,
        st.session_state.questions
    )
    st.session_state.questions.append(q)

question = st.session_state.questions[st.session_state.q_index]

# ---------- HEADER ----------
st.markdown(f"""
<h1 style="text-align:center;">🧠 AI Interview Session</h1>
<p style="text-align:center;">
Skill: <b>{st.session_state.skill}</b> |
Level: <b>{st.session_state.level}</b>
</p>
<hr>
""", unsafe_allow_html=True)

# ---------- QUESTION CARD ----------
st.markdown("""
<div style="
background:#ffffff;
padding:30px;
border-radius:14px;
max-width:760px;
margin:auto;
box-shadow:0 8px 20px rgba(0,0,0,0.15);
">
""", unsafe_allow_html=True)

st.markdown(f"### Question {st.session_state.q_index + 1}")
st.markdown(f"**{question}**")

st.markdown("### ✍️ Your Answer")
final_answer = st.text_area("Type your answer here", height=130)

st.markdown("### 🎤 Voice Answer (Disabled)")
st.info("Voice input is disabled to avoid billing issues. Please type your answer.")

# ---------- BUTTONS ----------
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("✅ Submit Answer"):
        if final_answer.strip():
            result = evaluate_answer(question, final_answer)
            st.session_state.feedback = result

            if "Score:" in result:
                score = int(result.split("Score:")[1].split("/")[0])
                st.session_state.total_score += score

with col2:
    if st.button("Next ➡️"):
        st.session_state.feedback = None
        st.session_state.q_index += 1
        st.rerun()

with col3:
    if st.button("🏁 End Interview"):
        st.switch_page("pages/3_Report.py")


# ---------- FEEDBACK ----------
if st.session_state.feedback:
    st.markdown("---")
    st.markdown("### 🧠 AI Feedback")
    st.success(st.session_state.feedback)

st.markdown("</div>", unsafe_allow_html=True)

