def answer (M,F):
	M = int(M)
	F = int (F)
	counter = -1
	while (M > 1) and (F > 1):
		bombs = (M,F)
		counter += int(max(bombs)/min(bombs))
		F = max(bombs) % min(bombs)
		M = min(bombs)
	
	if M < 1 or F < 1:
		return "impossible"
	if M == 1:
		counter += F
	if F == 1:
		counter += M
	return counter

print (answer(53,11))
