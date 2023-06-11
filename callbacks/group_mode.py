from pyrogram import Client
from pyrogram.types import CallbackQuery

from utils.group_mode import validate_user_status
import DB
from utils.send_exceptions import send_exception_to_support

# callback #mode
async def set_mode_to_db(client: Client, callback_query: CallbackQuery, data: list):
    """when admin clicks on (slow, fast, normal)(inline_keybaord) this function will run"""
    chat_id = int(data[2])
    if not await validate_user_status(chat_id=chat_id, user_id=callback_query.from_user.id, client=client):
        return await callback_query.answer('admin nisti', show_alert=True)

    current_group_mode: int = DB.showgpmode(chat_id)
    user_choosen_mode = int(data[1])

    if user_choosen_mode == current_group_mode:
        return await callback_query.answer('this mode is currently set', show_alert=True)

    try:
        DB.setnewmode(chat_id, user_choosen_mode)
        await callback_query.answer('new mode has been set', show_alert=True)
    except Exception as e:
        await callback_query.answer('be error barkhord kardim', show_alert=True)
        await send_exception_to_support(client, str(e))

