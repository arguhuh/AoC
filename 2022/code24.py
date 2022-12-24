from math import lcm
from queue import Queue, PriorityQueue, Empty
from pyperclip import copy as ctrl_C

Lboth = []
for filename in ["input/in24_test.txt", "input/in24_real.txt"]:
	with open(filename,"r") as infile:
		lines = infile.read().split('\n')
		M = len(lines) - 2
		N = len(lines[0]) - 2
		B = [[i - 1, j - 1, c] for i,line in enumerate(lines) for j,c in enumerate(line) if c not in '.#']
		L = B, M, N
		Lboth.append(L)
Ltest, Lreal = Lboth

def dijk(B, M, N, start, end, d0 = 0):
	cycle = lcm(M,N)
	t0 = d0 % cycle
	
	max_MD = -1
	dist = {}
	dist[(*start, t0)] = d0
	Q = PriorityQueue()
	Q.put((d0, (*start, t0)))
	freedict = {}
	while True:
		try:
			d, (i, j, t) = Q.get_nowait()
			if abs(i-start[0]) + abs(j-start[1]) > max_MD:
				max_MD = abs(i-start[0]) + abs(j-start[1])
				print(i, j, d)
		except Empty:
			return float('inf')
		if (i, j) == end:
			return d
		freedict[(i, j, t)] = False
		dp = d + 1
		tp = (t + 1) % cycle
		
		neighs = set()
		
		state = (i, j, tp)
		if state not in freedict:
			freedict[state] = is_free(*state, B, M, N, cycle)
		if freedict[state]:
			neighs.add(state)
		
		state = (i+1, j, tp)
		if state not in freedict:
			freedict[state] = is_free(*state, B, M, N, cycle)
		if freedict[state]:
			neighs.add(state)
		
		state = (i-1, j, tp)
		if state not in freedict:
			freedict[state] = is_free(*state, B, M, N, cycle)
		if freedict[state]:
			neighs.add(state)
		
		state = (i, j+1, tp)
		if state not in freedict:
			freedict[state] = is_free(*state, B, M, N, cycle)
		if freedict[state]:
			neighs.add(state)
		
		state = (i, j-1, tp)
		if state not in freedict:
			freedict[state] = is_free(*state, B, M, N, cycle)
		if freedict[state]:
			neighs.add(state)
		
		for dest in neighs:
			if dest not in dist or dp < dist[dest]:
				dist[dest] = dp
				Q.put((dp, dest))

def is_free(i, j, t, B, M, N, cycle):
	if (i, j) in [(-1, 0), (M, N-1)]:
		return True
	elif not (0 <= i < M and 0 <= j < N):
		return False
	else:
		return not ( [(i - t) % M, j, 'v'] in B or [(i + t) % M, j, '^'] in B \
		or [i, (j - t) % N, '>'] in B or [i, (j + t) % N, '<'] in B )

def day24_part1(B, M, N):
	return dijk(B, M, N, (-1, 0), (M, N-1))

def day24_part2(B, M, N, d0):
	return dijk(B, M, N, (-1, 0), (M, N-1), d0 = \
	dijk(B, M, N, (M, N-1), (-1, 0), d0 = d0))

result_test_1 = day24_part1(*Ltest)
result_real_1 = day24_part1(*Lreal)

print(result_real_1)
print(result_test_1)
try:
	ctrl_C(result_real_1)
except:
	print("cannot copy result")

result_test_2 = day24_part2(*Ltest, result_test_1)
result_real_2 = day24_part2(*Lreal, result_real_1)

if result_test_2 is not None:
	print()
	print(result_real_2)
	print(result_test_2)
	try:
		ctrl_C(result_real_2)
	except:
		print("cannot copy result")