import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

class FunctionRegistry:
    def __init__(self):
        # Initialize embedding model
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        
        # Define function metadata
        self.functions = [
            {
                'name': 'open_chrome',
                'description': 'Open Google Chrome browser',
                'category': 'Application Control'
            },
            {
                'name': 'open_calculator',
                'description': 'Open system calculator',
                'category': 'Application Control'
            },
            {
                'name': 'open_notepad',
                'description': 'Open text editor/notepad',
                'category': 'Application Control'
            },
            {
                'name': 'get_system_info',
                'description': 'Retrieve system performance metrics',
                'category': 'System Monitoring'
            },
            {
                'name': 'run_shell_command',
                'description': 'Execute arbitrary shell commands',
                'category': 'Command Execution'
            }
        ]
        
        # Create embeddings for function descriptions
        self.descriptions = [func['description'] for func in self.functions]
        self.embeddings = self.model.encode(self.descriptions)
        
        # Create FAISS index
        dimension = self.embeddings.shape[1]
        self.index = faiss.IndexFlatL2(dimension)
        self.index.add(self.embeddings)

    def retrieve_function(self, query, top_k=1):
        """Retrieve most relevant function based on query"""
        # Convert query to embedding
        query_embedding = self.model.encode([query])
        
        # Search in FAISS index
        D, I = self.index.search(query_embedding, top_k)
        
        # Return top matching functions
        return [self.functions[idx] for idx in I[0]]