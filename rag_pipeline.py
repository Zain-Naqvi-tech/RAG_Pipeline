import chromadb # for vector database
from chromadb.utils import embedding_functions # for embedding
from pypdf import PdfReader # for pdf reading

chroma_client = chromadb.Client() # create a chroma client which is a vector database

collection = chroma_client.create_collection(name="docs") # create a collection of docs

# create an embedding function
embedding_function = embedding_functions.SentenceTransformerEmbeddingFunction(model_name="all-MiniLM-L6-v2") 

def add_text_to_db(doc_name, text): 
    embedding = embedding_function([text]) # create an embedding for the text
    collection.add(documents=[text], ids=[doc_name], embeddings=[embedding[0].tolist()]) # add the text to the collection

def add_pdf_to_db(pdf_path): # add a pdf to the collection
    reader = PdfReader(pdf_path) # read the pdf
    # Chunking: Add each page as a separate document to the collection for better retrieval and faster queries
    for i, page in enumerate(reader.pages): # iterate through the pages - enumerate is used to get the index of the page
        text = page.extract_text() # extract the text from the page
        if text: # only non-empty pages
            chunk_id = f"{pdf_path}_page_{i+1}" # unique id for each chunk
            add_text_to_db(chunk_id, text) # add the chunk to the collection

def query_db(query, top_k): 
    query_embedding = embedding_function([query]) # create an embedding for the query
    #Convert the numpy array to a list of floats - something required by ChromaDB
    result = collection.query(query_embeddings=[query_embedding[0].tolist()], n_results=top_k) # query the collection


    # This function queries the vector database collection for the most relevant documents based on the input query.
    # The following line sends the query to the collection (vector database),
    # using the provided query string. It requests the top 'top_k' most relevant results.
    # 'collection.query' is assumed to be a method that performs a similarity search
    # over the documents stored in the collection, returning the closest matches.
    # The result is expected to be a dictionary with a 'documents' key,
    # which contains a list of lists (each sublist contains documents for each query).
    # Here, we return only the first set of documents (for the first query),
    return result['documents'][0] # return the result





 