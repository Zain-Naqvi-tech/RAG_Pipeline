# RAG (Retrieval-Augmented Generation) PDF Question Answering System

A Streamlit-based web application that implements a RAG pipeline for answering questions about PDF documents using a local Ollama LLM server.

## Features

- PDF Upload & Processing: Upload multiple PDF files through an intuitive web interface
- Vector Database Storage: Automatically process and store PDF content in ChromaDB
- Intelligent Q&A: Ask questions about uploaded documents and get AI-generated answers
- Configurable Retrieval: Adjust the number of relevant chunks retrieved for better accuracy
- Local LLM Integration: Uses Ollama with Llama2 model for privacy and offline operation

## Architecture

### Frontend
- Streamlit - Clean, interactive web interface
- File upload functionality for PDFs
- Text input for questions
- Configurable retrieval parameters

### Backend Components

1. PDF Processing (`rag_pipeline.py`):
   - PDF text extraction using PyPDF
   - Page-based chunking strategy
   - SentenceTransformer embeddings (`all-MiniLM-L6-v2`)
   - ChromaDB vector database storage

2. LLM Integration (`ollama_client.py`):
   - Local Ollama server connection 
   - Llama2 model integration
   - Streaming response handling
   - Context-aware prompt formatting

3. Main Application (`main.py`):
   - Workflow orchestration
   - User interaction management
   - Error handling and display

## Prerequisites

- Python 3.8+
- Ollama installed and running locally
- Llama2 model downloaded in Ollama

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Zain-Naqvi-tech/rag_ollama.git
   cd rag_ollama
   ```

2. Create and activate virtual environment:
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install streamlit chromadb sentence-transformers pypdf requests
   ```

## Usage

1. Start the application:
   ```bash
   streamlit run main.py
   ```

2. Open your browser and navigate to `http://localhost:8501`

3. Upload PDF files using the file uploader

4. Process PDFs by clicking the "Process PDFs" button

5. Ask questions by entering your query and clicking "Ask"

6. Adjust retrieval settings by modifying the "top_k" parameter (more chunks = more context but slower response)

## Configuration

### Model Configuration
- LLM Model: Llama2 (configurable in `ollama_client.py`)
- Embedding Model: all-MiniLM-L6-v2 (configurable in `rag_pipeline.py`)
- Vector Database: ChromaDB (in-memory)

### Performance Tuning
- Chunking Strategy: Page-based (can be modified for different strategies)
- Retrieval: Configurable top_k parameter for context retrieval
- Streaming: Enabled for real-time response generation

