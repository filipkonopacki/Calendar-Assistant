import json
from openai import OpenAI
from datetime import datetime

from utils import OPENAI_KEY
from modules.prompts import load_prompt

PROMPTS_CONFIG = {
    'intent': {
        'template': 'define_intent.jinja2',
        'temperature': 0.3
    },
    'reminder': {
        'template': 'reminder_extraction.jinja2',
        'temperature': 0.2
    },
    'greeting': {
        'template': 'greeting.jinja2',
        'temperature': 0.7
    }
}


class NLP:
    def __init__(self):
        self._client = OpenAI(api_key=OPENAI_KEY)
        self._sys_msg = load_prompt('sys_msg.jinja2', context={'today': datetime.now().isoformat()})

    def _get_intent(self, prompt):
        prompt = load_prompt(PROMPTS_CONFIG['intent']['template'], context={'user_input': prompt})
        intent = self._call_llm(prompt, PROMPTS_CONFIG['intent']['temperature'])
        return intent

    def get_welcome_message(self):
        prompt = load_prompt(PROMPTS_CONFIG['greeting']['template'])
        return self._call_llm(prompt, PROMPTS_CONFIG['greeting']['temperature'])

    def _call_llm(self, prompt, temperature):
        response = self._client.responses.create(
            model='gpt-4.1-mini',
            temperature=temperature,
            instructions=self._sys_msg,
            input=prompt,
        ).output_text

        return response

    def get_response(self, user_input):
        intent = self._get_intent(user_input)
        if intent == 'reminder':
            prompt = load_prompt(PROMPTS_CONFIG['reminder']['template'], context={'user_input': user_input})
            response = self._call_llm(prompt, PROMPTS_CONFIG['reminder']['temperature'])
            try:
                response_json = json.loads(response)
            except json.JSONDecodeError:
                response_json = {'error': 'Invalid response format'}

        else:
            response_json = {'error': f'Unknown intent: {intent}'}

        return response_json


if __name__ == '__main__':
    nlp = NLP()

