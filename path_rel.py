def assemble(Seq):
    pathstr = ""
    for i in Seq:
        pathstr += i
    return pathstr


def init(Value):
    seq = []
    returnlist = []
    while "/" in Value:
        loc = Value.index("/")
        if loc != 0:
            seq.append(Value[0:loc])
            seq.append("/")
            Value = Value[loc+1::]
        else:
            seq.append("/")
            Value = Value[loc+1::]
    if Value:
        seq.append(Value)
    err1 = list(seq)
    err1.insert(0, "\\")
    err2 = list(seq)
    err2.pop(0)
    err3 = list(seq)
    err3[1] = "\\"
    err4 = list(seq)
    err4.pop()
    for err in [err1, err2, err3, err4]:
        returnlist.append(assemble(err))
    return returnlist

