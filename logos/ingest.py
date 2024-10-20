from logos.log import log_action
from logos.types import Path

from typing import Optional, Sequence

from llama_index.core import Settings
from llama_index.core import SimpleDirectoryReader
from llama_index.core.schema import BaseNode
from llama_index.core.ingestion import IngestionPipeline, IngestionCache
from llama_index.core.text_splitter import TokenTextSplitter
from llama_index.llms.openai import OpenAI
from llama_index.embeddings.openai import OpenAIEmbedding


Settings.llm = OpenAI(model="gpt-3.5-turbo", temperature=0.1)


def ingest_documents(directory: Path, cache_path: Path) -> Sequence[BaseNode]:
    """
    Ingests documents located in the default specified directory.

    The documents are loaded from the directory and transformed with an
    ingestion pipeline.
    """
    print("Ingesting files from:", directory)
    documents = SimpleDirectoryReader(
            directory,
            filename_as_id=True,
    ).load_data()

    # Log the uploading
    for doc in documents:
        log_action(action=f"User uploaded {doc.id_} file",
                   action_type="UPLOAD")

    # Load ingestion cache
    cache = _try_load_cache(cache_path)

    pipeline = IngestionPipeline(
            transformations=[
                TokenTextSplitter(chunk_size=1024, chunk_overlap=20),
                OpenAIEmbedding(),
            ],
            cache=cache
    )

    nodes = pipeline.run(documents=documents)
    pipeline.cache.persist(cache_path)

    return nodes


def _try_load_cache(path: Path) -> Optional[IngestionCache]:
    """Tries to load cache file."""
    try:
        cached_hashes = IngestionCache.from_persist_path(path)
        print("Cache file found. Running using cache...")
    except Exception:
        cached_hashes = None
        print("No cache file found. Running withoug...")

    return cached_hashes
