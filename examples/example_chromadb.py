import os
import sys

project_root = os.path.dirname(os.path.dirname(__file__))
sys.path.append(project_root)

from api.chroma_db import initialize_chroma_db, connect_to_existing_collection, ChromaDBManager


manager = initialize_chroma_db()

# Adding items to the collection
documents = ["Richard is 3 years old",
             "Macbook is the best selling laptop",
             "Aura is most likely to be a cat",
             "The Juan valdez morning coffee is the one Krank loves ",
             "Arnold Triumph is an old guy with 89 years",
             "Arnold Triumph loves going to the zoo",
             "The Ra cat is waiting for Ela to be adopted"]
ids = ["1", "2", "3", "4", "5", "6", "7"]
manager.add_to_collection(documents, ids)

query_texts = ["What's the name of the cat that Ela will adopt?"]
n_results = 2
results = manager.retrieve_collections(query_texts, n_results)

print(results)

