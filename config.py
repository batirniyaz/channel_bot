from dotenv import load_dotenv
import os

load_dotenv()

TOKEN = os.getenv('TOKEN')
CHANNEL_ID = os.getenv('CHANNEL_ID')
ADMIN_ID = os.getenv('ADMIN_ID')
GEMINI_API = os.getenv('GEMINI_API')
