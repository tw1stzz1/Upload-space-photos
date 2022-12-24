# Космический Телеграм

Код позволяет загрузить фотографиии космоса и запуска ракет. А также публиковать фотографии в телеграм-канале используя бота.

### Как установить
Python3 должен быть уже установлен. Используйте `pip` (или `pip3`, есть есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```

### Переменные окружения
Переменные окружения используются для изменения конфигурации системы. Результат работы многих приложений на Python зависит от значений определённых переменных окружения.
Это избавит нас от необходимости исправлять переменные среды вручную и сделает код безопаснее: будут спрятаны конфиденциальные данные, которые требуется присвоить переменной окружения (например, токен API).

#### Пример .env файла:
```
API_KEY="chyprECONFsgQIIATq0Yi5SeA5WLz4jZdDArU4So"
TELEGRAM_TOKEN="958423683:AAEAtJ5Lde5YYfkjergber"
TG_CHAT_ID="@testing_my_tg_bots"
DELAY_TIME=14400
```

Для начала вам нужно получить API_KEY на сайте [NАSА](https://api.nasa.gov/#apod).

После создать бота с помощью другого бота [Отец ботов](https://telegram.me/BotFather).
Полученный токен вставить в `.env` файл.

И также добавить название канала в `.env`.

Еще можно изменить время задержки между публикациями изображений в `.env`. Время задержки измеряется в секундах.

### Пример запуска кода
``` python
#Загрузка фотографий Земли
python epic_images.py
#Загрузка фотографий космоса
python apod_images.py
#Загрузка фотографий запуска ракет
python spacex_last_launch_images.py --launch #номер запуска (по умолчанию последний)
#Публикация загруженных фотографий в телеграм-канале
python publish_space_images.py
```

### Цель проекта



# Space Telegram

The code allows you to upload photos of space and rocket launches. And also publish photos in the telegram channel using the bot.

### How to install

#### Python3 should already be installed. Use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```

### Environment variables
Environment variables are used to change the system configuration. The output of many Python applications depends on the values of certain environment variables.
This saves us from having to fix environment variables manually and makes the code safer by hiding sensitive data that needs to be assigned to an environment variable (for example, an API token).

#### .env example:
```
API_KEY="chyprECONFsgQIIATq0Yi5SeA5WLz4jZdDArU4So"
TELEGRAM_TOKEN="958423683:AAEAtJ5Lde5YYfkjergber"
TG_CHAT_ID="@testing_my_tg_bots"
DELAY_TIME=14400
```

First you need to get an api key from [NASA website](https://api.nasa.gov/#apod).

After create a bot using another bot [Bot Father](https://telegram.me/BotFather).
Insert the token you received into the `.env` file.

And also add your chat name to `.env`.

You can also change the delay time before sending in .env. It is measured in seconds.

#### Code run example
``` python
#Loading photos of Earth
python epic_images.py
#Loading photos of space
python apod_images.py
#Loading photos of rocket launch
python spacex_last_launch_images.py --launch #launch number (default last)
#Publishing uLoaded photos in the telegram channel
python publish_space_images.py
```

### Project Goals


