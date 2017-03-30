import utils
import shutil
import os
import subprocess
import lenseinfo
import time
log = {
        "MySQL":"/var/log/mariadb/mariadb.log",
        "Redis":"/var/log/redis.log"
        }
newlogs = "newlog/"
newconfs = "newconf/"
def YumScript(spirit_name):
    process = os.popen("yum search hello > ./tempfile 2>&1")
    #process  = os.popen("yum search hello")
    time.sleep(5)
    return utils.readfile("./tempfile")
    #process.wait()
def HttpdScript(spirit_name):
    process0 = os.popen("systemctl start httpd.service")
    time.sleep(5)
    #process = os.popen("systemctl status httpd.service -l >./" + directory_log + spirit_name+" 2>&1")
    process1 = os.popen("systemctl status httpd.service -l")
    time.sleep(1)
    process2 = os.popen("systemctl stop httpd.service")
    time.sleep(5)
    return process1.read()
def MySQLScript(spirit_name):
    position = utils.seek2(log[lenseinfo_name])
    process = os.popen("systemctl start mariadb.service")
    time.sleep(5)
    #process = os.popen("systemctl status mariadb.service -l >./" + directory_log + spirit_name+" 2>&1")
    #time.sleep(2)
    process = os.popen("systemctl stop mariadb.service")
    time.sleep(1)
    #utils.recordnewlog(log[lenseinfo_name], position, "./"+directory_log + spirit_name)
    logread = utils.getnewlog(log[lenseinfo_name], position)
    return logread
def RedisScript(spirit_name):
    #position = utils.seek2(log[lenseinfo_name])
    process = os.popen("redis-server /etc/redis.conf >  ./tempfile 2>&1")
    #process0 = os.popen("redis-server /etc/redis.conf")
    #print process.read()
    time.sleep(2)
    process1 = os.popen("redis-cli shutdown")
    return utils.readfile("./tempfile")
    #utils.recordnewlog(log[lenseinfo_name], position, "./"+directory_log + spirit_name)
def PostgreSQLScript(spirit_name):
    process0 = os.popen("systemctl start postgresql.service")
    time.sleep(5)
    #process = os.popen("systemctl status httpd.service -l >./" + directory_log + spirit_name+" 2>&1")
    process1 = os.popen("systemctl status postgresql.service -l")
    time.sleep(1)
    process2 = os.popen("systemctl stop postgresql.service")
    time.sleep(1)
    return process1.read()

def confcp2(conf_path, conf):
    shutil.copyfile(conf, conf_path)
    

runscript = {
                "Yum":YumScript,
                "Httpd":HttpdScript,
                "MySQL":MySQLScript,
                "Redis":RedisScript,
                "PostgreSQL":PostgreSQLScript,
            }


def init(spirit_name, confs, c_lenseinfo):
    global lenseinfo_name 
    directory_log = newlogs + c_lenseinfo.name + "/"
    directory_conf = newconfs + c_lenseinfo.name + "/"
    lenseinfo_name = c_lenseinfo.name
    #print conf_path
    #print conf
    print "now",spirit_name
    confcp2(c_lenseinfo.conf_path, directory_conf + spirit_name)
    logread = runscript[c_lenseinfo.name](spirit_name)
    print logread
    if utils.writefile(logread, "./"+directory_log + spirit_name):
        print "succeed!"
