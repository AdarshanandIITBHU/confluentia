# Transcript Analyzer App

A modern, LLM-powered application to analyze call or meeting transcripts in plain `.txt` format. Users can upload multiple transcripts, ask natural language questions, and generate insightful charts and summaries instantly.

---

## 🚀 Technologies Used

- **Frontend/UI:** Streamlit (Python)
- **Chart/Graph Generation:** Python `matplotlib` + `pandas`
- **Presentation Decks:** [Gamma](https://gamma.app/) (AI-powered slide generation, for summary decks)
- **Other Libraries:** `python-dotenv`, `requests`, standard Python libraries

---

## ✨ Features

- Upload one or more `.txt` transcript files (from calls, meetings, or interviews)
- Ask rich questions or request analytics in plain English (e.g., “Summarize customer feedback”, “Chart number of calls mentioning objections”, etc.)
- LLM-based answers and summaries powered by OpenAI GPT-4o-mini
- Automatic chart and graph generation based on transcript data
- Modern Streamlit interface for easy interaction

---

## 💡 How It Works

1. **User uploads text transcripts.**
2. **All user queries are routed and interpreted using Gemini agent logic.**
3. **Q&A or chart intents are dispatched to OpenAI GPT-4o-mini, which processes the transcript(s) and returns accurate answers or Python code for chart plotting.**
4. **Charts are generated on the fly using matplotlib, and answers are displayed in a clean UI.**
5. **For deck creation, output can be exported to Gamma for slick, shareable presentations.**

---

## 🏃‍♂️ Getting Started

1. **Clone the repo locally.**
2. **Create a `.env` file in your project and add your OpenAI API key:**
    ```
    OPENAI_API_KEY=sk-...your-key...
    ```
3. **Install dependencies:**
    ```
    pip install -r requirements.txt
    ```
4. **Activate your Python virtual environment if used:**
    ```
    # Windows
    .\venv\Scripts\activate
    # Mac/Linux
    source venv/bin/activate
    ```
5. **Run the app:**
    ```
    streamlit run demo.py
    ```
6. **Upload your .txt transcript(s), type a question or analysis instruction, and get instant insights!**

---

## 🌟 Example Prompts

- *Summarize the main customer objections in all calls.*
- *Chart sales performance by agent across transcripts.*
- *What is the overall sentiment of callers in these meetings?*


## 📒 Credits & Acknowledgments

- Agent decision logic inspired by [Gemini](https://deepmind.google/technologies/gemini/).
- LLM question-answering and analytics: [OpenAI GPT-4o-mini](https://openai.com).
- Deck/slide output: [Gamma](https://gamma.app/)
- Interface: [Streamlit](https://streamlit.io/)
- Data/plotting: matplotlib, pandas

---

## 🛡️ License

MIT License. See LICENSE file.

---

*Built by [Adarsh_Anand], 2025.*
