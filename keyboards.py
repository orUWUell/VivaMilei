from aiogram.utils.keyboard import InlineKeyboardMarkup, InlineKeyboardButton
tg_button_apply = InlineKeyboardButton(
        text='ДА',
        callback_data=f'apply'
    )
tg_button_edit = InlineKeyboardButton(
        text='редактировать',
        callback_data=f'edit'
    )

tg_button_time = InlineKeyboardButton(
        text='time',
        callback_data=f'time'
    )

row = [tg_button_apply, tg_button_edit, tg_button_time]
rows = [row]
message_markup = InlineKeyboardMarkup(inline_keyboard=rows)