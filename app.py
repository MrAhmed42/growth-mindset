import streamlit as st
import random

# Motivational Quotes
quotes = [
    "Growth and comfort do not coexist.",
    "Your only limit is your mind.",
    "Mistakes are proof that you are trying.",
    "Hardships often prepare ordinary people for an extraordinary destiny."
]

# Growth Mindset Challenges
challenges = [
    "Write down 3 things you're grateful for today.",
    "Try something new and reflect on your experience.",
    "Encourage someone today.",
    "Learn a new skill or fact outside your comfort zone."
]

# Streamlit UI
st.title("🚀 Growth Mindset Daily Challenge")

# Display Challenge
st.subheader("🌱 Your Challenge for Today:")
st.info(random.choice(challenges))

# Display Motivational Quote
st.subheader("💡 Motivational Quote:")
st.success(random.choice(quotes))

# Track Progress
st.subheader("📊 Track Your Progress")
progress = st.slider("How much did you complete today's challenge?", 0, 100, 0)
if progress > 0:
    st.success(f"Great job! You're {progress}% closer to a growth mindset! 🚀")
else:
    st.warning("Start now! Small steps lead to big changes.")

st.write("✨ Keep growing and challenging yourself every day! ✨")
