import json
import time
import uuid


def uuidget():
    return str(uuid.uuid1())+'-'+str(uuid.uuid4())

def jsonpull(json_1):
    a = json.dumps(json_1)
    return a

def jsonget(json_1):
    a = json.loads(json_1)
    return a

def get_time():
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())