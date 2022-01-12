# words = "one hell fight"
# splitwords = words.split(sep=None, maxsplit=-1)
# for i in splitwords:
# 	if len(i) > 4:
# 		print(i)


def spin_words(sentence):
	my_list = sentence.split(sep=None, maxsplit=-1)
	for index, elem in enumerate(my_list):
		if len(elem) >= 5:
			my_list[index] = elem[::-1]	
	print(" ".join(my_list))


spin_words("Hey fellow warriors")
# my_list = ['hello', 'world', 'goodbye', 'world']

# for index, elem in enumerate(my_list):
#     if len(elem) > 5:
#         my_list[index] = elem[::-1]

# print(my_list)
# print(" ".join(my_list))
