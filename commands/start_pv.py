from pyrogram import Client
from pyrogram.types import Message

from commands.mode import set_mode_type_pv

extra_commands = {
    'mode': set_mode_type_pv
}

# command /start => this function will run first
async def handle_start_command(client: Client, message: Message, text):
    """if len command is bigger than '2' another function will run to handle extra argument"""
    command = text[1].split('-', maxsplit=1)  # example: ['mode', 'chatid']

    if len(command) >= 2:
        try:
            await extra_commands[command[0]](client, message, extra_args=command[1])  # extra function for start command handles here
        except KeyError:
            pass

    else:
        await start_command(client, message)  # run normal start commands


async def start_command(client: Client, message: Message):
    """normal function start command"""
    await message.reply('welcome')
