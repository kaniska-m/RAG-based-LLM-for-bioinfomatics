
from langchain_huggingface import HuggingFaceEmbeddings

# Instantiate the HuggingFaceEmbeddings using the PubMedBERT model
embeddings = HuggingFaceEmbeddings(model_name="NeuML/pubmedbert-base-embeddings")

# Example embedding query
embed_vec = embeddings.embed_query("Hi How are you?")


# Print the embedding vector and its length to verify
#print(embed_vec)
#print(len(embed_vec))
