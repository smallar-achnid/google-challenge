def foo(x):
	
	def bar(x, counter):
		temp = 1
		if len(str(x)) == 1:
			return counter
		else:
			for i in str(x):
				temp = int(i) * temp
			counter += 1
			return bar(temp, counter)
	return bar(x, 0)

print (foo(77))

def foobar(varRealable):
	start = 0
	#done = False
	while True:
		if foo(start) == varRealable:
			return start
		else:
			start +=1

print (foobar(5))