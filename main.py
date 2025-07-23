import asyncio
from aiogram.fsm.context import FSMContext
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery
from config import TOKEN, moderators
from keyboards import message_markup
from aiogram.fsm.state import State, StatesGroup
from string_to_date import string_to_date

class SendLater(StatesGroup):
    date_to_public = State()
    message_id = State()
    chat_id = State()

bot = Bot(token=TOKEN)
dp = Dispatcher()
scheduler = AsyncIOScheduler(timezone="Europe/Moscow")


async def send_message_to_group(chat_id, message_id):
    await bot.copy_message(chat_id=-1002289944496, from_chat_id=chat_id, message_id=message_id)


@dp.message(CommandStart())
async def cmd_start(message: Message):
    if message.chat.id in moderators:
        await message.answer('Вы модератор')
    else:
        await message.answer('Привет! Здесь ты можешь прислать интересную новость.')


@dp.callback_query(F.data.startswith('apply'))
async def apply(call: CallbackQuery):
    chat_id = call.message.chat.id
    message_id = call.message.message_id
    await send_message_to_group(chat_id, message_id)


@dp.callback_query(F.data.startswith('time'))
async def time(call: CallbackQuery, state: FSMContext):
    chat_id = call.message.chat.id
    message_id = call.message.message_id
    await state.update_data(
        message_id=message_id,
        chat_id=chat_id
    )
    await call.message.answer("Введите нужное время в формате: ДД.ММ.ГГ ЧЧ:ММ")
    await state.set_state(SendLater.date_to_public)


@dp.message(SendLater.date_to_public)
async def send_later(message: Message, state: FSMContext):
    await state.update_data(date_to_public=message.text)
    data = await state.get_data()
    chat_id = data['chat_id']
    message_id = data['message_id']
    date_input = data['date_to_public']
    await state.clear()
    try:
        date_to_public = string_to_date(date_input)
        scheduler.add_job(send_message_to_group,
                          trigger='date', args=[chat_id, message_id],
                          run_date=date_to_public,
                          )
    except Exception:
        await message.answer('Что-то пошло не так. Попробуйте ещё раз.')



@dp.message()
async def send_subfeed(message: Message):
    if message.chat.id in moderators:
        await message.answer('Вы модератор')
    else:
        await message.answer('Сообщение отправлено')
        for mod_id in moderators:
            await bot.copy_message(chat_id=mod_id, from_chat_id=message.chat.id, message_id=message.message_id, reply_markup=message_markup)


async def main():
    scheduler.start()
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())