from modules.calendar import CalendarService
from modules.nlp import NLP

from utils.logger import logger

calendar = CalendarService()
agent = NLP()

user_input = "Remind me I have a doctor appointment next Monday at 10:00 AM"
logger.user(user_input)
response_json = agent.get_response(user_input)
logger.bot(response_json)
link = calendar.create_event(
    summary=response_json['subject'],
    start=response_json['datetime'],
)

logger.info(f"Event created: {link}")
