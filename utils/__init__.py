import os
import dotenv
from datetime import datetime
from jinja2 import Environment, FileSystemLoader


dotenv.load_dotenv()
OPENAI_KEY = os.getenv("OPENAI_KEY")

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
PROMPT_DIR = os.path.join(ROOT_DIR, '..', 'prompt_templates')

env = Environment(loader=FileSystemLoader(PROMPT_DIR))
SYS_MSG = env.get_template('sys_msg.jinja2').render(today=datetime.now())
