# Contains miscellaneous functions used by views 
from .modelInterface import *

def parseFloat(number:str):
    try:
        return float(number)
    except:
        return .0

def isUser(request):
    return request.user.groups.filter(name='User').exists()

def isOwner(request):
    return request.user.groups.filter(name='Owner').exists()

def isAdmin(request):
    return request.user.is_superuser

def getRelevantAttributes(obj):
    excluded_keys = 'created', '_state', 'timestamp', 'user', 'uid', 'changed'
    filtered = {}
    for i, j in obj.__dict__.items():
        if i not in excluded_keys:
            filtered.update({i:j})
    return filtered
