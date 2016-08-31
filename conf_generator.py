import service_assembler
import spirit
import lenseinfo

def do_service(c_lenseinfo, service):
    spirit.init(c_lenseinfo, service)
def generate_confs(lense, lstr_service):
    c_lenseinfo = lenseinfo.init(lense)
    for service in lstr_service:
        do_service(c_lenseinfo,service)

def init(lense, group):
    lstr_service = service_assembler.get_group_service(group)

    generate_confs(lense,lstr_service)
