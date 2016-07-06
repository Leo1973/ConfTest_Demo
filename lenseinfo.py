import utils
import xmlparser
conf_path = {"Yum":"/etc/yum.conf"
            }

def get_entry_info(lense):
    root = xmlparser.parsexml("lenseinfo/"+lense+".xml")
    allnode = xmlparser.getallnode(root)
    l_entry_attrib = xmlparser.getattrib(allnode)[0]
    return l_entry_attrib
def get_section_info(lense):
    root = xmlparser.parsexml("lenseinfo/"+lense+".xml")
    allnode = xmlparser.getallnode(root)
    l_section_attrib = xmlparser.getattrib(allnode)[1]
    return l_section_attrib
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
