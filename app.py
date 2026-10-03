import streamlit as st
import ollama
import whisper
import tempfile
import os
from PIL import Image

# Page Configuration
st.set_page_config(
    page_title="AirVault - Offline AI Memory Engine",
    page_icon="🛡️",
    layout="wide"
)

# Load Whisper Model locally (Cached)
@st.cache_resource
def load_whisper():
    return whisper.load_model("base")

st.sidebar.image("https://img.shields.io/badge/Status-100%25%20Offline-success?style=for-the-badge", use_container_width=True)
st.sidebar.markdown("### 🛡️ AirVault Security Center")
st.sidebar.info(
    "**Air-Gap Protocol Active**\n\n"
    "- **Model:** Gemma 2 (Local Open-Weight)\n"
    "- **Audio Engine:** Whisper Base (Local)\n"
    "- **Cloud Connections:** 0\n"
    "- **Data Storage:** Local RAM / Disk"
)

st.title("🛡️ AirVault: Personal Memory & Story Engine")
st.caption("A 100% offline, privacy-first AI box built for preserving personal histories without cloud exposure.")

tab1, tab2, tab3 = st.tabs(["🎙️ Voice Memoir Studio", "🖼️ Photo Memory Unlocker", "🔒 Privacy Architecture"])

# --- TAB 1: VOICE MEMOIR STUDIO ---
with tab1:
    st.header("Record or Upload a Voice Memory")
    st.markdown("Speak naturally about an old memory, a recipe, or a family event. Local AI will clean up raw speech into a written memoir chapter.")
    
    audio_file = st.file_uploader("Upload an audio recording (.mp3, .wav, .m4a)", type=["mp3", "wav", "m4a"])
    
    if audio_file is not None:
        st.audio(audio_file)
        if st.button("Process Memory Offline"):
            with st.spinner("Transcribing audio locally with Whisper..."):
                # Save to temporary file for Whisper processing
                with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
                    tmp.write(audio_file.read())
                    tmp_path = tmp.name
                
                model = load_whisper()
                result = model.transcribe(tmp_path)
                raw_text = result["text"]
                os.remove(tmp_path)
            
            st.subheader("Raw Local Transcription:")
            st.write(f'"{raw_text}"')
            
            with st.spinner("Structuring story with Gemma 2 open-weight model..."):
                prompt = f"""
                You are a compassionate family biographer. Take the following raw spoken transcript from an elderly loved one or friend and transform it into a beautifully written, warm memoir chapter. Fix stutters and filler words, but retain their original voice and narrative emotion.

                Raw Transcript:
                {raw_text}
                """
                
                response = ollama.chat(model='gemma2:2b', messages=[
                    {'role': 'user', 'content': prompt}
                ])
                
                st.subheader("📖 Formatted Memoir Chapter:")
                st.markdown(response['message']['content'])
                st.download_button("Save Chapter (.md)", response['message']['content'], file_name="memoir_chapter.md")

# --- TAB 2: PHOTO MEMORY UNLOCKER ---
with tab2:
    st.header("Unlock Memories from Photos")
    st.markdown("Upload a vintage or family photo. The local AI will ask evocative questions to help your loved one recall forgotten details.")
    
    uploaded_img = st.file_uploader("Upload a photo (.jpg, .png)", type=["jpg", "png", "jpeg"])
    photo_context = st.text_input("Optional context (e.g., 'Grandpa in 1974 at the lake'):")
    
    if uploaded_img is not None:
        image = Image.open(uploaded_img)
        st.image(image, caption="Uploaded Memory Photo", width=400)
        
        if st.button("Generate Guided Memory Prompts"):
            with st.spinner("Analyzing context with Gemma 2..."):
                prompt = f"""
                You are helping a friend/loved one recall details about an old photograph contextually labeled: '{photo_context}'.
                Generate 4 gentle, evocative, and specific memory-prompting questions to ask them while looking at this photo.
                Focus on sensory details (sounds, smells, feelings) and personal relationships.
                """
                response = ollama.chat(model='gemma2:2b', messages=[
                    {'role': 'user', 'content': prompt}
                ])
                
                st.subheader("💡 Memory Prompts to Ask Your Loved One:")
                st.markdown(response['message']['content'])

# --- TAB 3: PRIVACY ARCHITECTURE ---
with tab3:
    st.header("Why Open-Source AI is Mandatory Here")
    st.markdown("""
    | Feature | AirVault (Open-Source AI) | Cloud AI (ChatGPT / Claude) |
    | :--- | :--- | :--- |
    | **Data Privacy** | **100% Private** (Data stays on device) | Data sent to corporate servers |
    | **Internet Required?** | **No** (Runs air-gapped on a mountain) | Yes (Fails without Wi-Fi) |
    | **Cost** | **$0.00 Forever** | Monthly subscriptions / API fees |
    | **Control** | Full model choice (**Gemma 2**) | Subject to model changes / deprecation |
    """)