from pyrogram import Client

SUPPORT_GP: int = -1001452929879


async def send_exception_to_support(client: Client, msg: str) -> None:
    try:
        await client.send_message(SUPPORT_GP, msg)
    except Exception as e:
        print('unknown error at utils.send_exceptions')
