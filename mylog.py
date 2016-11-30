ID = 0
class log:
    def __init__(self, TARGET, OPERATOR, RESULT ,CONFFILE, LOGFILE):
        self.ID = self.getID()
        self.target = TARGET 
        self.operator = OPERATOR
        self.result = RESULT
        self.conffile = CONFFILE     
        self.logfile = LOGFILE
        self.dolog()
    def getID(self):
        global ID
        ID += 1
        return ID
    def dolog(self):
        if type(self.result)==list:
            newstr = "["
            for element in self.result:
                newstr += element + ','
            newstr += ']'
            self.result = newstr
        fp = open("newlog/runtimelog",'a')
        No = '['+str(self.ID)+']: '
        target = "TARGET:<t>"+self.target+"</t> "
        operator = "OPERATOR:<o>"+self.operator+"</o> "
        result = "RESULT:<r>"+self.result+"</r> "
        conffile = "CONFFILE:<c>"+self.conffile+"</c> "
        logfile = "LOGFILE:<l>"+self.logfile+"</l> "
        line = No+target+operator+result+conffile+logfile+'\n'
        fp.write(line)
        fp.close()

