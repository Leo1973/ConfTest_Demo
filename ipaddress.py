def assemble(Seq):
    ipstr = ""
    for i in Seq:
        ipstr += i
    return ipstr
def init(Value):
    numls = Value.split(".")
    seq = [numls[0], '.', numls[1], '.' , numls[2], '.', numls[3]]
    err1 = list(seq)
    err1[0] = "-1"
    err2 = list(seq)
    err2[0] = "256"
    err3 = list(seq)
    err3[0] = "o"
    err4 = list(seq)
    err4.pop()
    err5 = list(seq)
    err5[1] = ","
    returnlist = []
    for err in [err1, err2, err3, err4, err5]:
        returnlist.append(assemble(err))
    return returnlist
 
