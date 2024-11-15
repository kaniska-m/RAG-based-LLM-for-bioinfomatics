from typing import List

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter



class PDFChunker:
    def __init__(self,pdf_path, chunk_size=120, chunk_overlap=30) -> None:
        self.pages = PyPDFLoader(pdf_path).load_and_split()
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap

        self.text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=chunk_size, chunk_overlap=chunk_overlap
)

    def chunk(self) -> List:

        return  self.text_splitter.split_documents(self.pages)


chunker = PDFChunker("biobook.pdf")
docs = chunker.chunk()


print(len(chunker.chunk()))
