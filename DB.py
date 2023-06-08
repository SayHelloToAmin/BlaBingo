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


#===================================================check gp registeration=======================================

#this function just check if the chatid are exist in database or not

def CheckGroupReg(chatid):
    Cursor.execute(f"SELECT ID FROM groupss WHERE chatid = {chatid}")
    Cloud = Cursor.fetchone()
    if Cloud is None:
        return False
    else:
        return True
    
    



#============================================Register Group!=========================================================

#this function record the group's information into database

def RegisterGroup(chatid,title):
    try:
        Cursor.execute("INSERT INTO groupss (groupname,chatid) VALUES (%s,%s)",(title,chatid))
        db.commit()
    except:
        pass
    


# ========================================= enable and disable fast learning =========================================

#this function just change fastleraning mode

def Fastleraning(mode,chatid):
    
# if mode is False , turn off fastlearning and if mode is True change it to on
    if mode:
        Cursor.execute("update groupss set fastlearning = %s where chatid = %s",(1,chatid))
        db.commit()
    else:
        Cursor.execute("update groupss set fastlearning = %s where chatid = %s",(0,chatid))
        

# ====================================== add message to database =====================================================

# this function will record text message in messages table

def recordmessage(chatid,text):
    try:
        Cursor.execute("INSERT INTO messages (chatid,messages) VALUES (%s,%s)",(chatid,text))
        db.commit()
    except:
        print("error")
        
        
        
# ======================================return fastlearning mode=====================================================

#this function will return 0 or 1 as True or False

def isfastlearning(chatid):
    Cursor.execute(f"SELECT fastlearning FROM groupss WHERE chatid = {chatid}")
    Cloud = Cursor.fetchone()
    Cloud = Cloud[0]
    if Cloud:
        return True
    else:
        return False