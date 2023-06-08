from pyrogram import Client, filters
from pyrogram.types import Message, CallbackQuery
import tgcrypto
# only from commands folder :
from commands.Register import Handleregister
from commands.fastlearn import enablefastlearning, checkfastlearning
from commands.mode import set_mode_type_group
from commands.start_pv import handle_start_command
from callbacks.group_mode import set_mode_to_db

from apscheduler.schedulers.asyncio import AsyncIOScheduler

# only from DataBase file :
import DB
from addmessage import managemessage

scheduler = AsyncIOScheduler()


# bot setup:
app = Client(
    'Reyme',
    api_id=6703845,
    api_hash="3eac821a6d1e0b0e2969ae0ad2f970ea",
    bot_token="6158758706:AAEkCOBbA035j_0Fh6u1cZ4rjryX-k2GOXQ"
)

# commands group dictionary :
commands = {
    "/fastlearning": enablefastlearning,
    "/fastlearning@blabingobot": enablefastlearning,
    "/mode": set_mode_type_group
}

private_commands = {
    '/start': handle_start_command
}

callback_commands = {
    'mode': set_mode_to_db
}


# message handler :
@app.on_message(filters.group & filters.text)
async def TextHandler(client, message):
    text = message.text.lower()
    print(text)
    # check if user has send /register
    if text in ["/register", "/register@blabingobot"]:
        await Handleregister(message)
    else:
        if DB.CheckGroupReg(message.chat.id):
            if text in commands.keys():
                await commands[text](client, message)
            else:
                await managemessage(text, message.chat.id)
        else:
            if text in commands.keys():
                await message.reply("""‼️ | گروه شما همچنان در ربات ثبت نشده است و غیرقابل استفاده میباشد.
📝 | برای ثبت ربات از دستور زیر استفاده کنید ⤺
CMD | /register""")
            else:
                pass


@app.on_message(filters.private)
async def private_handler(client: Client, message: Message):
    text = message.text.split()

    try:
        await private_commands[text[0].lower()](client, message, text)
    except KeyError:
        pass


@app.on_callback_query(group=2)
async def callback_handler(client: Client, callback_query: CallbackQuery):
    data = callback_query.data.split('#')
    try:
        await callback_commands[data[0]](client, callback_query, data)
    except KeyError:
        pass


@app.on_chat_member_updated(filters.group)
async def test(Client, message):
    chatid = message.chat.id
    if message.new_chat_member.user.id == 6158758706:
        if DB.CheckGroupReg(chatid):
            await Client.send_message(chatid, """🙂 | ممنونم که دوباره به گروهتون راهم دادین . . . 
🗑 | اگه میخواین از اول همه چیزو یاد بگیرم و حرفای قبلی رو فراموش کنم از دستور زیر استفاده کنین ⤺
CMD | /formatme""")
        else:
            if str(message.chat.type) == "ChatType.SUPERGROUP":
                DB.RegisterGroup(chatid, message.chat.title)
                await Client.send_message(chatid, """✅ | این گروه با موفقیت ثبت شد و من از همین الان درحال یادگیری نحوه حرف زدن تو گروهتونم . . .
🤡 | درواقع من هر لحظه درحال یادگیری هستم و گاهی کلماتی که قبلا شما گفتین رو با هم ترکیب میکنم و میگم ( بعضی وقتا جمله های جالبی میسازم 👐🏿 )

⚒ | به هر حال برای اطالاعات بیشتر از نحوه کارکردم و تنظیم کردنم پیشنهاد میکنم یه سر به دفترچه راهنمام بزنی ⤺
CMD | /help""")
            else:
                await Client.send_message(chatid, """‼️ | گروه شما در ربات ثبت نشد چون گروه شما در حال حاضر یک گروه معمولی است ! 
—-> لطفا پس از اطمینان از تبدیل نوع گروهتون به 'سوپرگروه' از دستور زیر برای ثبت استفاده کنید ⤺
CMD | /register""")


scheduler.add_job(checkfastlearning, "interval", seconds=20, args=[app])

scheduler.start()
app.run()
