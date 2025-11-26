import tempfile
import os
from langchain_community.document_loaders import WebBaseLoader, PyPDFLoader
from langchain_core.documents import Document



def load_froms_url(url: str):
    loader = WebBaseLoader(url)
    return loader.load()


def load_from_pdf(pdf_file):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        tmp.write(pdf_file.read())
        tmp_path = tmp.name

    loader = PyPDFLoader(tmp_path)
    data = loader.load()
    os.remove(tmp_path)
    return data


def load_from_text_file(txt_file):
    content = txt_file.read().decode("utf-8")
    return [Document(page_content=content)]


def load_from_manual_text(txt):
    return [Document(page_content=txt)]
