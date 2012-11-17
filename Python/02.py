#Project Euler #2

def problemTwo():
	previous = 1
	current = 2
	sum = 2
	while (current < 4000000):
		next = previous + current
		previous = current
		current = next
		if (current % 2 == 0):
			sum += current
	return sum
	
print(problemTwo())
		