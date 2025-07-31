import json
from openai import OpenAI

from utils import OPENAI_KEY, SYS_MSG


class NLP:
    def __init__(self):
        self._client = OpenAI(api_key=OPENAI_KEY)

    def get_response(self, prompt):
        response = self._client.responses.create(
            model="gpt-4.1-mini",
            temperature=0.2,
            instructions=SYS_MSG,
            input=prompt,
        ).output_text

        try:
            data = json.loads(response)
            return data
        except json.JSONDecodeError:
            raise ValueError("Response is not valid JSON: " + response)


if __name__ == "__main__":
    nlp = NLP()

