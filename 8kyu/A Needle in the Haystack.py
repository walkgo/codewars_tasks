def find_needle(haystack):
    return 'found the needle at position ' + str(haystack.index('needle'))


# Best Practices
def find_needle(haystack): 
    return 'found the needle at position %d' % haystack.index('needle')
