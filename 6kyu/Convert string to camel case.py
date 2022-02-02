def to_camel_case(text):
    if text == '':
        return ''
    else:
        s = text
        for i in ["_", "-"]:
            if i in s:
                s = s.replace(i," ")
        s = s.title()
        s = s.replace(s[0], text[0])
        s = s.replace(" ", "")
        return(s)


# Best Practices
def to_camel_case(text):
    removed = text.replace('-', ' ').replace('_', ' ').split()
    if len(removed) == 0:
        return ''
    return removed[0]+ ''.join([x.capitalize() for x in removed[1:]])
