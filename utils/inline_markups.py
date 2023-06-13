from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

async def inline_set_mode_keyboard(current_group_mode: int, chat_id: int) -> InlineKeyboardMarkup:
    """current mode of the group will be marked with emoji"""
    inline_keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton('slow' if current_group_mode != 1 else 'slow ⭐️', callback_data=f'mode#1#{chat_id}')],
        [InlineKeyboardButton('normal' if current_group_mode != 2 else 'normal ⭐️', callback_data=f'mode#2#{chat_id}')],
        [InlineKeyboardButton('fast' if current_group_mode != 3 else 'fast ⭐️', callback_data=f'mode#3#{chat_id}')]
    ])
    return inline_keyboard
