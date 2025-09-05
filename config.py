import os

# Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "8271214309:AAG5QCxq5MOtWzJqgcVwxcMnxJLQPv0SU7A")

# Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "25225538"))

# Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "66d401695a3326c406e8782fa26d158d")

# Your Owner / Admin Id For Broadcast 
ADMINS = int(os.environ.get("ADMINS", "8075836012"))

# Your Mongodb Database Url
# Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_URI = os.environ.get("DB_URI", "") # Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_NAME = os.environ.get("DB_NAME", "vjsavecontentbot")

# If You Want Error Message In Your Personal Message Then Turn It True Else If You Don't Want Then Flase
ERROR_MESSAGE = bool(os.environ.get('ERROR_MESSAGE', True))
