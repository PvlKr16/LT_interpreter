import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')
ADMIN_TELEGRAM_ID = os.getenv('ADMIN_TELEGRAM_ID')
