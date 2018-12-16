import os
from dotenv import load_dotenv


load_dotenv(verbose=True)

ACADEMIC_TERM = os.getenv("ACADEMIC_TERM")
MYCONCORDIA_USERNAME = os.getenv("MYCONCORDIA_USERNAME")
MYCONCORDIA_PASSWORD = os.getenv("MYCONCORDIA_PASSWORD")
