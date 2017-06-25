def assemble(Seq):
    numberstr = ""
    for s in Seq:
        numberstr += s

    return numberstr

def init(Value, Constraint):
    ls = Constraint.split()
    #print Value
    #print Constraint
    typ = ls[0]
    rang = ls[1]
    unit = ls[2]
    if unit != "none":
        n = Value.split(unit)[0]
        if " " in n:
            seq = [n.split(' ')[0], ' ', unit]
        else:
            seq = [n, unit]
    else:
        seq = [Value]
    min_value = str(-9999999999)
    max_value = str(9999999999)
    if rang != "none":
        min_num = int(rang.split(',')[0][1::])
        max_num = int(rang.split(',')[1][:-1:])
        min_value = str(min_num - 1)
        max_value = str(max_num + 1)
    err1 = list(seq)
    err1[0] += ".5"
    err2 = list(seq)
    err2[0] = min_value
    err3 = list(seq)
    err3[0] = max_value
    err4 = list(seq)
    err4[0] = "abc"
    err5 = list(seq)
    err5.append("wrong")
    returnlist = []
    for err in [err1, err2, err3, err4, err5]:
        returnlist.append(assemble(err))
    return returnlist
"""
print init("16kb", "int [1,16] kb")

print init("16", "int [1,16] none")
print init("16kb", "int none kb")
print init("16", "int none none")
"""
