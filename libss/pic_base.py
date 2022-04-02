import base64
import pickle



def basepull(based):
    aa = pickle.dumps(based,4)
    aaa = base64.b64encode(aa)
    return aaa


def baseget(based):
    aaa = base64.b64decode(based)
    aa = pickle.loads(aaa)

    return aa
