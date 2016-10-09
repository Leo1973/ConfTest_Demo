def readfile(filepath):
    fp = open(filepath, 'r')
    fileread = fp.read()
    fp.close()
    return fileread

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
    logfp.close()
    tgfp.close()

