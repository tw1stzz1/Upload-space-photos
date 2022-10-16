import os
import random
import os.path
import time

import telegram
from dotenv import load_dotenv


def publish_space_images(bot, chat_id, delay_time):
    for dir_path, sub_dir, files in os.walk('images'):
        while True:
            for name in files:
                file_path = os.path.join(dir_path, name)
                with open(file_path, 'rb') as file:
                    photo = file
                bot.send_photo(chat_id, photo=photo)
                time.sleep(delay_time)
    
    
def main():
    load_dotenv()
    delay_time = int(os.getenv("DELAY_TIME",default=14400))
    token = os.getenv("TELEGRAM_TOKEN")
    chat_id = os.getenv("CHAT_ID")
    bot = telegram.Bot(token=token)
    updates = bot.get_updates()
    publish_space_images(bot, chat_id, delay_time)
    
    
if __name__ == "__main__":
    main()
    
