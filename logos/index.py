from llama_index.core import StorageContext
from llama_index.core import load_index_from_storage
from llama_index.core import VectorStoreIndex

from logos.types import Path, Nodes


def index_from_nodes(nodes: Nodes, persist_dir: Path) -> VectorStoreIndex:
    """Creates a vector store index from a sequence of nodes."""
    index = VectorStoreIndex(nodes)
    print(f"Persisting vector-store-index at {persist_dir}")
    index.storage_context.persist(persist_dir=persist_dir)
    return index


def index_from_path(path: Path) -> VectorStoreIndex:
    """Loads a vector store index from a path"""
    print(f"Loading vector-store-index from {path}")
    storage_context = StorageContext.from_defaults(persist_dir=path)
    index = load_index_from_storage(storage_context=storage_context)
    return index
