from DB import CheckGroupReg,RegisterGroup

async def Handleregister(message):
    chatid = message.chat.id
    if CheckGroupReg(chatid):
        await message.reply("""📋 | گروه شما قبلا ثبت شده ! من همچنان درحال یادگیری حرفاتونم ! 
📖 | اطلاعات بیشتر و راهنمای دستوراتم در ⤺
CMD | /help""")
    else:
        if str(message.chat.type) == "ChatType.SUPERGROUP":
            RegisterGroup(chatid,message.chat.title)
            await message.reply("""✅ | این گروه با موفقیت ثبت شد و من از همین الان درحال یادگیری نحوه حرف زدن تو گروهتونم . . .
🤡 | درواقع من هر لحظه درحال یادگیری هستم و گاهی کلماتی که قبلا شما گفتین رو با هم ترکیب میکنم و میگم ( بعضی وقتا جمله های جالبی میسازم 👐🏿 )

⚒ | به هر حال برای اطالاعات بیشتر از نحوه کارکردم و تنظیم کردنم پیشنهاد میکنم یه سر به دفترچه راهنمام بزنی ⤺
CMD | /help""")
        else:
            await message.reply("""‼️ | گروه شما در ربات ثبت نشد چون گروه شما در حال حاضر یک گروه معمولی است ! 
—-> لطفا پس از اطمینان از تبدیل نوع گروهتون به 'سوپرگروه' از دستور زیر برای ثبت استفاده کنید ⤺
CMD | /register""")