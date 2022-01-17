def get_count(sentence):
    vowels = []
    for i in sentence:
        if i in "aeiouAEIOU":
            vowels.append(i)
    return len(vowels)


# Best Practices
def get_count(sentence):
    return sum(1 for i in sentence if i in "aeiouAEIOU")
