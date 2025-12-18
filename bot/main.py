from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.client.default import DefaultBotProperties


import asyncio
import aiohttp

import logging
import markdown

def md_to_html(md_text: str) -> str:
    return markdown.markdown(md_text)

from dotenv import load_dotenv
import os
load_dotenv()

logging.basicConfig(level=logging.INFO)

API_TOKEN = os.getenv("TELEGRAM_API_TOKEN")
BACKEND_URL = os.getenv("BACKEND_URL")

bot = Bot(token=API_TOKEN,
          default=DefaultBotProperties(parse_mode="Markdown"))
dp = Dispatcher()


@dp.message(Command("start"))
async def start_cmd(message: types.Message):
    await message.answer("Привет! Я специалист по УК КР и я тебе помогу!")


@dp.message()
async def handle_message(message: types.Message):
    user_text = message.text
    
    waiting_msg = await message.answer("Секунду... думаю 🤔")
    
    async with aiohttp.ClientSession() as session:
        try:
            async with session.post(
                BACKEND_URL,
                json={"question": user_text}
            ) as response:
                if response.status != 200:
                    answer = f"Бэкэнд вернул ошибку: {response.status}"
                else:
                    response_data = await response.json()
                    answer = response_data.get("answer", "Бэкэнд не вернул ответ :(")
        
        except Exception as e:
            answer = f"Ошибка при обращении к бэкэнду: {e}"

    await waiting_msg.edit_text(answer)


async def main():
    logging.info("Бот успешно запущен и ждёт сообщения")
    await dp.start_polling(bot)
    
if __name__ == "__main__":
    asyncio.run(main())
