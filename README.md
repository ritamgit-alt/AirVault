# 🛡️ AirVault: Personal Memory & Story Engine

A 100% offline, privacy-first AI memory preservation engine built for the DEV Hacktoberfest challenge. AirVault takes raw voice memos and turns them into beautifully structured memoir chapters without sending a single byte of data to the cloud.

## 🧠 Tech Stack
- UI: Streamlit
- Audio-to-Text: OpenAI Whisper (Base model, cached locally)
- Narrative Engine: Google Gemma 2 2B (Served locally via Ollama)
- Hardware: Optimized for bare-metal local execution (tested on Apple Silicon M-series)

## 🚀 Quick Start

1. Ensure Ollama is installed and pull the required model by running `ollama pull gemma2:2b` in your terminal.
2. Clone the repository and install dependencies using `pip install -r requirements.txt`.
3. Start the local Ollama background server by running `ollama serve`.
4. In a separate terminal tab, launch the Streamlit app using `streamlit run app.py`.

## 📄 License
Distributed under the MIT License. See `LICENSE` for more information.
