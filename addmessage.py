groupcounts = {
    
}
import re
import random
from DB import recordmessage,isfastlearning
async def managemessage(text,chatid):
    persian_regex_pattern = re.compile('[u0600-u06FFuFB8Au067Eu0686u06AFu200Cu200F]+')
    global groupcounts
    print(groupcounts)
    if chatid in groupcounts.keys():
        groupcounts[chatid] += 1
    else:
        groupcounts[chatid] = 1
        
        
    chanceresult = False
    #check if fast learning was enable
    if isfastlearning(chatid):
        if random.randint(1,10) in [1,2,3,4,5,6,7,8]:
            chanceresult = True
        else:
            pass
    else:
        if random.randint(1,10) in [1,4,6,8,3]:
            chanceresult = True
        else:
            pass
    print(chanceresult)
    if chanceresult:
        text2 = text.split()
        new_list = [word for word in text2 if isinstance(word, str) and not persian_regex_pattern.fullmatch(word)]
        if len(new_list) == 1:
            finaltext = " ".join(new_list)
            recordmessage(chatid,finaltext)
            print(finaltext)
        else:
            new_num = random.randint(1, len(new_list))
            new_list = random.sample(new_list, new_num)
            new_list = [elem for elem in new_list if len(elem) <= 9]
            finaltext = " ".join(new_list)
            output_str = finaltext.replace(' ', '-')
            print(output_str)
            recordmessage(chatid,output_str)
    else:
        pass
    
    
    