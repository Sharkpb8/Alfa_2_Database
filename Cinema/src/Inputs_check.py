import re
from datetime import datetime

def StringCheck(value,lenght,specialchar = None):
    if(len(value)>lenght):
        return False
    if(not re.findall(r"^[A-Za-z0-9]*$",value)):
        return False
    if(specialchar and re.findall(f"{specialchar}",value)):
        return False
    return True

def NumberCheck(value,lenght,specialchar = None):
    if(len(value)>lenght):
        return False
    if(not re.findall(r"^[0-9]*$",value)):
        return False
    if specialchar and re.search(re.escape(specialchar), value):
        return False
    return True

def DateCheck(value,specialchar = "-"):
    date_format="%Y-%m-%d"
    date_format = date_format.replace("-", specialchar)
    try:
        datetime.strptime(value, date_format)
    except ValueError:
        return False
    else:
        return True
    
def BoolCheck(value,true):
    if value == true:
        return True
    else:
        return False

def EnumCheck(value,enum):
    if(value in enum):
        return True
    else:
        return False
    
def TimeCheck(value):
    try:
        datetime.strptime(value, "%H:%M:%S")
    except ValueError:
        return False
    else:
        return True

# print(StringCheck("asdasd54e",50,"/"))
# print(NumberCheck("500505",50,"."))
# print(DateCheck("2024/12/19","/"))
# print(BoolCheck("ano","ano"))
# print(EnumCheck("ano",["ano","ne","mozna"]))
# print(TimeCheck("23:50:50"))