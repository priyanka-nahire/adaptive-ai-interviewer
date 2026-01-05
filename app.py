import streamlit as st

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Adaptive AI Interviewer",
    page_icon="🤖",
    layout="centered"
)

# ---------------- HIDE SIDEBAR ----------------
st.markdown("""
<style>
[data-testid="stSidebar"] {
    display: none;
}
[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
}
[data-testid="stHeader"] {
    background: rgba(0,0,0,0);
}
</style>
""", unsafe_allow_html=True)

# ---------------- IMAGE ----------------
#st.image("assets/ai_interview.png", width=700)

# ---------------- CONTENT ----------------
st.markdown("""
<div style="
    background-color:white;
    padding:40px;
    border-radius:18px;
    max-width:760px;
    margin:auto;
    box-shadow:0 12px 30px rgba(0,0,0,0.25);
">
<h1 style="text-align:center;">Adaptive AI Interviewer</h1>
<h3 style="text-align:center;">Skill-Aware Intelligent Assessment System</h3>
<hr>

<p style="text-align:center;">
<b>Welcome to your safe space for interview practice 🤍</b>
</p>

<p style="text-align:center;">
Interviews are not about being perfect —  
they are about learning how to express what you already know.
</p>

<p style="text-align:center;">
This AI interviewer supports you, adapts to your level,
and helps you grow step by step.
</p>

<p style="text-align:center; font-weight:600;">
🌱 Every answer is progress  
🌱 Every mistake is learning  
🌱 Every session makes you stronger
</p>

<p style="text-align:center;">
Take a deep breath. Trust yourself. Start when you’re ready.
</p>
</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ---------------- FORM ----------------
skill = st.selectbox("💼 Select Skill", ["Java", "Python", "DSA", "SQL"])
level = st.selectbox("🎯 Select Experience Level", ["Beginner", "Intermediate", "Advanced"])

if st.button("🚀 Start Interview"):
    st.session_state.skill = skill
    st.session_state.level = level
    st.switch_page("pages/2_Interview.py")

