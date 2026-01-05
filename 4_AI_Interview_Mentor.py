import streamlit as st
from openai import OpenAI

# ---------- OPENAI CLIENT ----------
client = OpenAI()

# ---------- PAGE CONFIG ----------
st.set_page_config(
    page_title="AI Interview Mentor",
    page_icon="🎯",
    layout="centered"
)

# ---------- BLOCK DIRECT ACCESS ----------
if "total_score" not in st.session_state:
    st.switch_page("app.py")

# ---------- STYLE ----------
st.markdown("""
<style>
[data-testid="stSidebar"] { display: none; }
[data-testid="stAppViewContainer"] { background-color: #f5f7fb; }
.card {
    background: white;
    padding: 28px;
    border-radius: 18px;
    box-shadow: 0 10px 25px rgba(0,0,0,0.15);
    margin-bottom: 25px;
}
h1, h2, h3 { color: #000; }
</style>
""", unsafe_allow_html=True)

# ---------- HEADER ----------
st.markdown("""
<h1 style="text-align:center;">🎯 AI Interview Mentor</h1>
<p style="text-align:center; color:#444;">
Your personalized interview improvement & guidance plan
</p>
<hr>
""", unsafe_allow_html=True)

# ---------- BASIC DATA ----------
skill = st.session_state.skill
level = st.session_state.level
questions = st.session_state.questions
score = st.session_state.total_score
attempted = len(questions)

confidence = min(100, int((score / max(attempted * 10, 1)) * 100))

# ---------- SUMMARY ----------
st.markdown('<div class="card">', unsafe_allow_html=True)
st.markdown("### 🧾 Performance Overview")
st.markdown(f"""
- **Skill:** {skill}  
- **Level:** {level}  
- **Questions Attempted:** {attempted}  
- **Confidence Score:** **{confidence}%**
""")
st.markdown('</div>', unsafe_allow_html=True)

# ---------- AI COACHING PROMPT ----------
coach_prompt = f"""
You are an experienced interview mentor.

Candidate Skill: {skill}
Level: {level}
Confidence Score: {confidence}%

Tasks:
1. Identify 3 strengths
2. Identify 3 weaknesses
3. Provide a 2-week improvement roadmap
4. Give one motivational message

Return in clean bullet points.
"""

response = client.responses.create(
    model="gpt-4.1-mini",
    input=coach_prompt
)

mentor_feedback = response.output_text.strip()

# ---------- AI MENTOR FEEDBACK ----------
st.markdown('<div class="card">', unsafe_allow_html=True)
st.markdown("### 🤖 AI Mentor Guidance")
st.write(mentor_feedback)
st.markdown('</div>', unsafe_allow_html=True)

# ---------- ANSWER IMPROVEMENT EXAMPLE ----------
st.markdown('<div class="card">', unsafe_allow_html=True)
st.markdown("### ✨ How to Improve Your Answers")

st.markdown("""
**Before (Candidate Answer)**  
> “Java is object oriented language.”

**After (AI Mentor Improved Answer)**  
> “Java is a platform-independent, object-oriented programming language widely used to build scalable and secure enterprise-level applications.”

📌 *Tip:* Always include **what**, **why**, and **where it is used**.
""")

st.markdown('</div>', unsafe_allow_html=True)

# ---------- CONFIDENCE MESSAGE ----------
st.markdown('<div class="card">', unsafe_allow_html=True)
st.markdown("### 💬 Mentor’s Message")

if confidence >= 70:
    st.success("🌟 You are interview-ready. Focus on polishing answers.")
elif confidence >= 40:
    st.info("👍 You are on the right track. Practice will boost confidence.")
else:
    st.warning("💪 Don’t doubt yourself. Skills improve with consistency.")

st.markdown("""
> *“Confidence is built, not born. Every interview is a step forward.”*
""")

st.markdown('</div>', unsafe_allow_html=True)

# ---------- BUTTON ----------
if st.button("🏠 Back to Home"):
    for key in list(st.session_state.keys()):
        del st.session_state[key]
    st.switch_page("app.py")
