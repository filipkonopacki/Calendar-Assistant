import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_KEY = os.getenv("OPENAI_KEY")

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
PROMPT_DIR = os.path.join(ROOT_DIR, 'prompt_templates')

# Define Google services credentials and token file paths
GOOGLE_CREDENTIALS = os.path.join(ROOT_DIR, 'credentials.json')
GOOGLE_TOKEN = os.path.join(ROOT_DIR, 'token.json')

# Define the path for the logs directory
LOGS_DIR = os.path.join(ROOT_DIR, 'logs')
if not os.path.exists(LOGS_DIR):
    os.makedirs(LOGS_DIR)
