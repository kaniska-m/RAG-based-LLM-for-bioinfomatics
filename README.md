# RAG-based Language Model for Bioinformatics

This project implements a **Retrieval-Augmented Generation (RAG)** model designed to answer bioinformatics questions with high accuracy and contextual relevance. The model integrates a **vector database** for efficient information retrieval with a **large language model (LLM)** to provide precise, generative responses.

---

## Features

- **Document Chunking**: Breaks large documents into smaller, manageable chunks for effective processing.
- **Semantic Embeddings**: Generates vector representations of text using a bioinformatics-tuned model (`PubMedBERT`).
- **Vector Database Storage**: Stores embeddings in Pinecone for fast similarity-based retrieval.
- **Contextual Answer Generation**: Uses an LLM to generate answers based on retrieved context from the vector database.

---

## Repository Structure

```plaintext
.
├── chunker.py                # Splits PDF documents into text chunks.
├── embedder.py               # Generates embeddings using PubMedBERT.
├── multi_turn_chatbot.py     # Handles multi-turn conversation.
├── requirements.txt          # Lists all dependencies.
├── single_turn_chatbot.py    # Chatbot for single-question interactions.
└── vdbb.py                   # Manages vector database storage and retrieval.
```

## Setup Instructions
Prerequisites
Python 3.8 or higher
API keys for Pinecone and the LLM service provider (e.g., OpenAI, Groq)
Installation
