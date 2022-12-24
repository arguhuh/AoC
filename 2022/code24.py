from math import lcm
from queue import PriorityQueue, Empty
from pyperclip import copy as ctrl_C

def step(B, M, N):
	for b in B:
		match b[2]:
			case '>':
				b[1] = (b[1] + 1) % N
			case '<':
				b[1] = (b[1] - 1) % N
			case 'v':
				b[0] = (b[0] + 1) % M
			case '^':
				b[0] = (b[0] - 1) % M
	return B

Lboth = []
for filename in ["input/in24_test.txt", "input/in24_real.txt"]:
	with open(filename,"r") as infile:
		lines = infile.read().split('\n')
		M = len(lines) - 2
		N = len(lines[0]) - 2
		B = [[i - 1, j - 1, c] for i,line in enumerate(lines) for j,c in enumerate(line) if c not in '.#']
		
		cycle = lcm(M,N)
		occupied = [{(i,j) for i,j,_ in B}] + [{(i,j) for i,j,_ in step(B,M,N)} for _ in range(cycle-1)]
		
		L = occupied, M, N
		Lboth.append(L)
Ltest, Lreal = Lboth

def dijk(occupied, M, N, start, end, d0 = 0):
	cycle = lcm(M,N)
	t0 = d0 % cycle
	
	dist = {}
	dist[(*start, t0)] = d0
	Q = PriorityQueue()
	Q.put((d0, (*start, t0)))
	freedict = {}
	for t in range(cycle):
		freedict[(*start, t)] = True
		freedict[(*end, t)] = True
	while True:
		try:
			d, (i, j, t) = Q.get_nowait()
		except Empty:
			return float('inf')
		if (i, j) == end:
			return d
		freedict[(i, j, t)] = False
		dp = d + 1
		tp = (t + 1) % cycle
		
		neighs = set()
		for pos in [(i, j), (i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
			state = (*pos, tp)
			if state not in freedict:
				freedict[state] = 0 <= state[0] < M and 0 <= state[1] < N \
				and pos not in occupied[tp]
			if freedict[state]:
				neighs.add(state)
		
		for dest in neighs:
			if dest not in dist or dp < dist[dest]:
				dist[dest] = dp
				Q.put((dp, dest))

def day24_part1(occupied, M, N):
	return dijk(occupied, M, N, (-1, 0), (M, N-1))

def day24_part2(occupied, M, N, d0):
	return dijk(occupied, M, N, (-1, 0), (M, N-1), d0 = \
	dijk(occupied, M, N, (M, N-1), (-1, 0), d0 = d0))

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