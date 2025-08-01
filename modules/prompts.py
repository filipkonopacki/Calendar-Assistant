from jinja2 import Environment, FileSystemLoader

from utils import PROMPT_DIR

env = Environment(loader=FileSystemLoader(PROMPT_DIR))


def load_prompt(template_name, context=None):
    return env.get_template(template_name).render(context or {})

