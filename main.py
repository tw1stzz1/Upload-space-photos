import os

import telegram
from dotenv import load_dotenv





def main():
    load_dotenv()
    token = os.getenv("TOKEN")
    chat_id = os.getenv("CHAT_ID")
    bot = telegram.Bot(token=token)
    updates = bot.get_updates()
    bot.send_photo(chat_id, photo=open('images/spacex_0.jpg', 'rb'))
if __name__ == "__main__":
    main()