import regex
import ipaddress
import email
import url
import boolean
import port
import path_abs
import path_rel
import number
#STEP 1 identify the type

#STEP 2 generate the type-specific misconfigurations

#STEP 3 judge the misconf whether legal

def name_mut(Value, Constraint):
    returnlist = []
    returnlist.extend("testvalue")
    return returnlist
def address_mut(Value, Constraint):
    returnlist = []
    if regex.IfMatch("address_ipv4", Value):
        returnlist.extend(ipaddress.init(Value))
        #do
    else:
        print "mutator.py: wrong address type while access value:", Value
    return returnlist
def enum_mut(Value, Constraint):
    returnlist = []
    regex.GenReg("ENUM", Constraint)
    #if regex.IfMatch("enum", Value):
    returnlist.extend("testvalue")
    #else:
        #print "mutator.py: wrong Enum type while access value:", Value
    return returnlist
def mail_mut(Value, Constraint):
    returnlist = []
    if regex.IfMatch("address_email", Value):
        returnlist.extend(email.init(Value))
    else:
        print "mutator.py: wrong mail type while access value:", Value
    return returnlist
def url_mut(Value, Constraint):
    returnlist = []
    if regex.IfMatch("address_url", Value):
        returnlist.extend(url.init(Value))
    else:
        print "mutator.py: wrong url type while access value:", Value
    return returnlist
def boolean_mut(Value, Constraint):
    returnlist = []
    regex.GenReg("BOOL", Constraint)
    if regex.IfMatch("enum_bool", Value):
        returnlist.extend(boolean.init(Value, Constraint))
    else:
        print "mutator.py: wrong bool type while access value:", Value
    return returnlist
def port_mut(Value, Constraint):
    returnlist = []
    if regex.IfMatch("number_port", Value):
        returnlist.extend(port.init(Value))
    else:
        print "mutator.py: wrong port type while access value:", Value
    return returnlist
def path_mut(Value, Constraint):
    returnlist = []
    if regex.IfMatch("path_abs", Value):
        returnlist.extend(path_abs.init(Value))
    elif regex.IfMatch("path_rel", Value):
        returnlist.extend(path_rel.init(Value))
    else:
        print "mutator.py: wrong path type while access value:", Value
    return returnlist
def number_mut(Value, Constraint):
    returnlist = []
    returnlist.extend(number.init(Value, Constraint))
    return returnlist


typemutator = {
    "NAME" : name_mut,
    "ADDRESS" : address_mut,
    "ENUM" : enum_mut,
    "EMAIL" : mail_mut,
    "NUMB" : number_mut,
    "URL" : url_mut,
    "BOOL" : boolean_mut,
    "PORT" : port_mut,
    "PATH" : path_mut,
}

def gensyn(Value, Type, Constraint):
    return typemutator[Type](Value, Constraint)
