from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import PromptTemplate
from langchain.chains import create_retrieval_chain
from langchain_openai import ChatOpenAI
from langchain.chains.combine_documents import create_stuff_documents_chain
from config import OPENAI_API_KEY, EMBED_MODEL, LLM_MODEL


def build_vector_store(docs):
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    split_docs = splitter.split_documents(docs)

    embeddings = HuggingFaceEmbeddings(model_name=EMBED_MODEL)
    store = FAISS.from_documents(split_docs, embeddings)
    return store.as_retriever()

def _safe_extract_text(result):
    if result is None:
        return ""
    if isinstance(result, str):
        return result
    if isinstance(result, (bytes, bytearray)):
        return result.decode("utf-8", errors="ignore")
    if isinstance(result, dict):
        for key in ("answer", "output", "result", "text"):
            if key in result and isinstance(result[key], str):
                return result[key]
    
        for v in result.values():
            if isinstance(v, str):
                return v
    return str(result)

def generate_answer(retriever, question):
    llm = ChatOpenAI(
        model=LLM_MODEL,
        api_key=OPENAI_API_KEY,
        temperature=0.2
    )

    prompt_template = PromptTemplate(
        template="""
You are a helpful assistant. Answer the user based ONLY on the given blog context.

CONTEXT:
{context}

QUESTION:
{input}

Answer in detail:
""",
        input_variables=["context", "input"]
    )

    combine_chain = create_stuff_documents_chain(llm, prompt_template)
    rag_chain = create_retrieval_chain(retriever, combine_chain)

    result = rag_chain.invoke({"input": question})

    answer = _safe_extract_text(result)
    return answer