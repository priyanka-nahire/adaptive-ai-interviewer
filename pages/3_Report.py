import streamlit as st

# ---------- PAGE CONFIG ----------
st.set_page_config(
    page_title="Interview Report",
    page_icon="📊",
    layout="centered"
)

# ---------- BLOCK DIRECT ACCESS ----------
if "total_score" not in st.session_state:
    st.switch_page("app.py")

# ---------- STYLE ----------
st.markdown("""
<style>
[data-testid="stSidebar"] { display: none; }
[data-testid="stAppViewContainer"] { background-color: #f7f9fc; }
.card {
    background: white;
    padding: 25px;
    border-radius: 16px;
    box-shadow: 0 8px 20px rgba(0,0,0,0.15);
    margin-bottom: 25px;
}
h1, h2, h3 { color: #000000; }
</style>
""", unsafe_allow_html=True)

# ---------- HEADER ----------
st.markdown("""
<h1 style="text-align:center;">📊 AI Interview Performance Report</h1>
<p style="text-align:center; color:#444;">
Your personalized interview feedback & growth insights
</p>
<hr>
""", unsafe_allow_html=True)

# ---------- SUMMARY CARD ----------
st.markdown('<div class="card">', unsafe_allow_html=True)

questions_attempted = st.session_state.q_index
score = st.session_state.total_score
confidence = min(100, int((score / max(questions_attempted * 10, 1)) * 100))

st.markdown("### 🧾 Interview Summary")
st.markdown(f"""
- **Skill:** {st.session_state.skill}  
- **Level:** {st.session_state.level}  
- **Questions Attempted:** {questions_attempted}  
- **Total Score:** {score}  
- **Confidence Level:** **{confidence}%**
""")

st.markdown('</div>', unsafe_allow_html=True)

# ---------- CONFIDENCE MESSAGE ----------
st.markdown('<div class="card">', unsafe_allow_html=True)

st.markdown("### 💬 Confidence Insight")

if confidence >= 70:
    st.success("🌟 Excellent performance! You are interview ready.")
elif confidence >= 40:
    st.info("👍 Good effort. With a bit more practice, you’ll do great.")
else:
    st.warning("💪 Don’t worry. Confidence comes from practice — keep going!")

st.markdown("""
> *“You are not bad at interviews. You are just under-practiced.”*
""")

st.markdown('</div>', unsafe_allow_html=True)

# ---------- STRENGTHS & WEAKNESSES ----------
st.markdown('<div class="card">', unsafe_allow_html=True)

st.markdown("### 🧠 Strengths & Improvement Areas")

st.markdown("""
**Strengths**
- Clear understanding of basic concepts  
- Good attempt to explain answers  
- Confidence in responding  

**Areas to Improve**
- Add more real-world examples  
- Improve technical terminology  
- Structure answers clearly  
""")

st.markdown('</div>', unsafe_allow_html=True)

# ---------- QUESTION REVIEW ----------
st.markdown('<div class="card">', unsafe_allow_html=True)

st.markdown("### 📋 Question-wise Review")

for i, q in enumerate(st.session_state.questions, start=1):
    st.markdown(f"**Q{i}.** {q}")
    st.markdown("- Score: _Evaluated by AI_")
    st.markdown("---")

st.markdown('</div>', unsafe_allow_html=True)

# ---------- BUTTON ----------
if st.button("🎯 Go to AI Interview Mentor"):
    st.switch_page("pages/4_AI_Interview_Mentor.py")

    for key in list(st.session_state.keys()):
        del st.session_state[key]
    st.switch_page("app.py")
