import os.path
import datetime
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

from utils import GOOGLE_CREDENTIALS, GOOGLE_TOKEN

# If modifying these scopes, delete the token.json file.
SCOPES = ['https://www.googleapis.com/auth/calendar.events']


class CalendarService:
    def __init__(self):
        self.service = self._get_calendar_service()

    @staticmethod
    def _get_calendar_service():
        if os.path.exists(GOOGLE_TOKEN):
            creds = Credentials.from_authorized_user_file(GOOGLE_TOKEN, SCOPES)
        else:
            flow = InstalledAppFlow.from_client_secrets_file(GOOGLE_CREDENTIALS, SCOPES)
            creds = flow.run_local_server(port=0)
            with open(GOOGLE_TOKEN, 'w') as token:
                token.write(creds.to_json())

        return build('calendar', 'v3', credentials=creds)

    def create_event(self, summary, start, duration_minutes=60):
        start_datetime = datetime.datetime.fromisoformat(start)
        end = (start_datetime + datetime.timedelta(minutes=duration_minutes)).isoformat()

        event = {
            'summary': summary,
            'start': {'dateTime': start, 'timeZone': 'Europe/Warsaw'},
            'end': {'dateTime': end, 'timeZone': 'Europe/Warsaw'}
        }

        created_event = self.service.events().insert(calendarId='primary', body=event).execute()
        return created_event.get('htmlLink')
