📘 Blog RAG Chat Application — README
A smart Retrieval-Augmented Generation (RAG)–based chat application that allows users to upload blogs, PDFs, text files, or URLs, and ask contextual questions.
The app uses LangChain, FAISS, HuggingFace Embeddings, and OpenAI GPT models to generate accurate answers based entirely on the uploaded content.

🚀 Features

Upload multiple content types:

🌐 Web URL

📄 PDF

📝 Text File

✏️ Manual Text

Intelligent document chunking using Recursive Text Splitter

Semantic search using FAISS Vector Store

Context-aware answers using OpenAI GPT LLM

Clean chat-based UI using Streamlit

End-to-end RAG pipeline with retrieval + generation

Modular code structure (loaders, pipeline, UI, app controller)

🏗️ Tech Stack

Frontend: Streamlit
Backend: Python
AI Framework: LangChain
Embeddings: Sentence Transformers (MiniLM)
Vector Store: FAISS
LLM Provider: OpenAI GPT Models
Document Loaders: WebBaseLoader, PyPDFLoader, TXT Loader
Environment Config: python-dotenv
Testing Tools: Streamlit logs, Postman (optional)

🧠 High-Level Architecture
User
  │
  ▼
Streamlit UI
  │
  ▼
Application Controller
  │
  ▼
Document Loaders (URL/PDF/TXT/Manual)
  │
  ▼
Text Splitter (Chunking)
  │
  ▼
Embeddings Generator (MiniLM)
  │
  ▼
FAISS Vector Store
  │
  ▼
Retriever (Top-K Chunks)
  │
  ▼
LLM (OpenAI GPT Model)
  │
  ▼
RAG Answer Generator
  │
  ▼
Streamlit UI — Final Answer

🧩 Low-Level Design (Modules)
1️⃣ Loaders Module

Handles all input types

load_from_url()

load_from_pdf()

load_from_text_file()

load_from_manual_text()

2️⃣ Vector Store Module

Split documents into chunks

Embed using MiniLM

Store vectors inside FAISS

Return retriever

3️⃣ RAG Pipeline

RetrievalQA

PromptTemplate

OpenAI GPT LLM

Answer generation

4️⃣ UI Module

Chat layout

Message bubbles

Sidebar upload panel

5️⃣ App Controller

Session state

Connecting UI → Pipeline → Output

📂 Project Structure
📦 Blog-RAG-Chat-App
│
├── app.py                # Main Streamlit app
├── pipeline.py           # RAG pipeline (Retrieval + LLM)
├── loaders.py            # URL/PDF/Text loaders
├── ui.py                 # Chat UI components
├── config.py             # API keys & model configs
├── .env                  # OpenAI Key
└── requirements.txt      # Dependencies

⚙️ Installation & Setup
1. Clone the Repository
git clone https://github.com/yourusername/blog-rag-chat.git
cd blog-rag-chat

2. Create Virtual Environment
python -m venv venv
source venv/bin/activate       # Mac/Linux
venv\Scripts\activate          # Windows

3. Install Dependencies
pip install -r requirements.txt

4. Add Your OpenAI Key

Create .env:

OPENAI_API_KEY=your_key_here

5. Run App
streamlit run app.py

📦 Example Usage

Upload a PDF / URL / Text

Ask questions like:

“Summarize this blog”

“What are the key points?”

“Explain section 3 in simple words”

“What does the author say about AI ethics?”

Get contextual answers based only on your document.
🔮 Future Scope

Persistent vector storage using ChromaDB/Pinecone

Multi-file combined knowledge retrieval

Chat history memory

Add authentication + user sessions

Deploy on cloud (Railway / Render / AWS)

Add a React frontend + FastAPI backend version

🤝 Contributing

Pull requests are welcome.
For major changes, please open an issue first to discuss what you'd like to change.

📜 License

This project is licensed under MIT License.

🙌 Acknowledgements

LangChain

Streamlit

HuggingFace

OpenAI