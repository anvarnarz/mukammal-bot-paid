import os

# .env fayl ichidan quyidagilarni o'qiymiz
BOT_TOKEN = str(os.environ.get("BOT_TOKEN"))  # Bot token
ADMINS = list(os.environ.get("ADMINS"))  # adminlar ro'yxati
IP = str(os.environ.get("ip"))  # Xosting ip manzili
PROVIDER_TOKEN = str(os.environ.get("PROVIDER_TOKEN"))