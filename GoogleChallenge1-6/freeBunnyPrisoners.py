import math
def nCr(n,r):
	combinations = int(math.factorial(n)/(math.factorial(r)*math.factorial(n-r)))
	return combinations

def incr(current, max):
	delta = len(current) - 1
	while delta >= 0:
		if delta == len(current) - 1:
			if current[delta] < max - 1:
				current[delta] = current[delta] + 1
				return current
			else:
				delta -= 1	
		else:
			if current[delta] < current[delta+1] - 1:
				current[delta] += 1
				for i in range(delta + 1, len(current)):
					current[i] = current[i-1]+1
				return current	
			else:
				delta = delta - 1

def answer(num_buns, num_required) :
	n = num_buns
	r = num_required - 1
	keys_needed = nCr(n , r)
	total = [range(keys_needed) for i in range(n)]
	counting_list = range(r)
	
	for i in range(keys_needed, 0, -1):
		for j in range(r):
			list(total[counting_list[j]]).remove(i-1)
		counting_list = incr(counting_list, n)
	return total


print(answer(7,5))