#coding:utf-8

import xml.etree.ElementTree as ET
import sys
try: 
    tree = ET.parse("mutation.xml")     #打开xml文档 
    #root = ET.fromstring(country_string) #从字符串传递xml 
    root = tree.getroot()         #获得root节点  
except Exception, e: 
    print "Error:cannot parse file:mutation.xml."
#print root.tag
#for i in root:
    #print i.tag
def getallnode():
    ls = ["000","001","010"]
    return ls