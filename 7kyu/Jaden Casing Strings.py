import re

def to_jaden_case(s): 
    return re.sub(r"[A-Za-z]+('[A-Za-z]+)?", 
    lambda mo: mo.group(0)[0].upper() + 
    mo.group(0)[1:].lower(), 
    s)


# Best Practices
def toJadenCase(string):        
    return " ".join(w.capitalize() for w in string.split())