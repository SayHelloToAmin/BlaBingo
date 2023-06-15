import mysql.connector

# Connect to MySQL Server :
db = mysql.connector.connect(
    host='localhost',
    user="root",
    password="amin1400",
    database="blabingo",
    # auth_plugin='mysql_native_password'

)

Cursor = db.cursor()

Cursor.execute("update groupss set fastlearning = 0 where fastlearning = 1 ")
db.commit()


# ===================================================check gp registeration=======================================

# this function just check if the chatid are exist in database or not

def CheckGroupReg(chatid):
    Cursor.execute(f"SELECT ID FROM groupss WHERE chatid = {chatid}")
    Cloud = Cursor.fetchone()
    if Cloud is None:
        return False
    else:
        return True


# ============================================Register Group!=========================================================

# this function record the group's information into database

def RegisterGroup(chatid, title):
    try:
        Cursor.execute("INSERT INTO groupss (groupname,chatid) VALUES (%s,%s)", (title, chatid))
        db.commit()
    except:
        pass


# ========================================= enable and disable fast learning =========================================

# this function just change fastleraning mode

def Fastleraning(mode, chatid):
    # if mode is False , turn off fastlearning and if mode is True change it to on
    if mode:
        Cursor.execute("update groupss set fastlearning = %s where chatid = %s", (1, chatid))
        db.commit()
    else:
        Cursor.execute("update groupss set fastlearning = %s where chatid = %s", (0, chatid))
        db.commit()


# ====================================== add message to database =====================================================

# this function will record text message in messages table

def recordmessage(chatid, text,time):
    try:
        Cursor.execute("INSERT INTO messages (chatid,messages,add_time) VALUES (%s,%s,%s)", (chatid, text,time))
        db.commit()
    except:
        print("error")


# ======================================return fastlearning mode=====================================================

# this function will return 0 or 1 as True or False

def isfastlearning(chatid):
    Cursor.execute(f"SELECT fastlearning FROM groupss WHERE chatid = {chatid}")
    Cloud = Cursor.fetchone()
    Cloud = Cloud[0]
    if Cloud:
        return True
    else:
        return False


# =========================================== group mode reciver ======================================================

# this function just return a number [1.2.3]

def showgpmode(chatid):
    Cursor.execute(f"SELECT choosenmode FROM groupss WHERE chatid = {chatid}")
    Cloud = Cursor.fetchone()
    Cloud = Cloud[0]
    return Cloud

# =========================================== chosenmode setter =======================================================

# this function will set a new number for choosenmode param

def setnewmode(chatid,newmode:int):
    Cursor.execute("update groupss set choosenmode = %s where chatid = %s", (newmode, chatid))
    db.commit()
    
    
    
# =============================================== take messages from database =========================================

# this function will return some lists inside of a tuple 

def messagetaker(chatid,limit):
    Cursor.execute("SELECT messages FROM messages where chatid = %s ORDER BY RAND() LIMIT %s",(chatid,limit))
    Cloud = Cursor.fetchall()
    return Cloud