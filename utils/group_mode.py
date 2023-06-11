from pyrogram import Client
from pyrogram.enums import ChatMemberStatus

ADMIN_STATUS = (ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.OWNER)

async def validate_user_status(chat_id: int, user_id: int, client: Client) -> bool:
    """validate user status to verify be admin"""
    user = await client.get_chat_member(chat_id, user_id)
    if user.status in ADMIN_STATUS:
        return True
    return False
