import requests
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

BOT_TOKEN = "8478003974:AAEf1RHpMJ8Aw0pAYx_Q2XtzbctAgY7V3EM"
DJANGO_API_URL = "http://127.0.0.1:8000/api/save_chat_id/"
DJANGO_API_TOKEN = "123"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()  # no bot here in v3

@dp.message(Command("start"))
async def start_handler(message: types.Message):
    payload = {
        "chat_id": message.chat.id,
        "username": message.from_user.username
    }
    headers = {"Authorization": f"Token {DJANGO_API_TOKEN}"}

    try:
        requests.post(DJANGO_API_URL, json=payload, headers=headers)
    except Exception as e:
        print("Error sending to Django:", e)

    await message.answer("✅ You are now subscribed to order notifications!")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
