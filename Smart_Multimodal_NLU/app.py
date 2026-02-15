import streamlit as st
from modules.intent import detect_intent
from modules.ner import extract_entities
from modules.qa import answer_question
from modules.speech import speech_to_text

st.title("🧠 Smart Multimodal NLU Assistant")

mode = st.selectbox("Select Input Mode", ["Text", "Voice"])

if mode == "Text":
    user_input = st.text_area("Enter your text")

elif mode == "Voice":
    audio_file = st.file_uploader("Upload audio file (.wav)")
    if audio_file:
        with open("temp.wav", "wb") as f:
            f.write(audio_file.read())
        user_input = speech_to_text("temp.wav")
        st.write("Recognized Text:", user_input)

if 'user_input' in locals() and user_input:

    st.subheader("Intent Detection")
    intent = detect_intent(user_input)
    st.write(intent)

    st.subheader("Entity Extraction")
    entities = extract_entities(user_input)
    st.write(entities)

    st.subheader("Question Answering")
    context = st.text_area("Enter context for QA")
    if context:
        answer = answer_question(user_input, context)
        st.write("Answer:", answer)
