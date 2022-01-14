def abbrev_name(name):
    name_list = name.split()
    return (name_list[0][:1].upper() + "." + name_list[1][:1].upper())


# Best Practices
def abbrevName(name):
    return '.'.join(w[0] for w in name.split()).upper()
