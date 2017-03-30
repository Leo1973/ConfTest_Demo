import regex

#STEP 1 identify the type

#STEP 2 generate the type-specific misconfigurations

#STEP 3 judge the misconf whether legal

def name_mut(Value):
def address_mut(Value):
def enum_mut(Value):
def mail_mut(Value):
def number_mut(Value):
def url_mut(Value):
def boolean_mut(Value):
def port_mut(Value):
def path_mut(Value):

typemutator = {
    "name" : name_mut,
    "address" : address_mut,
    "enum" : enum_mut,
    "mail" : mail_mut,
    "number" : number_mut,
    "url" : url_mut,
    "boolean" : boolean_mut,
    "port" : port_mut,
    "path" : path_mut
}

def gensyn(Value, Type):

