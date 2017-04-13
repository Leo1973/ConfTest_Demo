import re
"""
pattern = re.compile(r'he&')
match = pattern.match('he') 
print match
print match.group()
"""
mapping = {
    "path_abs" : r'/[^/.]+(/[^/]+)*/?$',
    "path_rel" : r'[^/.]+(/[^/]+)*/?$',
    "address_url" : r'^((http|https|ftp)\://)?([a-zA-Z0-9\.\-]+(\:[a-zA-Z0-9\.&amp,%\$\-]+)*@)?((25[0-5]|2[0-4][0-9]|[0-1]{1}[0-9]{2}|[1-9]{1}[0-9]{1}|[1-9])\.(25[0-5]|2[0-4][0-9]|[0-1]{1}[0-9]{2}|[1-9]{1}[0-9]{1}|[1-9]|0)\.(25[0-5]|2[0-4][0-9]|[0-1]{1}[0-9]{2}|[1-9]{1}[0-9]{1}|[1-9]|0)\.(25[0-5]|2[0-4][0-9]|[0-1]{1}[0-9]{2}|[1-9]{1}[0-9]{1}|[0-9])|([a-zA-Z0-9\-]+\.)*[a-zA-Z0-9\-]+\.[a-zA-Z]{2,4})(\:[0-9]+)?(/[^/][a-zA-Z0-9\.\,\?\'\\/\+&amp,%\$#\=~_\-@]*)*$',
    "address_email" : r"[\w!#$%&'*+/=?^_`{|}~-]+(?:\.[\w!#$%&'*+/=?^_`{|}~-]+)*@(?:[\w](?:[\w-]*[\w])?\.)*[\w](?:[\w-]*[\w])?",
    "address_ipv4" : r'^((2[0-4]\d|25[0-5]|[01]?\d\d?)\.){3}(2[0-4]\d|25[0-5]|[01]?\d\d?)$',
    "number_port" : r'^([0-9]|[1-9]\d|[1-9]\d{2}|[1-9]\d{3}|[1-5]\d{4}|6[0-4]\d{3}|65[0-4]\d{2}|655[0-2]\d|6553[0-5])$',
    "number_permission" : r'^[0-7]{4}$|^[0-7]{3}$',
    "number" : r'^(-?[1-9][0-9]+|^-?[0-9])(\.[0-9]+)?$',
    "enum_bool" : r'',
    "enum" : r'',
}
        
def IfMatch(Type, arg):
    pattern = re.compile(mapping[Type])
    result = pattern.match(arg)
    return result #None if not match

def GenReg(Type, Constraint):
    global mapping
    if Type == "BOOL":
        if Constraint == "10":
            mapping["enum_bool"] = r"^(1|0)$"
        elif Constraint == "of":
            mapping["enum_bool"] = r"(?i)^(on|off)$"
        elif Constraint == "yn":
            mapping["enum_bool"] = r"(?i)^(yes|no)$"
        elif Constraint == "tf":
            mapping["enum_bool"] = r"(?i)^(true|false)$"
        else:
            print "Error message while genreg: Type:"+Type+" Constraint: "+Constraint
    elif Type == "ENUM":
        mapping["enum"] += "^" + Constraint + "$"
    else:
        print "Unknown Type!"

"""
GenReg("BOOL", "of")
print mapping["enum_bool"]
print re.compile(mapping["enum_bool"]).match("On").group()
GenReg("BOOL", "10")
print mapping["enum_bool"]
print re.compile(mapping["enum_bool"]).match("1").group()
GenReg("BOOL", "yn")
print mapping["enum_bool"]
print re.compile(mapping["enum_bool"]).match("yes").group()
GenReg("BOOL", "tf")
print mapping["enum_bool"]
print re.compile(mapping["enum_bool"]).match("TRUE").group()"""

#print IfMatch("path_rel", "/etc/http.conf")
