# from modules.calendar import CalendarService
from modules.nlp import NLP
#
# from utils.logger import logger
#
# calendar = CalendarService()
agent = NLP()
#
# user_input = "Remind me I have a doctor appointment next Monday at 10:00 AM"
# logger.user(user_input)
# response_json = agent.get_response(user_input)
# logger.bot(response_json)
# link = calendar.create_event(
#     summary=response_json['subject'],
#     start=response_json['datetime'],
# )
#
# logger.info(f"Event created: {link}")
import gradio as gr

from utils.logger import logger


def conversation(user_message, chat_history):
    # Ignore empty messages
    if user_message.strip() == "":
        return gr.update(), chat_history

    # Display user message
    logger.user(user_message)
    chat_history.append((user_message, None))

    # Simulate a response (replace with actual NLP model call)
    response = agent.get_response(user_message)
    chat_history.append((None, response))
    logger.bot(response.__str__())

    # Clear textbox and return updated chat
    return "", chat_history


def init_chat():
    welcome_message = agent.get_welcome_message()
    logger.bot(welcome_message)
    return [(None, welcome_message)]


with gr.Blocks(title='Calendar Assistant AI') as demo:
    gr.Markdown(
        """
        # Calendar Assistant AI
        This is a demo of the Calendar Assistant AI. You can ask questions about your calendar, and it will respond with relevant information.
        """
    )

    chatbot = gr.Chatbot(label="Convesation", height=500, show_copy_button=True)
    message = gr.Textbox(label="Your message", placeholder="Type your message here...", show_label=False, autofocus=True)
    submit_button = gr.Button("Send", variant="primary")

    submit_button.click(
        fn=conversation,
        inputs=[message, chatbot],
        outputs=[message, chatbot]
    )
    message.submit(
        fn=conversation,
        inputs=[message, chatbot],
        outputs=[message, chatbot]
    )
    demo.load(init_chat, outputs=chatbot)

if __name__ == '__main__':
    demo.launch()
