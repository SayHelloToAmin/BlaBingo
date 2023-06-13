from pyrogram import Client
from pyrogram.types import CallbackQuery

from utils.group_mode import validate_user_status
import DB
from utils.send_exceptions import send_exception_to_support
from utils.inline_markups import inline_set_mode_keyboard

MODE_CHANGED_TEXT = 'new mode has been set'
MODE_IS_ALREADY_SET_TEXT = 'this mode is currently set'
NOT_ADMIN_TEXT = 'admin nisti'
ERROR_TEXT = 'be error barkhord kardim'

# texts = {
#     'mode_changed': 'new mode has been set',
#     'mode_is_already_set': 'this mode is currently set',
#     'not_admin': 'admin nisti',
#     'error': 'error'
# }

# callback #mode
async def set_mode_to_db(client: Client, callback_query: CallbackQuery, data: list):
    """when admin clicks on (slow, fast, normal) on (inline_keybaord) this function will run"""
    chat_id = int(data[2])
    if not await validate_user_status(chat_id=chat_id, user_id=callback_query.from_user.id, client=client):
        return await callback_query.answer(NOT_ADMIN_TEXT, show_alert=True)

    current_group_mode: int = DB.showgpmode(chat_id)
    user_choosen_mode = int(data[1])

    if user_choosen_mode == current_group_mode:
        return await callback_query.answer(MODE_IS_ALREADY_SET_TEXT, show_alert=True)

    try:
        DB.setnewmode(chat_id, user_choosen_mode)
        inline_markup = await inline_set_mode_keyboard(user_choosen_mode, chat_id)
        await callback_query.edit_message_text(MODE_CHANGED_TEXT, reply_markup=inline_markup)

    except Exception as e:
        await callback_query.answer(ERROR_TEXT, show_alert=True)
        await send_exception_to_support(client, str(e))

