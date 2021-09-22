# from environs import Env
#
# # environs kutubxonasidan foydalanish
# env = Env()
# env.read_env()
#
# # .env fayl ichidan quyidagilarni o'qiymiz
# BOT_TOKEN = env.str("BOT_TOKEN")  # Bot token
# ADMINS = env.list("ADMINS")  # adminlar ro'yxati
# IP = env.str("ip")  # Xosting ip manzili
# PROVIDER_TOKEN = env.str("PROVIDER_TOKEN")

import os

# .env fayl ichidan quyidagilarni o'qiymiz
BOT_TOKEN = str(os.environ.get("BOT_TOKEN"))  # Bot token
ADMINS = list(os.environ.get("ADMINS"))  # adminlar ro'yxati
IP = str(os.environ.get("ip"))  # Xosting ip manzili
PROVIDER_TOKEN = str(os.environ.get("PROVIDER_TOKEN"))