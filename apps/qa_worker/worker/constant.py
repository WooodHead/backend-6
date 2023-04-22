import os

from dotenv import load_dotenv

load_dotenv()

POSTGRES_USERNAME = os.environ["POSTGRES_USERNAME"]
POSTGRES_PASSWORD = os.environ["POSTGRES_PASSWORD"]
POSTGRES_HOST = os.environ["POSTGRES_HOST"]
POSTGRES_PORT = os.environ["POSTGRES_PORT"]
POSTGRES_DB = os.environ["POSTGRES_DB"]
POSTGRES_SCHEMA = os.environ["POSTGRES_SCHEMA"]
FAISS_URL = f"postgresql://{POSTGRES_USERNAME}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/faiss"

OPENAI_API_KEY = os.environ['OPENAI_API_KEY']

EMBEDDING_MODEL = "ada"
QA_MODEL = "gpt-3.5-turbo"
