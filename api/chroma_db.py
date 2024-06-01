import chromadb


class ChromaDBManager:
    """
    A manager for interacting with the Chroma database.
    This class provides methods to create, add to, retrieve from, check existence,
    delete, and connect to collections within a Chroma database.
    """
    def __init__(self):
        self.chroma_client = chromadb.Client()
        self.collection_name = None
        self.collection = None

    def create_collection(self, name):
        """
        Create a new collection in the Chroma database.
        This method sets the collection name and creates a new collection with the
        specified name.
        Args:
            name (str): The name of the collection to be created.
        """
        self.collection_name = name
        self.collection = self.chroma_client.create_collection(name=self.collection_name)

    def add_to_collection(self, documents, ids):
        """
        Add documents to the collection.
        This method adds a list of documents to the current collection. The collection
        must be created first.
        Args:
            documents (list): A list of documents to add to the collection.
            ids (list): A list of IDs corresponding to the documents.
        Raises:
            ValueError: If the collection has not been created.
        """
        if self.collection is None:
            raise ValueError("Collection has not been created. Call create_collection method first.")

        self.collection.add(
            documents=documents,
            ids=ids
        )
        print(f"Added {len(documents)} items to collection {self.collection_name}")

    def retrieve_collections(self, query_texts, n_results):
        """
        Retrieve documents from the collection.
        This method queries the collection for documents matching the query texts and
        returns the results.
        Args:
            query_texts (list): A list of query texts to search for in the collection.
            n_results (int): The number of results to return.
        Returns:
            list: A list of results matching the query texts.
        Raises:
            ValueError: If the collection has not been created.
        """
        if self.collection is None:
            raise ValueError("Collection has not been created. Call create_collection method first.")

        results = self.collection.query(
            query_texts=query_texts,
            n_results=n_results
        )
        return results

    def collection_exists(self, collection_name):
        """
         Check if a collection exists in the Chroma database.
         This method checks if a collection with the specified name exists.
         Args:
             collection_name (str): The name of the collection to check.
         Returns:
             bool: True if the collection exists, False otherwise.
         """
        collections = self.chroma_client.list_collections()
        for collection in collections:
            if collection.name == collection_name:
                return True
        return False

    def delete_collection(self, collection_name):
        """
        Delete a collection from the Chroma database.
        This method deletes a collection with the specified name if it exists.
        Args:
            collection_name (str): The name of the collection to delete.
        """
        if self.collection_exists(collection_name):
            self.chroma_client.delete_collection(collection_name)
            print(f"Deleted collection: {collection_name}")
        else:
            print(f"Collection {collection_name} does not exist.")

    def connect_to_collection(self, collection_name):
        """
        Connect to an existing collection in the Chroma database.
        This method connects to a collection with the specified name if it exists.
        Args:
            collection_name (str): The name of the collection to connect to.
        Raises:
            ValueError: If the collection does not exist.
        """
        if self.collection_exists(collection_name):
            self.collection_name = collection_name
            self.collection = self.chroma_client.get_collection(collection_name)
            print(f"Connected to collection: {collection_name}")
        else:
            raise ValueError(f"Collection {collection_name} does not exist.")


def initialize_chroma_db():
    """
    Initialize the Chroma database by creating a new collection.
    This function initializes a ChromaDBManager instance, checks if a collection with
    the specified name exists, deletes it if it does, and then creates a new collection
    with that name.
    Returns:
        ChromaDBManager: The manager instance with the newly created collection.
    """
    collection_name = "tenant_rag"
    manager = ChromaDBManager()
    if manager.collection_exists(collection_name):
        manager.delete_collection(collection_name)
    manager.create_collection(collection_name)
    return manager


def connect_to_existing_collection():
    """
    Connect to an existing collection in the Chroma database.
    This function initializes a ChromaDBManager instance and attempts to connect to
    a collection with the specified name. If the connection is successful, it returns
    the manager instance. If the collection does not exist, it prints the error and
    returns None.
    Returns:
        ChromaDBManager or None: The manager instance if the connection is successful,
        None otherwise.
    """
    collection_name = "tenant_rag"
    manager = ChromaDBManager()
    try:
        manager.connect_to_collection(collection_name)
        return manager
    except ValueError as e:
        print(e)
        return None