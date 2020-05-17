

def find_multiples(l, position):
	multiples = []
	for item in l[position + 1:]:
	#l[position +1:] means that it will only search for multiples after the current position
		new = l.index(item)
		if item % l[position] == 0 and  position:
			multiples.append(item)
	#print(multiples)
	return len(multiples)

def find_divisors(l, position):
	divisors = []
	for item in l[:position]:
	#l[:position] means that it will only search for divisors before the current position 
		if l[position] % item == 0 and l.index(item) < position:
			divisors.append(item)
	#print (divisors)
	return len(divisors)

def answer(l):
	counter = 0
	position = len(l)-1
	while position >= 2:
		position -= 1
		counter +=  (find_multiples(l, position)*find_divisors(l, position))
	return counter

print (find_multiples ([1,1,1], 1))
print(answer([1,2,4]))