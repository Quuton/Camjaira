# Contains miscellaneous functions used by views 
from .modelInterface import *

def parseFloat(number:str):
    try:
        return float(number)
    except:
        return .0

def isUser():
    pass

def isOwner():
    pass