import utils
import spirit_method

name = ""
conf_path = ""
conf_origin = ""
conf_entry_info = []
conf_section_info = []

section_operator = ["[*]",
                    "<*>"]
entry_operator = ["=",
                  " ",
                  " = "]
bool_types = ["10",
              "yn",
              "tf"]
def do1(service):#section_order
    print service
    if conf_section_info.__len__() >= 2:
        strA = conf_section_info[0].origin
        strB = conf_section_info[1].origin
        new_conf = spirit_method.instr_swap(strA, strB,
                                            conf_origin)
        spirit_method.save(new_conf, service, "")
def do2(service):#section_loss
    print service
    #print conf_origin
    for section in conf_section_info:
        #print section.origin
        #print section.origin
        mutation = ""
        new_conf = spirit_method.instr_replace(section.origin, mutation, 
                                                conf_origin)
        #print new_conf
        spirit_method.save(new_conf, service, section.name)
def do3(service):#section_replication
    print service
    for section in conf_section_info:
        mutation = section.origin+'\n'+section.origin
        new_conf = spirit_method.instr_replace(section.origin, mutation, 
                                                conf_origin)
        spirit_method.save(new_conf, service, section.name)


def do4(service):#section_name_typo
    print service
    for section in conf_section_info:
        str_typo = spirit_method.typo(section.name)
        mutation = spirit_method.instr_replace(section.name, str_typo,
                                               section.origin)
        new_conf = spirit_method.instr_replace(section.origin, mutation,
                                                conf_origin)
        spirit_method.save(new_conf, service, section.name)
def do5(service):#section_name_sensitive
    print service
    for section in conf_section_info:
        str_sensitive = spirit_method.sens(section.name)
        mutation = spirit_method.instr_replace(section.name, str_sensitive,
                                               section.origin)
        new_conf = spirit_method.instr_replace(section.origin, mutation,
                                               conf_origin)
        spirit_method.save(new_conf, service, section.name)

def do6(service):#section_name_loss
    print service
    for section in conf_section_info:
        str_loss = ""
        mutation = spirit_method.instr_replace(section.name, str_loss,
                                               section.origin)
        new_conf = spirit_method.instr_replace(section.origin, mutation,
                                               conf_origin)
        spirit_method.save(new_conf, service, section.name)

def do7(service):#section_operator_wrong
    print service
    for section in conf_section_info:
        operator_wrong = spirit_method.chosewrong(section.operator,section_operator)
        mutation = spirit_method.instr_opereplace(section.operator, operator_wrong,
                                               section.origin)
        new_conf = spirit_method.instr_replace(section.origin, mutation,
                                               conf_origin)
        spirit_method.save(new_conf, service, section.name)

def do8(service):#section_operator_loss
    print service
    for section in conf_section_info:
        operator_loss = "*"
        mutation = spirit_method.instr_opereplace(section.operator, operator_loss,
                                                  section.origin)
        new_conf = spirit_method.instr_replace(section.origin, mutation,
                                               conf_origin)
        spirit_method.save(new_conf, service, section.name)

def do9(service):#key_value_pair_order
    print service
    if conf_entry_info.__len__() >= 2:
        strA = conf_entry_info[0].origin
        strB = conf_entry_info[1].origin
        new_conf = spirit_method.instr_swap(strA, strB,
                                            conf_origin)
        spirit_method.save(new_conf, service, "")
def do10(service):#key_value_pair_loss
    print service
    for entry in conf_entry_info:
        mutation = ""
        new_conf = spirit_method.instr_replace(entry.origin, mutation,
                                               conf_origin)
        spirit_method.save(new_conf, service, entry.key)

def do11(service):#key_value_pair_repulication
    print service
    for entry in conf_entry_info:
        mutation = entry.origin+"\n"+entry.origin
        new_conf = spirit_method.instr_replace(entry.origin, mutation,
                                               conf_origin)
        spirit_method.save(new_conf, service, entry.key)

def do12(service):#entry_key_typo
    print service
    for entry in conf_entry_info:
        str_typo = spirit_method.typo(entry.key)
        mutation = spirit_method.instr_replace(entry.key, str_typo,
                                               entry.origin)
        new_conf = spirit_method.instr_replace(entry.origin, mutation,
                                               conf_origin)
        spirit_method.save(new_conf, service, entry.key)
 
def do13(service):#entry_key_sensitive
    print service
    for entry in conf_entry_info:
        str_sensitive = spirit_method.sens(entry.key)
        mutation = spirit_method.instr_replace(entry.key, str_sensitive,
                                               entry.origin)
        new_conf = spirit_method.instr_replace(entry.origin, mutation,
                                               conf_origin)
        spirit_method.save(new_conf, service, entry.key)

def do14(service):#entry_key_loss
    print service
    for entry in conf_entry_info:
        str_loss = ""
        mutation = spirit_method.instr_replace(entry.key, str_loss,
                                               entry.origin)
        new_conf = spirit_method.instr_replace(entry.origin, mutation,
                                               conf_origin)
        spirit_method.save(new_conf, service, entry.key)

def do15(service):#entry_operator_wrong
    print service
    for entry in conf_entry_info:
        operator_wrong = spirit_method.chosewrong(entry.operator, entry_operator)
        mutation = spirit_method.instr_replace(entry.operator, operator_wrong,
                                               entry.origin)
        new_conf = spirit_method.instr_replace(entry.origin, mutation,
                                               conf_origin)
        spirit_method.save(new_conf, service, entry.key)

def do16(service):#entry_operator_space
    print service
    for entry in conf_entry_info:
        operator_space = ' ' + entry.operator + ' '
        mutation = spirit_method.instr_replace(entry.operator, operator_space,
                                               entry.origin)
        new_conf = spirit_method.instr_replace(entry.origin, mutation,
                                               conf_origin)
        spirit_method.save(new_conf, service, entry.key)



def do17(service):#entry_operator_loss
    print service
    for entry in conf_entry_info:
        operator_loss = ""
        mutation = spirit_method.instr_replace(entry.operator, operator_loss,
                                               entry.origin)
        new_conf = spirit_method.instr_replace(entry.origin, mutation,
                                               conf_origin)
        spirit_method.save(new_conf, service, entry.key)

def do18(service):#name_syn
    print service

def do19(service):#name_sem
    print service

def do20(service):#address_syn
    print service

def do21(service):#address_sem
    print service

def do22(service):#MV_syn
    print service

def do23(service):#MV_sem
    print service

def do24(service):#enum_syn
    print service

def do25(service):#enum_sem
    print service

def do26(service):#mail_syn
    print service

def do27(service):#mail_sem
    print service

def do28(service):#number_syn
    print service
    for entry in conf_entry_info:
        if entry.type != "NUMB" :
            continue
        else:
            wrong_num = "thisisatest"
            mutation = spirit_method.instr_replace(entry.value, wrong_num,
                                                   entry.origin)
            new_conf = spirit_method.instr_replace(entry.origin, mutation,
                                                   conf_origin)
            spirit_method.save(new_conf, service, entry.key)

def do29(service):#number_sem
    print service
    for entry in conf_entry_info:
        if entry.type != "NUMB" :
            continue
        else:
            sem_value = []
            constraint = entry.constraint.split()
            num_type = constraint[0]
            num_range = constraint[1]
            num_unit = constraint[2]
            if num_type == "int":
                float_value = str(int(entry.value)+0.5)
                overflow_value = "99999999999999999"
                sem_value.append(float_value)
                sem_value.append(overflow_value)
            if num_range != "none":
                min_num = int(num_range.split(',')[0][1::])
                max_num = int(num_range.split(',')[1][:-1:])
                min_value = str(min_num - 1)
                max_value = str(max_num + 1)
                sem_value.append(min_value)
                sem_value.append(max_value)
            if num_unit != "none":
                print "#TODO"
            mutation = spirit_method.instr_replace(entry.value, sem_value,
                                                   entry.origin)
            new_conf = spirit_method.instr_replace(entry.origin, mutation,
                                                   conf_origin)
            spirit_method.save(new_conf, service, entry.key)

def do30(service):#url_syn
    print service

def do31(service):#url_sem
    print service

def do32(service):#boolean_syn
    print service
    #todo

def do33(service):#boolean_sem
    print service
    for entry in conf_entry_info:
        if entry.type != "BOOL" :
            continue
        else:
            sem_value = []
            if entry.constraint != "10":
                sens_bool = spirit_method.sens(entry.value)
                sem_value.append(sens_bool)
            wrong_bool_type = spirit_method.chosewrong(entry.constraint, bool_types)
            wrong_bool = spirit_method.bool_generate(wrong_bool_type)
            sem_value.append(wrong_bool)
            mutation = spirit_method.instr_replace(entry.value, sem_value,
                                                   entry.origin)
            new_conf = spirit_method.instr_replace(entry.origin, mutation,
                                                   conf_origin)
            spirit_method.save(new_conf, service, entry.key)
            
def do34(service):#port_syn
    print service

def do35(service):#port_sem
    print service

def do36(service):#path_syn
    print service
    for entry in conf_entry_info:
        if entry.type != "PATH" :
            continue
        else:
            value = spirit_method.trans_path(entry.value, entry.constraint)
            syn_value = []
            syn_value.append('\\' + value[1::])
            syn_value = spirit_method.trans_path(syn_value, entry.constraint)
            mutation = spirit_method.instr_replace(entry.value, syn_value,
                                                   entry.origin)
            new_conf = spirit_method.instr_replace(entry.origin, mutation,
                                                   conf_origin)
            spirit_method.save(new_conf, service, entry.key)



def do37(service):#path_sem
    print service
    for entry in conf_entry_info:
        if entry.type != "PATH" :
            continue
        else:
            value = spirit_method.trans_path(entry.value, entry.constraint)
            sem_value = []
            sem_value.append('/abc')
            sem_value.append('/cba/abc')
            sem_value.append('/spirittest')
            sem_value.append('/spirittest/spirit')
            sem_value = spirit_method.trans_path(sem_value, entry.constraint)
            mutation = spirit_method.instr_replace(entry.value, sem_value,
                                                   entry.origin)
            new_conf = spirit_method.instr_replace(entry.origin, mutation,
                                                   conf_origin)
            spirit_method.save(new_conf, service, entry.key)
            

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
    dict_service[service](service)
