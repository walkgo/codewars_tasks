def get_middle(s):
    a = (int(len(s) / 2))
    if (len(s) % 2) != 0:
        return(s[a])
    else:
        return(s[a-1:a+1])


# Best Practices
def get_middle(s):
   return s[(len(s)-1)/2:len(s)/2+1]
