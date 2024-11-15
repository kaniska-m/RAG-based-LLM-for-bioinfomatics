from langchain_pinecone import PineconeVectorStore
from pinecone.grpc import PineconeGRPC as Pinecone
from pinecone import ServerlessSpec

from chunker import docs 
from embedder import embeddings
import os 

PINECONE_API_KEY= "pcsk_2KThR5_6Tf82WL1JD2AQnd3HGWRQZtjZEnK1JNMb4pQY1M8HrX1Rj1RbKvffuUDJHiFwUz"

os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY


index_name = "bio-index"


pc = Pinecone(api_key=PINECONE_API_KEY)



from chunker import docs 
from embedder import embeddings


docsearch = PineconeVectorStore.from_documents(docs, embeddings, index_name=index_name)

r_docs = docsearch.similarity_search(query="What are the aims of bioinformatics?",k=2)

print(len(r_docs))
#for doc in docs:
#    print(doc.page_content)
