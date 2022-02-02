import string


def alphabet_position(text):
    text = text.lower()
    for i in ["'", " ", "."]:
        if i in text:
            text = text.replace(i,"")
    lst = []
    if text.isalpha() == True:
        for i in text:
            lst.append(string.ascii_lowercase.index(i) + 1)
        return(" ".join(map(str,lst)))
    else:
        return ""


# Best Practices
def alphabet_position(text):
    return ' '.join(str(ord(c) - 96) for c in text.lower() if c.isalpha())
