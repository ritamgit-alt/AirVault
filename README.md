# 🛡️ AirVault: Personal Memory & Story Engine

A 100% offline, privacy-first AI memory preservation engine built for Hacktoberfest. AirVault takes raw voice memos and turns them into beautifully structured memoir chapters without sending a single byte of data to the cloud.

## 🧠 Tech Stack
- **UI:** Streamlit
- **Audio-to-Text:** OpenAI Whisper (Cached locally)
- **Narrative Engine:** Google Gemma 2 2B (Served locally via Ollama)

## 🚀 Quick Start

1. Ensure [Ollama](https://ollama.com/) is installed and pull the model:
   ```bash
   ollama pull gemma2:2b
