import streamlit as st
from streamlit_mic_recorder import mic_recorder
from streamlit_lottie import st_lottie
import requests
from gtts import gTTS
import io
import os

from stt import transcribe_audio
from engine import calculate_pronunciation_score

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="PronounceAI", page_icon="🎙️", layout="wide")

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>
.main {
    background-color: #f8f9fa;
}

.analysis-card {
    background: #ffffff;
    padding: 24px;
    border-radius: 18px;
    border-left: 6px solid #2563eb;
    box-shadow: 0 10px 25px rgba(0,0,0,0.08);
    margin-top: 15px;
}

.label {
    color: #475569;
    font-size: 14px;
    font-weight: 600;
}

.heard-text {
    color: #2563eb;
    font-weight: 600;
    margin-bottom: 10px;
}

.phoneme-box {
    background: #0f172a;
    color: #22c55e;
    padding: 12px;
    border-radius: 10px;
    font-family: monospace;
    font-size: 15px;
    margin-bottom: 10px;
}

.phoneme-box.user {
    color: #60a5fa;
}
</style>
""", unsafe_allow_html=True)

# ---------------- LOTTIE LOADER ----------------
def load_lottie(url):
    try:
        r = requests.get(url, timeout=5)
        if r.status_code == 200:
            return r.json()
    except:
        pass
    return None

lottie_mic = load_lottie("https://assets5.lottiefiles.com/packages/lf20_6p8bfmnd.json")
lottie_success = load_lottie("https://assets10.lottiefiles.com/packages/lf20_vl9o6syf.json")

# ---------------- SIDEBAR ----------------
with st.sidebar:
    if lottie_mic:
        st_lottie(lottie_mic, height=140)
    else:
        st.info("🎙️ Microphone Ready")

    st.title("Settings")
    target_word = st.text_input("🎯 Target Word", "Phenomenal").strip()

    st.markdown("---")

    st.write("### 🔊 Listen to Native")
    if st.button("Play Sound"):
        tts = gTTS(text=target_word, lang="en")
        audio_fp = io.BytesIO()
        tts.write_to_fp(audio_fp)
        st.audio(audio_fp, format="audio/mp3")

    st.info("Tip: Focus on vowel clarity and word stress.")

# ---------------- MAIN UI ----------------
st.title("🗣️ PronounceAI")
st.caption("Real-time Phonetic Feedback Engine")

col1, col2 = st.columns([1, 1.2], gap="large")

# ---------------- RECORD ----------------
with col1:
    st.subheader("Step 1: Record")
    st.write("Press the button and pronounce the word clearly.")

    audio = mic_recorder(
        start_prompt="Start Speaking 🎙️",
        stop_prompt="Stop ⏹️",
        key="recorder"
    )

# ---------------- PROCESS ----------------
if audio:
    with open("temp.wav", "wb") as f:
        f.write(audio["bytes"])

    with st.spinner("Analyzing pronunciation..."):
        user_text = transcribe_audio("temp.wav")
        score, target_p, user_p, feedback = calculate_pronunciation_score(
            target_word, user_text
        )

    with col2:
        st.subheader("Step 2: Results")

        if score >= 80:
            st.success(f"Amazing! Score: {score}%")
            if lottie_success:
                st_lottie(lottie_success, height=90)
            st.balloons()
        elif score >= 50:
            st.warning(f"Good effort! Score: {score}%")
        else:
            st.error(f"Needs improvement. Score: {score}%")

        st.progress(score / 100)

        # -------- PHONETIC ANALYSIS (NO INDENTATION!) --------
        st.markdown(
f"""
<div class="analysis-card">
<h3>🔤 Phonetic Analysis</h3>

<p class="label">What I heard:</p>
<p class="heard-text">{user_text if user_text else "—"}</p>

<hr>

<p class="label">Target Sounds</p>
<div class="phoneme-box">
{' '.join(target_p)}
</div>

<p class="label">Your Sounds</p>
<div class="phoneme-box user">
{' '.join(user_p)}
</div>
</div>
""",
unsafe_allow_html=True
        )

        st.write("### 🔍 Correction Guide")
        st.info(feedback if feedback else "Good pronunciation overall!")

    if os.path.exists("temp.wav"):
        os.remove("temp.wav")

# ---------------- EMPTY STATE ----------------
else:
    with col2:
        st.image(
            "https://cdn-icons-png.flaticon.com/512/3293/3293603.png",
            width=100
        )
        st.write("Your analysis will appear here after you record.")
