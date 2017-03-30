#import lenseinfo_generator
import conf_generator
import test_generator
#import log_checker
import lenseinfo
#get_group_service(group_num)
lense = "PostgreSQL"
group = 1
c_lenseinfo = lenseinfo.init(lense)
#print service_assembler.get_group_service(group)
#lenseinfo_generator.init(lense)
try:
    conf_generator.init(lense,group)

    test_generator.init(lense)
    log_checker.init(lense)
finally:
    fp = open(c_lenseinfo.conf_path, 'w')
    fp.write(c_lenseinfo.conf_origin)
    fp.close()
