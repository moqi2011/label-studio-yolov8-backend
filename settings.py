import os

MODEL_TYPE = os.environ.get("MODEL_TYPE").lower()
MODEL_FILE_PATH = os.environ.get("MODEL_FILE_PATH", "best.pt")
LS_URL = os.environ.get("LS_URL")
LS_API_TOKEN = os.environ.get("LS_API_TOKEN")
