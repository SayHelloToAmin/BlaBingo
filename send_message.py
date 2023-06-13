import random

from pyrogram import Client

from addmessage import group_counts
import DB
from utils.send_exceptions import send_exception_to_support


VERBS = ['یم', 'م', 'ه']


async def check_time_to_send(client: Client):
    """
    check group_counts dict if the count of messages that sent by a group
     exceed minimum requirment, send random messages
     """
    print('check time to send')
    for chat_id, msg_count in group_counts.items():
        if msg_count >= 1:
            if await is_time_to_send(chat_id):
                random_messages = DB.messagetaker(chatid=chat_id, limit=random.randint(3, 5))

                choosen_message = await _convert_random_messages(random_messages)
                final_text = await _initial_text_verb(choosen_message)
                await _send_to_group(client, chat_id, final_text)

                group_counts[chat_id] = 0


async def is_time_to_send(chat_id: int) -> bool:
    """if message count of a group exceed its minium this function will check group mode(slow, normal, fast)"""
    return True


async def _convert_random_messages(random_messages: list) -> str:
    """choose messages from list of tuples of messages that taken from database and add them to one string"""
    choosen_messages = str()
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
        for verb in VERBS:
            if word.endswith(verb):
                deleted_verb = words.pop(words.index(word))
                words.append(deleted_verb)
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
