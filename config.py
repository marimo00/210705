import os

TELEGRAM_TOKEN = os.environ.get('TELEGRAM_TOKEN', '1277942532:AAF7fGMs4hyHtPAFH9ILlfGu1tmRist-Ikc')
CHAT_ID = os.environ.get('CHAT_ID', '-499559301')

if not TELEGRAM_TOKEN or not CHAT_ID:
  raise Exception(TELEGRAM_TOKEN, CHAT_ID)

if __name__ == "__main__":
  print(TELEGRAM_TOKEN)
  print(CHAT_ID)