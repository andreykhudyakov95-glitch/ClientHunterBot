import json

# 🔥 ВАЖНО:
# СЮДА ты потом сам вставишь токен своего Telegram-бота
TOKEN = "PASTE_YOUR_TOKEN_HERE"

# Твой Telegram ID — всё верно
ADMIN_ID = 7906503101

# Загружаем ключевые слова из файла
with open("keywords.txt", "r", encoding="utf-8") as f:
    KEYWORDS = [x.strip().lower() for x in f.readlines()]

# Загружаем ID чатов из файла
with open("chats.json", "r", encoding="utf-8") as f:
    GROUPS = [str(x).strip() for x in json.load(f)]
