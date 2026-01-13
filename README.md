# AI Newspaper Voice Assistant + Trend Analyzer

A complete AI-powered application that reads the news to you, summarizes articles, and analyzes trending topics.

## 🚀 Features
- **News Fetcher**: Scrapes latest news from RSS feeds (BBC, CNN, Google News).
- **AI Summarization**: Uses HuggingFace Transformers (BART/T5) to summarize articles.
- **Voice Assistant**: Converts summaries to audio using gTTS.
- **Topic Analytics**: Visualizes the most frequent news topics.
- **Trend Prediction**: Predicts future trending categories using simple ML.

## 📂 Project Structure
```
ai-newspaper-voice-assistant/
├── backend/            # FastAPI Backend
├── frontend/           # Streamlit Frontend
├── data/               # Local data storage
├── notebooks/          # Jupyter Notebooks for experiments
└── requirements.txt    # Parameters
```

## 🛠️ Installation

1. **Clone the repository** (or use the created folder).
2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## 🏃‍♂️ How to Run

### Step 1: Generate Dummy Models (First Run Only)
Before running the backend, create the dummy ML models:
```bash
python backend/models/generate_dummy_models.py
```

### Step 2: Start the Backend (FastAPI)
Run the following command from the root directory:
```bash
uvicorn backend.main:app --reload
```
The API will be available at `http://localhost:8000`.

### Step 3: Start the Frontend (Streamlit)
Open a new terminal and run:
```bash
streamlit run frontend/app.py
```
The UI will open in your browser at `http://localhost:8501`.

## 🧪 Testing the App
1. Go to the **Home** page and click "Read Today's News".
2. Wait for the AI to fetch and summarize articles.
3. Click "▶️ Play" to hear the audio summary.
4. Go to **Analytics** to see the topic distribution.
5. Go to **Trend Prediction** to see future predictions.

## 🤖 Models Used
- **Summarization**: `sshleifer/distilbart-cnn-12-6`
- **TTS**: `gTTS` (Google Text-to-Speech)
- **Classification**: Logistic Regression (Bag of Words)
- **Trend Prediction**: Linear Regression
