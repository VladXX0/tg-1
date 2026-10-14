import asyncio 
from token import TOKEN
from aiogram import Bot, Dispatcher
from aiogram.types import Message

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message()
async def handle_message(message: Message):
    await message.answer("Hello, World!")
    await message.reply("как дела?")
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())