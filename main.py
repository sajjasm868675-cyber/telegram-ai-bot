mport asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import Message

# توکن ربات تلگرام
TOKEN = "8554754667:AAHJLzIkN9I-Wf6I3qJqJMH9cge44PQhZDk"

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start_handler(message: Message):
    await message.answer("سلام سجاد 👋 رباتت آنلاین شد!")

@dp.message()
async def echo_handler(message: Message):
    await message.answer(f"تو گفتی: {message.text}")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
