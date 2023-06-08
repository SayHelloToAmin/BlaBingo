from pyrogram import Client, filters
import tgcrypto
# only from commands folder :
from commands.Register import Handleregister
from commands.fastlearn import enablefastlearning,checkfastlearning

from apscheduler.schedulers.asyncio import AsyncIOScheduler
scheduler = AsyncIOScheduler()




# only from DataBase file :
import DB
from addmessage import managemessage

# bot setup:
app = Client(
    'Reyme',
    api_id=6703845,
    api_hash="3eac821a6d1e0b0e2969ae0ad2f970ea",
    bot_token="6158758706:AAEkCOBbA035j_0Fh6u1cZ4rjryX-k2GOXQ"
)


# commands dictionary :
comanddict = {
    "/fastlearning" : enablefastlearning,
    "/fastlearning@blabingobot" : enablefastlearning
}






# message handler :
@app.on_message(filters.group & filters.text)
async def TextHandler(client, message):
    text = message.text.lower()
    # check if user has send /register
    if text in ["/register","/register@blabingobot"]:
        await Handleregister(message)
    else:
        if DB.CheckGroupReg(message.chat.id):
            if text in comanddict.keys():
                await comanddict[text](client, message)
            else:
                await managemessage(text,message.chat.id)
        else:
            if text in comanddict.keys():
               await message.reply("""‼️ | گروه شما همچنان در ربات ثبت نشده است و غیرقابل استفاده میباشد.
📝 | برای ثبت ربات از دستور زیر استفاده کنید ⤺
CMD | /register""")
            else:
                pass


























@app.on_chat_member_updated(filters.group)
async def test(Client,message):
    chatid = message.chat.id
    if message.new_chat_member.user.id == 6158758706:
        if DB.CheckGroupReg(chatid):
            await Client.send_message(chatid,"""🙂 | ممنونم که دوباره به گروهتون راهم دادین . . . 
🗑 | اگه میخواین از اول همه چیزو یاد بگیرم و حرفای قبلی رو فراموش کنم از دستور زیر استفاده کنین ⤺
CMD | /formatme""")
        else:
            if str(message.chat.type) == "ChatType.SUPERGROUP":
                DB.RegisterGroup(chatid,message.chat.title)
                await Client.send_message(chatid,"""✅ | این گروه با موفقیت ثبت شد و من از همین الان درحال یادگیری نحوه حرف زدن تو گروهتونم . . .
🤡 | درواقع من هر لحظه درحال یادگیری هستم و گاهی کلماتی که قبلا شما گفتین رو با هم ترکیب میکنم و میگم ( بعضی وقتا جمله های جالبی میسازم 👐🏿 )

⚒ | به هر حال برای اطالاعات بیشتر از نحوه کارکردم و تنظیم کردنم پیشنهاد میکنم یه سر به دفترچه راهنمام بزنی ⤺
CMD | /help""")
            else:
                await Client.send_message(chatid,"""‼️ | گروه شما در ربات ثبت نشد چون گروه شما در حال حاضر یک گروه معمولی است ! 
—-> لطفا پس از اطمینان از تبدیل نوع گروهتون به 'سوپرگروه' از دستور زیر برای ثبت استفاده کنید ⤺
CMD | /register""")


















scheduler.add_job(checkfastlearning, "interval", seconds=20, args=[app])





scheduler.start()
app.run()