def answer(h, q):
	parent_list = []
	
	for value in q:
		found = False
		parent = 2**h - 1
		if value >= parent:
			parent_list.append(-1)
			found = True
		g = h
		while found == False:
			if value == (parent - 2**(g - 1)) or value == parent - 1:
				parent_list.append(parent)
				found = True
			elif value < (parent - 2**(g - 1)):
				parent = (parent - 2**(g - 1))
			else:
				parent = parent - 1
			g = g - 1
	return parent_list


print(answer(5, [10, 6, 300]))
