import random
import asyncio

from pyrogram import Client
import aiofiles

import DB
from utils.send_exceptions import send_exception_to_support
from addmessage import group_counts


async def check_time_to_send(client: Client, chat_id: int):
    msg_count = group_counts[chat_id]
    if msg_count > 10:
        if await is_time_to_send(chat_id, msg_count):
            random_messages = DB.messagetaker(chatid=chat_id, limit=random.randint(2, 3))

            choosen_message = await _convert_random_messages(random_messages)
            final_text = await _initial_text_verb(choosen_message)
            await _send_to_group(client, chat_id, final_text)

            group_counts[chat_id] = 0


async def is_time_to_send(chat_id: int, message_count: int) -> bool:
    mode = DB.showgpmode(chat_id)
    if (message_count == 20 and mode == 3) or (message_count == 40 and mode == 2) or (
            message_count == 60 and mode == 1):
        return True
    # chance of sending progress
    if random.randint(1, 5) == 3:
        if mode == 1 and 45 < message_count < 60:
            return True
        elif mode == 2 and 30 < message_count < 40:
            return True
        elif mode == 3 and 10 < message_count < 20:
            return True
    return False


async def _convert_random_messages(random_messages: list) -> str:
    """choose messages from list of tuples of messages that taken from database and add them to one string"""
    choosen_messages = ''
    for messages in random_messages:
        msg = messages[0].split('-')
        max_number_to_choose = random.randint(1, 3) if len(msg) >= 3 else 1
        msg = random.sample(msg, k=max_number_to_choose)
        msg = ' '.join(msg)
        choosen_messages += f'{msg} '
    return choosen_messages


async def _initial_text_verb(sentence: str) -> str:
    """if the word ends with a verb remove it from list and add it to the last of sentence then break the loop"""
    words = sentence.split()
    verb_found = False
    for word in words:
        async with aiofiles.open('verbs.txt', 'r', encoding='utf-8') as file:
            async for verb in file:
                verb = verb.strip('\n')
                if verb == word:
                    words.remove(verb)
                    words.append(verb)
                    verb_found = True
                    break
        if verb_found:
            break
    final_text = ' '.join(words)
    return final_text


async def _send_to_group(client: Client, chat_id: int, text: str):
    try:
        await client.send_message(chat_id, text)
    except Exception as e:
        await send_exception_to_support(client, str(e))
