# -*- coding:utf-8 -*-
import random
directory = "newconf/"
def instr_swap(strA, strB, str_origin):
    if str_origin.count(strA)*str_origin.count(strB)==1 and strA != strB:
        new_str = str_origin.replace(strA, "thisisastrA")
        new_str = new_str.replace(strB, strA)
        new_str = new_str.replace("thisisastrA", strB)
        return new_str
    else:
        return ""
def instr_replace(origin, mutation, str_origin):
    #print conf_origin.count(origin)
    if type(mutation) == str:
        if str_origin.count(origin)==1 and origin != mutation:
            new_str = str_origin.replace(origin, mutation)
            return new_str
        else:
            return ""
    elif type(mutation) == list:
        new_strs = []
        for mut in mutation:
            if str_origin.count(origin)==1 and origin != mut:
                new_str = str_origin.replace(origin, mut)
                new_strs.append(new_str)
            else:
                new_str = ""
                new_strs.append(new_str)
        return new_strs

    else:
        return ""
def instr_opereplace(ope_ori, ope_mut, str_origin):
    opeF = ope_ori.split('*')[0]
    opeL = ope_ori.split('*')[1]
    mid_str = str_origin.split(opeF)[1].split(opeL)[0]
    new_str = ope_mut.replace('*', mid_str)
    return new_str
def save(new_conf, service, origin):
    if type(new_conf) == str:
        if new_conf:
            name = origin+"_"+service
            fp = open(directory+name,'w')
            fp.write(new_conf)
            fp.close()
        else:
            print "invalid"
    elif type(new_conf) == list:
        count = 0
        for conf in new_conf:
            if conf:
                name = origin + "_" + service + "_" + str(count)
                count += 1
                fp = open(directory+name,'w')
                fp.write(conf)
                fp.close()
            else:
                print "invalid"
def typo(string):
    if string.isalpha():
        character_new = chr(ord(string[0])+1)
        str_new = character_new + string[1::]
        return str_new
    else:
        return string

def sens(string):
    if string.isalpha():
        str_new = string.upper()
        return str_new
    else:
        return string

def chosewrong(string, str_list):
    strwrong = random.choice(str_list)
    while (strwrong == string):
        strwrong = random.choice(str_list)
    return strwrong


