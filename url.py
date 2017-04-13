def assemble(Seq):
    urlstr = ""
    for i in Seq:
        urlstr += i
    return urlstr
def init(Value):
    returnlist = []
    if "://" in Value:
        unit = Value.split("://")
        seq = [unit[0], "://", unit[1]]
        err1 = list(seq)
        err1[0] = "unknown"
        err2 = list(seq)
        err2[1] = "::/"
        err3 = list(seq)
        err3[2] = "abcdefg"
        err4 = list(seq)
        err4.pop()
        for err in [err1, err2, err3, err4]:
            returnlist.append(assemble(err))
    else:
        returnlist.append("abcdefg")
        returnlist.append("http://"+Value)
        returnlist.append("unknown://"+Value)

    return returnlist

#print init("http://www.baidu.com")

#print init("www.baidu.com")

