import xmlparser
import utils
def getfilename(lense):
    filename = []
    filename.append("lenseinfo/"+lense+".dat")
    filename.append("lenseinfo/"+lense+".xml")
    return filename
def parse(fileread):
    
def store(fileparse):

def init(lense):
    filename = getfilename(lense)
    fileread = utils.readfile(filename[0])
    fileparse = parse(fileread)
    store(fileparse)
