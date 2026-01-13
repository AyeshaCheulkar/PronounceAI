🎙️ PronounceAI

**PronounceAI** is an **NLP-based pronunciation evaluation system** that analyzes a user’s spoken word and provides **phoneme-level pronunciation accuracy and feedback** using speech and language processing techniques.

📌 Problem Statement

Learners often struggle to know whether they are pronouncing English words correctly.
Traditional systems either rely on spelling comparison or require human feedback, which is not scalable.

This project aims to **automatically evaluate pronunciation accuracy** using **Natural Language Processing (NLP)** techniques.

🎯 Objectives

* Convert user speech into text
* Analyze pronunciation at the **phoneme (sound) level**
* Compare spoken pronunciation with correct pronunciation
* Provide an **accuracy score and corrective feedback**
* Offer a simple and interactive web interface
🧠 Technologies & Concepts Used

🔹 NLP Concepts

* Speech-to-Text (Automatic Speech Recognition)
* Grapheme-to-Phoneme (G2P) Conversion
* Phoneme sequence comparison
* Linguistic similarity analysis

🔹 Tools & Libraries

* **Whisper** – Speech-to-text (ASR)
* **g2p_en** – Grapheme-to-phoneme conversion
* **CMU Pronouncing Dictionary** – Phoneme reference
* **difflib / Levenshtein** – Sequence similarity
* **gTTS** – Native pronunciation audio (Text-to-Speech)
* **Streamlit** – Web application framework
* **Git & GitHub** – Version control and collaboration
🏗️ System Architecture

User Speech
     ↓
Speech-to-Text (Whisper)
     ↓
Text Normalization
     ↓
Grapheme-to-Phoneme Conversion
     ↓
Phoneme Sequence Comparison
     ↓
Accuracy Score + Feedback
     ↓
Streamlit Web Interface
```
🔄 How the System Works

1. User enters a **target word**
2. User records their pronunciation using a microphone
3. Whisper converts speech into text
4. Both target word and spoken word are converted into **phonemes**
5. Phoneme sequences are compared using similarity matching
6. A pronunciation score is generated
7. Visual phonetic feedback is displayed to the user
8. Native pronunciation audio can be played for reference

🖥️ Features

* 🎤 Real-time voice recording
* 🔊 Native pronunciation playback
* 📊 Pronunciation accuracy score
* 🔤 Phoneme-level analysis
* 🎨 Clean and interactive UI
* 🌐 Works locally without external pronunciation databases

▶️ How to Run the Project

 1️⃣ Clone the repository

```bash
git clone https://github.com/AyeshaCheulkar/PronounceAI.git
cd PronounceAI
```

 2️⃣ Create and activate virtual environment

```bash
python -m venv venv
venv\Scripts\activate
```

 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

 4️⃣ Download NLTK resources

```python
import nltk
nltk.download('averaged_perceptron_tagger_eng')
nltk.download('cmudict')
```

 5️⃣ Run the application

```bash
streamlit run app.py
```

Open in browser:

```
http://localhost:8501
```
⚠️ Limitations

* Pronunciation accuracy depends on speech recognition quality
* Background noise may affect results
* Best suited for **single-word pronunciation**
* Accent variations may slightly impact scoring

🚀 Future Enhancements

* Syllable-level error detection
* Accent-aware pronunciation scoring
* Sentence-level pronunciation analysis
* User performance tracking
* Deployment on cloud platforms

👩‍💻 Contributors

* **Ayesha Cheulkar** – Project Owner

📚 Conclusion

PronounceAI demonstrates how **Natural Language Processing techniques** can be applied to **spoken language analysis**.
By focusing on phoneme-level comparison, the system provides meaningful pronunciation feedback in an automated and scalable manner.

