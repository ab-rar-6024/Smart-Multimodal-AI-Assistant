# 🧠 Smart Multimodal AI Assistant

A Transformer-based Multimodal Natural Language Understanding (NLU) system that supports **Text and Voice input**, performs **Intent Detection**, **Named Entity Recognition (NER)**, and **Question Answering**, all within an interactive Streamlit web interface.

This project demonstrates how multiple AI models can be integrated into a single intelligent assistant using HuggingFace Transformers.

---

## 🚀 Features

- 📝 Text-based Natural Language Understanding
- 🎤 Voice Input (Speech-to-Text using Whisper)
- 🏷 Named Entity Recognition (NER)
- 🎯 Intent Detection
- ❓ Extractive Question Answering
- 🖥 Interactive Streamlit Web Interface
- 🔥 Modular and Extendable Architecture

---

## 🧠 AI Models Used

| Task | Model Used |
|------|------------|
| Intent Detection | DistilBERT |
| Named Entity Recognition | dslim/bert-base-NER |
| Question Answering | DistilBERT (SQuAD) |
| Speech Recognition | OpenAI Whisper |
| (Optional Upgrade) Text Generation | FLAN-T5 |

---

## 🏗 System Architecture

User Input (Text / Voice)
↓
Speech Recognition (if voice)
↓
Intent Classification
↓
Entity Extraction (NER)
↓
Question Answering
↓
Response Display


---

## 📂 Project Structure

Smart_Multimodal_AI_Assistant/
│── app.py
│── requirements.txt
│── README.md
│
└── modules/
├── intent.py
├── ner.py
├── qa.py
└── speech.py


---

## ▶ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/Smart-Multimodal-AI-Assistant.git
cd Smart-Multimodal-AI-Assistant
2️⃣ Install Dependencies
pip install -r requirements.txt
3️⃣ Run the Application
streamlit run app.py
Open in browser:

http://localhost:8501
🧪 How to Use
🔹 Text Mode
Select Text from dropdown.

Enter any sentence or question.

Provide context for Question Answering (if needed).

View:

Intent Detection

Extracted Entities

QA Result

🔹 Voice Mode
Select Voice.

Upload a .wav file.

The system converts speech → text.

NLU pipeline runs automatically.

📌 Example Usage
🏷 Named Entity Recognition
Input:

Barack Obama visited India in 2015.
Output:

Barack Obama → PERSON

India → LOCATION

2015 → DATE

❓ Question Answering
Question:

Who visited India?
Context:

Barack Obama visited India in 2015.
Answer:

Barack Obama
🎤 Voice Example
Spoken Input:

Who founded Tesla?
Context:

Tesla was founded by Elon Musk.
Output:

Elon Musk
🌍 Real-World Applications
AI Chatbots

Voice Assistants

Document Analysis Systems

Customer Support Automation

Knowledge Base Assistants

Educational AI Platforms

🎓 Academic Relevance
This project demonstrates:

Transformer-based NLP

Multimodal AI Integration

Speech Recognition

Named Entity Recognition

Extractive Question Answering

End-to-End AI System Architecture

🔮 Future Enhancements
🌐 Wikipedia-based automatic context retrieval

🖼 Image Captioning (True Multimodal)

🎙 Real-time microphone recording

🤖 Conversational memory

📊 Vector database integration (FAISS)

🌍 Deployment on HuggingFace Spaces or Render

👨‍💻 Author
Mohamed Abrar
AI & Full Stack Developer
