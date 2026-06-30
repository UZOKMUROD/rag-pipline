from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("DEEPSEEK_API")
sql_dir = os.getenv("CHUNKS_DB_URL")

encoder_model = os.getenv("DEFAULT_ENCODER_MODEL")
reranker_model = os.getenv("DEFAULT_RERANKER_MODEL")

save_encoder_path = os.getenv("ENCODER_PATH")
save_reranker_path = os.getenv("RERANKER_PATH")

