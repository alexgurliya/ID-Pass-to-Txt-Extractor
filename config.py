import os

api_id =  os.environ.get("API_ID", "23671274")
api_hash = os.environ.get("API_HASH", "09b9c07a023f7c13c2164f2b22bd937e")
bot_token = os.environ.get("BOT_TOKEN", " ")
auth_users = os.environ.get("AUTH_USERS", "903077627,903077627")
sudo_users = [int(num) for num in auth_users.split(",")]
osowner_users = os.environ.get("OWNER_USERS", "903077627,1369808729")
owner_users = [int(num) for num in osowner_users.split(",")]
