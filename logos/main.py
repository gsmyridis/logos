from logos.ingest import ingest_documents
from logos.index import index_from_path, index_from_nodes
from logos.settings.globals import STORAGE_DIR, CACHE_FILE, INDEX_STORAGE_DIR


def main():

    nodes = ingest_documents(directory=STORAGE_DIR, cache_path=CACHE_FILE)
    index = index_from_nodes(nodes=nodes, persist_dir=INDEX_STORAGE_DIR)

    index = index_from_path(path=INDEX_STORAGE_DIR)
    chat_engine = index.as_chat_engine()

    for i in range(3):
        query = input("Question: ")
        response = chat_engine.chat(query)
        print("Response: ", response)


if __name__ == "__main__":

    main()
