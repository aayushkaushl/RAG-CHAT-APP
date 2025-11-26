import streamlit as st
from loaders import load_froms_url, load_from_pdf, load_from_text_file, load_from_manual_text
from pipeline import build_vector_store, generate_answer
from ui import chat_box, chat_header

st.set_page_config(page_title="Blog RAG Chat", layout="wide")
chat_header()


if "messages" not in st.session_state:
    st.session_state.messages = []

if "retriever" not in st.session_state:
    st.session_state.retriever = None


st.sidebar.title(" Upload Document")

option = st.sidebar.selectbox("Choose input type", ["Web URL", "PDF File", "Text File", "Manual Text"])

data = None

if option == "Web URL":
    url = st.sidebar.text_input("Enter URL")
    if st.sidebar.button("Load"):
        data = load_froms_url(url)

elif option == "PDF File":
    file = st.sidebar.file_uploader("Upload PDF", type=["pdf"])
    if file and st.sidebar.button("Load"):
        data = load_from_pdf(file)

elif option == "Text File":
    text_file = st.sidebar.file_uploader("Upload text file", type=["txt"])
    if text_file and st.sidebar.button("Load"):
        data = load_from_text_file(text_file)

elif option == "Manual Text":
    txt = st.sidebar.text_area("Paste text manually")
    if st.sidebar.button("Load"):
        data = load_from_manual_text(txt)



if data:
    with st.spinner("Building vector store..."):
        retriever = build_vector_store(data)
        st.session_state.retriever = retriever
        st.sidebar.success("Document Loaded Successfully!")



question = st.chat_input("Ask a question from the blog...")

if question:
    retriever = st.session_state.retriever
    if not retriever:
        st.error(" Load a document first!")
    else:
      
        st.session_state.messages.append({"role": "user", "text": question})
        chat_box(question, "user")

        with st.spinner("Thinking..."):
            answer = generate_answer(retriever, question)

        st.session_state.messages.append({"role": "assistant", "text": answer})
        chat_box(answer, "assistant")



for msg in st.session_state.messages:
    chat_box(msg["text"], msg["role"])
