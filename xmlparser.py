#coding:utf-8

import xml.etree.ElementTree as ET
import sys
def parsexml(path):
    root = None
    try: 
        tree = ET.parse(path)     #打开xml文档 
        #root = ET.fromstring(country_string) #从字符串传递xml 
        root = tree.getroot()         #获得root节点  
        return root
    except Exception, e: 
        print "Error:cannot parse file:"+path
    #print root.tag
    #for i in root:
        #print i.tag
def getallnode(root):
    l_allnode = []
    for node in root.getiterator():
        if node.getchildren() == []:
            l_allnode.append(node)
    return l_allnode
def getattrib(l_allnode):#0 for entry 1 for section
    l_entry_attrib = []
    l_section_attrib = []
    for node in l_allnode:
        if "Entry" in node.tag:
            l_entry_attrib.append(node.attrib)
        elif "Section" in node.tag:
            l_section_attrib.append(node.attrib)
    return l_entry_attrib, l_section_attrib

