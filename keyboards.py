from aiogram.utils.keyboard import InlineKeyboardMarkup, InlineKeyboardButton
tg_button_apply = InlineKeyboardButton(
        text='ДА',
        callback_data=f'apply'
    )
tg_button_edit = InlineKeyboardButton(
        text='редактировать',
        callback_data=f'edit'
    )
row = [tg_button_apply, tg_button_edit]
rows = [row]
message_markup = InlineKeyboardMarkup(inline_keyboard=rows)