def spin_words(sentence):
	list = sentence.split(sep=None, maxsplit=-1)
	for index, elem in enumerate(list):
		if len(elem) >= 5:
			list[index] = elem[::-1]	
	return(" ".join(list))
