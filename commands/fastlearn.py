import time
from DB import Fastleraning

currentfastlearning = {}


async def enablefastlearning(client, message):
    chatid = message.chat.id
    if chatid in currentfastlearning.keys():
        await message.reply(
            f"⏳ | درحال حاضر FastLearning برای این گروه فعاله و {round((5400 - (time.time() - currentfastlearning[chatid])) / 60)} دقیقه دیگه غیرفعال میشه !")
    else:
        currentfastlearning[chatid] = time.time()
        Fastleraning(True, chatid)
        await message.reply("""⏱ | از همین حالا **یادگیری سریع 'FastLearning'** فعال و تا 90 دقیقه ادامه داره ! 
📥 | تو این مدت پیام هاتون رو سریعتر یاد میگیرم!""")


async def checkfastlearning(client):
    global currentfastlearning
    Cloud = []
    if currentfastlearning:
        for ke, val in currentfastlearning.items():
            if (time.time() - val) >= 5400:
                Fastleraning(False, ke)
                Cloud.append(ke)
                await client.send_message(ke, """⌛️ | حالت **یادگیری سریع 'FastLearning'** از همین لحظه غیر فعال شد و ربات به حالت عادی برگشت!
☑️ | برای فعال کردن دوباره این حالت میتونین از دستور زیر استفاده کنید ⤺
CMD | /fastlearning""")
        for ids in Cloud:
            del currentfastlearning[ids]
