import utils
import shutil
import os
import subprocess
import lenseinfo
import time
log = {
        "MySQL":"/var/log/mariadb/mariadb.log"
        }
newlogs = "newlog/"
newconfs = "newconf/"
def YumScript(spirit_name):
    process = os.popen("yum search hello > ./"+directory_log + spirit_name+" 2>&1")
    #process.wait()
def HttpdScript(spirit_name):
    process = os.popen("systemctl start httpd.service")
    time.sleep(1)
    process = os.popen("systemctl status httpd.service -l >./" + directory_log + spirit_name+" 2>&1")
    time.sleep(1)
    process = os.popen("systemctl stop httpd.service")
    time.sleep(1)
def MySQLScript(spirit_name):
    position = utils.seek2(log[lenseinfo_name])
    process = os.popen("systemctl start mariadb.service")
    time.sleep(5)
    #process = os.popen("systemctl status mariadb.service -l >./" + directory_log + spirit_name+" 2>&1")
    #time.sleep(2)
    process = os.popen("systemctl stop mariadb.service")
    time.sleep(1)
    utils.recordnewlog(log[lenseinfo_name], position, "./"+directory_log + spirit_name)
def confcp2(conf_path, conf):
    shutil.copyfile(conf, conf_path)


runscript = {
                "Yum":YumScript,
                "Httpd":HttpdScript,
                "MySQL":MySQLScript
            }


def init(spirit_name, confs, c_lenseinfo):
    global directory_log, lenseinfo_name 
    directory_log = newlogs + c_lenseinfo.name + "/"
    directory_conf = newconfs + c_lenseinfo.name + "/"
    lenseinfo_name = c_lenseinfo.name
    #print conf_path
    #print conf
    print "now",spirit_name
    confcp2(c_lenseinfo.conf_path, directory_conf + spirit_name)
    runscript[c_lenseinfo.name](spirit_name)

