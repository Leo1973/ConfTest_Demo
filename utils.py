def readfile(filepath):
    fp = open(filepath, 'r')
    fileread = fp.read()
    fp.close()
    return fileread

def writefile(load, filepath):
    fp = open(filepath, 'w')
    fp.write(load)
    return fp.close()
def seek2(filepath):
    fp = open(filepath, 'r')
    fp.seek(0, 2)
    position =  fp.tell()
    fp.close()
    return position

def recordnewlog(logpath, position, tgpath):
    logfp = open(logpath, 'r')
    logfp.seek(position)
    fileread = logfp.read()
    tgfp = open(tgpath, 'w')
    tgfp.write(fileread)
    return logfp.close() and tgfp.close()

def getnewlog(logpath, position):
    logfp = open(logpath, 'r')
    logfp.seek(position)
    fileread = logfp.read()
    return fileread
