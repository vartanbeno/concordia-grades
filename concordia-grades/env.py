import os
from dotenv import load_dotenv


ROOT_DIR = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

load_dotenv(verbose=True)

ACADEMIC_TERM = os.getenv("ACADEMIC_TERM")

MYCONCORDIA_USERNAME = os.getenv("MYCONCORDIA_USERNAME")
MYCONCORDIA_PASSWORD = os.getenv("MYCONCORDIA_PASSWORD")

MY_PHONE_NUMBER = os.getenv("MY_PHONE_NUMBER")

TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_NUMBER = os.getenv("TWILIO_NUMBER")
