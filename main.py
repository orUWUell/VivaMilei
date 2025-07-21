import asyncio

from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery
from config import TOKEN, moderators
from keyboards import message_markup
bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def cmd_start(message: Message):
    if message.chat.id in moderators:
        await message.answer('Вы модератор')
    else:
        await message.answer('Привет! Здесь ты можешь прислать интересную новость.')

@dp.message()
async def send_subfeed(message: Message):

    if message.chat.id in moderators:
        await message.answer('Вы модератор')
    else:
        await message.answer('Сообщение отправлено')
        for mod_id in moderators:
            await bot.copy_message(chat_id=mod_id, from_chat_id=message.chat.id, message_id=message.message_id, reply_markup=message_markup)

@dp.callback_query(F.data.startswith('apply'))
async def apply(call: CallbackQuery):
    chat_id = call.message.chat.id
    message_id = call.message.message_id
    await bot.copy_message(chat_id=-1002289944496, from_chat_id=chat_id, message_id=message_id)

# @dp.callback_query(F.data.startswith('edit'))
# async def edit(call: CallbackQuery):
#     chat_id = call.message.chat.id
#     message_id = call.message.message_id
#     await bot.edit_message_text(text='<b>Отправляю сообщение!!!</b>', chat_id=chat_id, message_id=message_id, reply_markup=message_markup)


async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())