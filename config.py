# Copyright (c) 2025 devgagan : https://github.com/devgaganin.  
# Licensed under the GNU General Public License v3.0.  
# See LICENSE file in the repository root for full license text.

import os
from dotenv import load_dotenv

load_dotenv()

# VPS --- FILL COOKIES 🍪 in """ ... """ 

INST_COOKIES = """
# wtite up here insta cookies
"""

YTUB_COOKIES = """
# write here yt cookies
"""

API_ID = os.getenv("API_ID", "23939637")
API_HASH = os.getenv("API_HASH", "477f51720ede3eef6997dbc442151c43")
BOT_TOKEN = os.getenv("BOT_TOKEN", "")
MONGO_DB = os.getenv("MONGO_DB", "mongodb+srv://rex380895:sxz1J690QyA5RIaj@cluster0.scyfy8x.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
OWNER_ID = list(map(int, os.getenv("OWNER_ID", "6425525488").split())) # list seperated via space
DB_NAME = os.getenv("DB_NAME", "MANGO_DB")
STRING = os.getenv("STRING", "1BVtsOJ4BuyBlTNK6O6tqteRyAGEXUYAlyb6lYkcMo0dIclJY6Lc5UK4XQZY7MrDjC11RTo-OpVEIQZvPxD2MJ7_2dlL75XN0U3D55nluEMFZ5UpCcA5IHdzCspk1M8ONckq0Zb4s6r-9MQm4-ml77uNM7fVv_MjUGxCBsMgqYXIypB6Co1M17yYtMPOST1vQFpa8YMSUeVBvP2eQJQ20pkdyqmLlsuAUbgO_YCO9WiVwLmGVsr-nIcMv6baxLnKljDBqDCTgfTxEzb9JCYAiwSHGkQ_f-zX-k04FZx8pzjaNFjO1zMU84TNleae8rC7ccsL5NNUhFV8jGMigT3T6zoi4_Qmx5f8=") # optional
LOG_GROUP = int(os.getenv("LOG_GROUP", "-1002780402081")) # optional with -100
FORCE_SUB = int(os.getenv("FORCE_SUB", "-1002780402081")) # optional with -100
MASTER_KEY = os.getenv("MASTER_KEY", "lq0a7uQHiGP00yzzYN3YF1yOIqIddCygNm9lv4rUM64=") # for session encryption
IV_KEY = os.getenv("IV_KEY", "fa6cd9ac65d3fc6053e4bdfb58de22d4") # for decryption
YT_COOKIES = os.getenv("YT_COOKIES", YTUB_COOKIES)
INSTA_COOKIES = os.getenv("INSTA_COOKIES", INST_COOKIES)
FREEMIUM_LIMIT = int(os.getenv("FREEMIUM_LIMIT", "0"))
PREMIUM_LIMIT = int(os.getenv("PREMIUM_LIMIT", "500"))
JOIN_LINK = os.getenv("JOIN_LINK", "https://t.me/team_spy_pro") # this link for start command message
ADMIN_CONTACT = os.getenv("ADMIN_CONTACT", "https://t.me/username_of_admin")

