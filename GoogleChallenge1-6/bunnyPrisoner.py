
def answer(x, y):

	position = 1
	for i in range (y):
		position = position + i
	
	for j in range(y+1, y+x):
		position = position + j
	return str(position)

print(answer(5, 3))
print(answer(1, 1))
print(answer(5,10))