from dotenv import load_dotenv
import os

load_dotenv()

WORKBOOK_ID = os.getenv('WORKBOOK_ID')
DRIVER_PATH = os.getenv('DRIVER_PATH')

SCHEDULER_HOUR = os.getenv('SCHEDULER_HOUR')
SCHEDULER_MINUTE = os.getenv('SCHEDULER_MINUTE')