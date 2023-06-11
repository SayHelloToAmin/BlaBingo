from pyrogram.types import Message
from pyrogram import Client
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from utils.group_mode import validate_user_status
import DB


# command: /mode (gp) => used in groups
async def set_mode_type_group(client: Client, message: Message):
    """this command will be used in groups to send a message for sending admin to private"""
    if not await validate_user_status(message.chat.id, message.from_user.id, client):
        return await message.reply('admin nisti')

    inline_markup = await _inline_to_pv_keybaord(message.chat.id)
    await message.reply('brim pv', reply_markup=inline_markup)

async def _inline_to_pv_keybaord(chat_id: int) -> InlineKeyboardMarkup:
    """create keybaord for specific chat id to redirect admin"""
    inline_markup = InlineKeyboardMarkup([
        [InlineKeyboardButton('To Pv', url=f'http://telegram.me/BlaBingoBot?start=mode-{chat_id}')]
    ])
    return inline_markup


# commands /start (pv) => have chat_id with it too
async def set_mode_type_pv(client: Client, message: Message, extra_args: str):
    """when admin clicks on the 'go to private' and starts the robot this function will run & extra_args is chatid
    here """
    chat_id = int(extra_args)
    if not await validate_user_status(chat_id=chat_id, user_id=message.from_user.id, client=client):
        return await message.reply('admin nisti')

    current_group_mode = DB.showgpmode(chat_id)
    inline_markup = await _inline_set_mode_keyboard(current_group_mode, chat_id)
    await message.reply('entekhab konid', reply_markup=inline_markup)


async def _inline_set_mode_keyboard(current_mode: str, chat_id: int) -> InlineKeyboardMarkup:
    """current mode of the group will be marked with emoji"""
    inline_keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton('slow' if current_mode != 1 else 'slow ⭐️', callback_data=f'mode#1#{chat_id}')],
        [InlineKeyboardButton('normal' if current_mode != 2 else 'normal ⭐️', callback_data=f'mode#2#{chat_id}')],
        [InlineKeyboardButton('fast' if current_mode != 3 else 'fast ⭐️', callback_data=f'mode#3#{chat_id}')]
    ])
    return inline_keyboard
