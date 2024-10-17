import os


# Define directories
BASE_DIR = "data"
CACHE_DIR = os.path.join(BASE_DIR, "cache")
STORAGE_DIR = os.path.join(BASE_DIR, "ingestion_storage")
SESSION_DATA_DIR = os.path.join(BASE_DIR, "session")
INDEX_STORAGE_DIR = os.path.join(BASE_DIR, "index_storage")


# Create directories
os.makedirs(CACHE_DIR, exist_ok=True)
os.makedirs(STORAGE_DIR, exist_ok=True)
os.makedirs(SESSION_DATA_DIR, exist_ok=True)
os.makedirs(INDEX_STORAGE_DIR, exist_ok=True)


# Define file path
LOG_FILE = os.path.join(SESSION_DATA_DIR, "user_actions.log")
SESSION_FILE = os.path.join(SESSION_DATA_DIR, "user_session_state.yaml")

CACHE_FILE = os.path.join(CACHE_DIR, "pipeline_cache.json")
CONVERSATION_FILE = os.path.join(CACHE_DIR, "chat_history.json")
QUIZ_FILE = os.path.join(CACHE_DIR, "quiz.csv")
SLIDES_FILE = os.path.join(CACHE_DIR, "slides.json")


# Define parameters
QUIZ_SIZE = 5
ITEMS_ON_SLIDES = 4
