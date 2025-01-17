import re
from datetime import datetime
import math

def StringCheck(value,lenght,specialchar = ""):
    if(len(value)>lenght):
        return False
    specialchar = re.escape(specialchar)
    if(not re.findall(rf"^[A-Za-z0-9 áčďéěíňóřšťúůýžÁČĎÉĚÍŇÓŘŠŤÚŮÝŽ{specialchar}]*$",value)):
        return False
    return True

def NumberCheck(value,lenght = math.inf,decimal = True,negative = True):
    if(len(value)>lenght):
        return False
    try:
        float_value = float(value)
        if(not decimal):
            if("." in value):
                raise ValueError
    except ValueError:
        return False
    if(not negative and float(value) <0):
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
    
def BoolCheck(value,true,false):
    if value == true or value == false:
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
        datetime.strptime(value, "%H:%M")
    except ValueError:
        return False
    else:
        return True

# print(StringCheck("asdasd54e",50,"/"))
# print(NumberCheck("-500505.0",50,True,False))
# print(DateCheck("2024/12/19","/"))
# print(BoolCheck("ano","ano"))
# print(EnumCheck("ano",["ano","ne","mozna"]))
# print(TimeCheck("23:50:50"))