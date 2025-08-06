import streamlit as st # for the UI
from ollama_client import generate_response
from rag_pipeline import add_pdf_to_db, query_db
from pypdf import PdfReader # for reading pdfs
import os #For os operations

st.title("RAG Project - PDFs")

uploaded_files = st.file_uploader("Upload PDF files", type="pdf", accept_multiple_files=True) # for uploading pdfs



if st.button("Process PDFs"): # for processing the pdfs
    # Process uploaded files
    if uploaded_files:
        for uploaded_file in uploaded_files: # for each uploaded file
            try:
                add_pdf_to_db(uploaded_file) # for adding the pdf to the database
                st.success(f"Processed uploaded file: {uploaded_file.name}") # for success message
            except Exception as e:
                st.error(f"Error processing uploaded file {uploaded_file.name}: {e}") # for error message

query = st.text_input("Enter your question:") #User input

top_chunks = st.number_input("How many relevant chunks should be retrieved (top_k)?", value=5) # for the top_k - More chunks = More context = More accurate answer - however, the more the chunks, the more the time it takes to retrieve the answer

if st.button("Ask"): #if the user clicks the button
    context = query_db(query, top_k=top_chunks) # for the context
    prompt = f"Answer the following question based on the following context: {context}\n\nQuestion: {query}\n\nAnswer: " # for the prompt
    response = generate_response(prompt) # for the response
    st.markdown("### Answer")
    st.write(response)








