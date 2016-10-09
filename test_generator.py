import lenseinfo
import tester
import os
confs = "newconf/"

def getnewconf(path):
    return os.listdir(path)




def init(lense):
    c_lenseinfo = lenseinfo.init(lense)
    directory = confs + c_lenseinfo.name + '/'
    new_conf = getnewconf(directory)
    for name in new_conf:
        tester.init(name, confs, c_lenseinfo)

