def disemvowel(string):
    consonant  = []
    for i in string:
        if i not in "aeiouAEIOU":
            consonant .append(i)
    return ''.join(consonant)


# Best Practices
def disemvowel(string):
    return "".join(i for i in string if i.lower() not in "aeiou")
