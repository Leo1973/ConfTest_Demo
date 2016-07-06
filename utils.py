def readfile(filepath):
    fp = open(filepath, 'r')
    fileread = fp.read()
    fp.close()
    return fileread

