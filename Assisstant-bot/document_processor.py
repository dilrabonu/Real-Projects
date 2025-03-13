import os
from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
import faiss

class DocumentProcessor:
    def __init__(self, data_dir="data"):
        self.data_dir = data_dir
        self.documents = []
        self.embeddings = OpenAIEmbeddings()
        self.vectorstore = None

    def load_documents(self):
        """Load all documents from the data directory"""
        for filename in os.listdir(self.data_dir):
            file_path = os.path.join(self.data_dir, filename)
            
            if filename.endswith('.pdf'):
                loader = PyPDFLoader(file_path)
                pages = loader.load()
                
                for page in pages:
                    page.metadata['source'] = filename
                    page.metadata['page_number'] = page.metadata.get('page', 0) + 1
                
                self.documents.extend(pages)
                print(f"Loaded PDF: {filename} with {len(pages)} pages")
            
            elif filename.endswith('.txt'):
                loader = TextLoader(file_path)
                documents = loader.load()
                for doc in documents:
                    doc.metadata['source'] = filename
                self.documents.extend(documents)
                print(f"Loaded text file: {filename}")
        
        print(f"Total documents loaded: {len(self.documents)}")
        return self.documents

    def create_embeddings(self):
        """Split documents and create embeddings"""
        if not self.documents:
            print("No documents loaded. Call load_documents() first.")
            return None
        
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200,
        )
        
        splits = text_splitter.split_documents(self.documents)
        print(f"Split into {len(splits)} chunks for embeddings")

        # Initialize FAISS index
        index = faiss.IndexFlatL2(1536)  # 1536-d for OpenAI embeddings
        
        # Create vector store
        self.vectorstore = FAISS.from_documents(splits, self.embeddings)
        
        # Save the vector store for later use
        self.vectorstore.save_local("faiss_index")
        print("Vector store saved to disk")
        
        return self.vectorstore

    def search_documents(self, query, k=3):
        """Search documents for relevant information"""
        if not self.vectorstore:
            try:
                self.vectorstore = FAISS.load_local("faiss_index", self.embeddings, allow_dangerous_deserialization=True)
                print("Loaded vector store from disk")
            except:
                print("No vector store found. Create embeddings first.")
                return []
        
        results = self.vectorstore.similarity_search_with_relevance_scores(query, k=k)
        return results
