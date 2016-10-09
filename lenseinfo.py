import utils
import xmlparser
class make_entry:
    def __init__(self,dic):
        self.key = dic["key"]
        self.value = dic["value"]
        self.origin = dic["origin"]
        self.operator = dic["operator"]
        self.constraint = dic["constraint"]
        self.type = dic["type"]
class make_section:
    def __init__(self,dic):
        self.name = dic["name"]
        self.operator = dic["operator"]
        self.origin = dic["origin"]
conf_path = {"Yum":"/etc/yum.conf",
             "Httpd":"/etc/httpd/conf/httpd.conf",
             "MySQL":"/etc/my.cnf",
             "Redis":"/etc/redis.conf"
            }

def get_entry_info(lense):
    root = xmlparser.parsexml("lenseinfo/"+lense+".xml")
    allnode = xmlparser.getallnode(root)
    l_entry_attrib = xmlparser.getattrib(allnode)[0]
    l_entry_info = []
    if l_entry_attrib[0]:
        for entry_attrib in l_entry_attrib:
            l_entry_info.append(make_entry(entry_attrib))
    return l_entry_info
def get_section_info(lense):
    root = xmlparser.parsexml("lenseinfo/"+lense+".xml")
    allnode = xmlparser.getallnode(root)
    l_section_attrib = xmlparser.getattrib(allnode)[1]
    #print l_section_attrib
    l_section_info = []
    if l_section_attrib[0]:
        for section_attrib in l_section_attrib:
            l_section_info.append(make_section(section_attrib))
    return l_section_info
class c_lenseinfo:
    def __init__(self,lense):
        self.name = lense
        self.conf_path = conf_path[lense]
        self.conf_origin = utils.readfile(self.conf_path)
        self.conf_entry_info = get_entry_info(lense)
        self.conf_section_info = get_section_info(lense)
def init(lense):
    c_lenseinfo_new =  c_lenseinfo(lense)
    return c_lenseinfo_new
