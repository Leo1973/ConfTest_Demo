#coding:utf-8
import xmlparser
class group_info:
    def __init__(self):
        self.group_num = 0
        self.service_set = []
    def set_num(self, num):
        self.group_num = num
    def allinclude(self):
        for node in xmlparser.getallnode():
            self.service_set.append(node)
    def include(self, node):
        self.service_set.append(node)
    def exclude(self, node):
        self.service_set.remove(node)

def getfile():
    gpfile = open("groupinfo",'r')
    gpfileread = []
    line = gpfile.readline()
    while(line[0] != '#' and line != None):
        gpfileread.append(line)
        line = gpfile.readline()
    return gpfileread
def chose_todo(s_line):
    if "group" in s_line:
        global group_num = int(s_line.split('=')[1])
        new_gi = group_info()
        new_gi.group_num = group_num
        return new_gi
def assign_group_info(l_getfile):
    l_group_info = []
    group_num = 0
    while(l_getfile):
        line = l_getfile.pop(0)
        chose_todo(line)