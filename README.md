<p align="center">
  <img src="https://user-images.githubusercontent.com/74038190/212750147-854a394f-fee9-4080-9770-78a4b7ece53f.gif" alt="Real Estate Assistant Banner" />
</p>


# 🏠 Real Estate News Assistant using Retrieval-Augmented Generation (RAG)

A **GenAI-powered assistant** that extracts insights from **real estate news articles** using **Retrieval-Augmented Generation**. It lets users input URLs of real estate articles, processes them with embeddings and vector search, and provides **precise, source-cited answers** to user questions.

Built with ⚙️ **Streamlit**, 🧠 **LangChain**, 🗃️ **ChromaDB**, 🚀 **Groq (LLaMA 3)**, and 📐 **Alibaba GTE Embeddings**.

---

## 🚀 Features

- 🔗 Input up to **3 news article URLs**
- 🧾 **Smart Web Scraping**: Supports structured & dynamic websites with `SeleniumURLLoader`
- 🧠 **RAG Pipeline**:
  - Recursive text splitting via `RecursiveCharacterTextSplitter`
  - Semantic embeddings via `gte-base-en-v1.5`
  - Vector search using **ChromaDB**
  - LLM-powered answers using **LLaMA-3-70B-Versatile** (hosted on Groq)
- 🖥️ **Streamlit App**:
  - Clean sidebar for input
  - Answer area with source references

---

## 🧩 Tech Stack

| Component       | Tool / Service                               |
| --------------- | -------------------------------------------- |
| Frontend        | [Streamlit](https://streamlit.io)            |
| Framework       | [LangChain](https://www.langchain.com)       |
| Embeddings      | Alibaba GTE (`gte-base-en-v1.5`)             |
| LLM             | [Groq](https://groq.com) (LLaMA-3-70B)       |
| Vector Store    | [ChromaDB](https://www.trychroma.com)        |
| Loaders         | `SeleniumURLLoader`, `UnstructuredURLLoader` |

---

## 📁 Project Structure

real-estate-news-assistant/
├── main.py # Streamlit UI
├── rag.py # RAG pipeline: load, embed, answer
├── requirements.txt # All Python dependencies
├── .env # API keys (not committed)
├── assets/
│ └── banner.png # Project banner
└── README.md # This file

---

## ⚙️ Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/sidhartthhhhh/Real-Estate.git
cd Real-Estate
```

### Create a Virtual Environment (recommended)
```bash
python -m venv venv
venv\Scripts\activate     # Windows
# Or
source venv/bin/activate  # macOS/Linux

```
Install Requirements
```bash

pip install -r requirements.txt
```

### Set Environment Variables
Create a .env file:

GROQ_API_KEY=your_groq_api_key

 Run the App
```bash

streamlit run main.py
```
💬 Example Questions
After entering article URLs and clicking "Retrieve Details", ask:

“What is the 30-year fixed mortgage rate and its date?”

“What did the Fed announce in December 2024?”

“What’s the expected trend in home prices?”

✅ Notes
Ensure URLs point to real estate news with accessible HTML (Selenium handles most JavaScript sites).

Results include source citations.

Built with a focus on performance, clarity, and low-latency LLM responses using Groq.

🧑‍💻 Author
Made with ❤️ by Sidharth Singh

If you like this project, consider ⭐ starring the repo or sharing it with others!
