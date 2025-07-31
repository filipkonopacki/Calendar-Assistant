import os
import atexit
import datetime
from enum import Enum
from utils import LOGS_DIR


class LogType(Enum):
    INFO = 'INFO'
    ERROR = 'ERROR'
    INPUT = 'INPUT'
    WARN = 'WARNING'
    BOT = 'BOT'
    USER = 'USER'
    DEBUG = 'DEBUG'


class Logger:
    def __init__(self):
        self._setup_log_file()
        atexit.register(self._close_log_file)  # Ensures file is closed on exit

    def _setup_log_file(self):
        today_str = datetime.date.today().strftime('%Y-%m-%d')
        self.logs_dir = os.path.join(LOGS_DIR, today_str)
        os.makedirs(self.logs_dir, exist_ok=True)

        filename = f'log__{today_str}.txt'
        self.log_file_path = os.path.join(self.logs_dir, filename)
        self.log_file = open(self.log_file_path, 'a', encoding='utf-8')

        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
        self.log_file.write(f'********** New conversation {timestamp} **********\n')

    def _close_log_file(self):
        if self.log_file and not self.log_file.closed:
            self.log_file.write('********** End of session **********\n')
            self.log_file.close()

    def _create_log(self, message_type, message):
        timestamp = datetime.datetime.now().strftime('%H:%M:%S')
        log = f'[{message_type.value} {timestamp}]\t{message}'
        print(log)
        self.log_file.write(log + '\n')

    def info(self, message): self._create_log(LogType.INFO, message)
    def error(self, message): self._create_log(LogType.ERROR, message)
    def bot(self, message): self._create_log(LogType.BOT, message)
    def user(self, message): self._create_log(LogType.USER, message)
    def warning(self, message): self._create_log(LogType.WARN, message)
    def debug(self, message): self._create_log(LogType.DEBUG, message)


logger = Logger()
