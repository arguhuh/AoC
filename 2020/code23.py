from itertools import pairwise,chain

def day23_part1(s,N):
	curr_cup = int(str(s)[0]) - 1
	D = [None] * 9
	for p,q in pairwise(map(lambda c: int(c) - 1,str(s))):
		D[p] = q
	D[q] = curr_cup
	
	for _ in range(N):
		if curr_cup:
			destination = curr_cup - 1
		else:
			destination = 8
		test_cup = curr_cup
		test_cups = [(test_cup := D[test_cup]) for _ in range(3)]
		while destination in test_cups:
			if destination:
				destination -= 1
			else:
				destination = 8
		
		next_cup = D[test_cup]
		D[curr_cup] = next_cup
		D[test_cup] = D[destination]
		D[destination] = test_cups[0]
		
		curr_cup = next_cup
	
	test_cup = 0
	return ''.join(str((test_cup := D[test_cup]) + 1) for _ in range(8))

def day23_part2(s):
	Nmax = 1_000_000
	curr_cup = int(str(s)[0]) - 1
	D = [None] * Nmax
	for p,q in pairwise(chain(map(lambda c: int(c) - 1,str(s)),range(9,Nmax))):
		D[p] = q
	D[q] = curr_cup
	
	for _ in range(10_000_000):
		if curr_cup:
			destination = curr_cup - 1
		else:
			destination = Nmax - 1
		test_cup = curr_cup
		test_cups = [(test_cup := D[test_cup]) for _ in range(3)]
		while destination in test_cups:
			if destination:
				destination -= 1
			else:
				destination = Nmax - 1
		
		next_cup = D[test_cup]
		D[curr_cup] = next_cup
		D[test_cup] = D[destination]
		D[destination] = test_cups[0]
		
		curr_cup = next_cup
	
	return (D[0] + 1) * (D[D[0]] + 1)

print(day23_part1(389125467,100)) #test
print(day23_part1(394618527,100)) #real

print(day23_part2(389125467)) #test
print(day23_part2(394618527)) #real