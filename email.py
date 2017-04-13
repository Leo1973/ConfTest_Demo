def assemble(Seq):
    emailstr = ""
    for i in Seq:
        emailstr += i
    return emailstr
def init(Value):
    unit = Value.split("@")
    seq = [unit[0], '@', unit[1]]
    err1 = list(seq)
    err2 = list(seq)
    err3 = list(seq)
    err4 = list(seq)
    err1[0] = "!@#$%^&*()"
    err2[1] = "#"
    err3[2] = ".."
    err4.pop()
    returnlist = []
    for err in [err1, err2, err3, err4]:
        returnlist.append(assemble(err))
    return returnlist

#print init("liwang2015@nudt.edu.cn")


