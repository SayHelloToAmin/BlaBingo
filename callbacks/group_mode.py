from pyrogram import Client
from pyrogram.types import CallbackQuery

from commands.mode import validate_user_status


# callback #mode
async def set_mode_to_db(client: Client, callback_query: CallbackQuery, data: list):
    """when admin clicks on (slow, fast, normal) this function will run"""
    if not await validate_user_status(chat_id=data[2], user_id=callback_query.from_user.id, client=client):
        return await callback_query.answer('admin nisti', show_alert=True)

    current_group_mode = '1'
    if data[1] == current_group_mode:
        await callback_query.answer('this mode is currently set', show_alert=True)

    # Run database method here to store it => data[1]: mode
    await callback_query.answer('new mode has been set', show_alert=True)
