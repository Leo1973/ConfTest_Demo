import util
import spirit_method
name = ""
conf_path = ""
conf_origin = ""
conf_entry_info = []
conf_section_info = []

def do12():
    for entry in conf_entry_info:
        
        #judge typo(entry["key"]) or not
        if spirit_method.cantypo(entry["key"]):
            replace
            
        #if typo:
            #replace(origin,typo)
            #replace origin file and save to target dir
        #else:
            #continue

def do2():
    print conf_entry_info
    print conf_section_info

dict_service = {
                #00X
                "section_order":do1,
                "section_loss":do2,
                "section_replication":do3,
                #01X
                "section_name_typo":do4,
                "section_name_sensitive":do5,
                "section_name_loss":do6,
                #02X
                "section_operator_wrong":do7,
                "section_operator_loss":do8,
                #10X
                "entry_key_value_pair_order":do9,
                "entry_key_value_pair_loss":do10,
                "entry_key_value_pair_replication":do11,
                #11X
                "entry_key_typo":do12,
                "entry_key_sensitive":do13,
                "entry_key_loss":do14,
                #12X
                "entry_operator_wrong":do15,
                "entry_operator_space":do16,
                "entry_operator_loss":do17,
                #13X
                "entry_value_name_syntactic":do18,
                "entry_value_name_semantic":do19,
                "entry_value_address_syntactic":do20,
                "entry_value_address_semantic":do21,
                "entry_value_multi_value_syntactic":do22,
                "entry_value_multi_value_semantic":do23,
                "entry_value_enum_syntactic":do24,
                "entry_value_enum_semantic":do25,
                "entry_value_mail_syntactic":do26,
                "entry_value_mail_semantic":do27,
                "entry_value_number_syntactic":do28,
                "entry_value_number_semantic":do29,
                "entry_value_url_syntactic":do30,
                "entry_value_url_semantic":do31,
                "entry_value_boolean_syntactic":do32,
                "entry_value_boolean_semantic":do33,
                "entry_value_port_syntactic":do34,
                "entry_value_port_semantic":do35,
                "entry_value_path_syntactic":do36,
                "entry_value_path_semantic":do37,
               }

def init(c_lenseinfo, service):
    global name, conf_path, conf_origin, conf_entry_info, conf_section_info    
    name = c_lenseinfo.name
    conf_path = c_lenseinfo.conf_path
    conf_origin = c_lenseinfo.conf_origin
    conf_entry_info = c_lenseinfo.conf_entry_info
    conf_section_info = c_lenseinfo.conf_section_info
    dict_service[service]()
