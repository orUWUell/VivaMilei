import asyncio

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message
from config import TOKEN, moderators
bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def cmd_start(message: Message):
    if message.from_user.username in moderators:
        await message.answer('Вы модератор')
    else:
        await message.answer('Привет! Здесь ты можешь прислать интересную новость.')

@dp.message()
async def send_subfeed(message: Message):
    if message.from_user.username in moderators:
        await message.answer('Вы модератор')
    else:
        await message.answer('Сообщение отправлено')
        await bot.send_message(message.chat.id, text=message.text)

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())