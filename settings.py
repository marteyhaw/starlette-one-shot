from starlette.config import Config

config = Config(".env")
MONGO_URL = config("MONGO_URL")
MONGO_DB = config("MONGO_DB")
