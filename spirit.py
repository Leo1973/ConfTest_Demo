def do1(lenseinfo):
    print lenseinfo.name
    print lenseinfo.conf_path
def do2(lenseinfo):
    print lenseinfo.conf_entry_info
    print lenseinfo.conf_section_info
dict_service = {"service1":do1,
                "service2":do2}
def init(c_lenseinfo, service):
    dict_service[service](c_lenseinfo)
