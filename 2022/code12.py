from queue import PriorityQueue
from pyperclip import copy as ctrl_C
from copy import deepcopy

Lboth = []
for filename in ["input/in12_test.txt", "input/in12_real.txt"]:
	with open(filename,"r") as infile:
		L = list(map(list,infile.read().split('\n')))
		Lboth.append(L)
Ltest, Lreal = Lboth

def dijk(grid,start,crit,neigh,Ni,Nj):
	unvisited = {(i,j) for i in range(Ni) for j in range(Nj)}
	dist = [[float("inf") for _ in range(Nj)] for _ in range(Ni)]
	dist[start[0]][start[1]] = 0
	Q = PriorityQueue()
	Q.put((0,start))
	while len(unvisited) > 0:
		d,(p,q) = Q.get_nowait()
		if crit(grid,p,q):
			return d
		unvisited.remove((p,q))
		neighs = []
		if p > 0 and neigh(grid,p,q,p-1,q) and (p-1,q) in unvisited:
			neighs.append((p-1,q))
		if p < Ni-1 and neigh(grid,p,q,p+1,q) and (p+1,q) in unvisited:
			neighs.append((p+1,q))
		if q > 0 and neigh(grid,p,q,p,q-1) and (p,q-1) in unvisited:
			neighs.append((p,q-1))
		if q < Nj-1 and neigh(grid,p,q,p,q+1) and (p,q+1) in unvisited:
			neighs.append((p,q+1))
		newd = d + 1
		for r,s in neighs:
			if newd < dist[r][s]:
				dist[r][s] = newd
				Q.put((newd,(r,s)))

def day12_part1(L):
	Ni = len(L)
	Nj = len(L[0])
	start = [(i,row.index('S')) for i,row in enumerate(L) if 'S' in row][0]
	L[start[0]][start[1]] = 'a'
	end = [(i,row.index('E')) for i,row in enumerate(L) if 'E' in row][0]
	L[end[0]][end[1]] = 'z'
	return dijk(L, start, lambda _,p,q: (p,q) == end, \
	lambda g,p,q,r,s: ord(g[r][s]) <= ord(g[p][q]) + 1, Ni, Nj)

def day12_part2(L):
	Ni = len(L)
	Nj = len(L[0])
	S = [(i,row.index('S')) for i,row in enumerate(L) if 'S' in row][0]
	L[S[0]][S[1]] = 'a'
	end = [(i,row.index('E')) for i,row in enumerate(L) if 'E' in row][0]
	L[end[0]][end[1]] = 'z'
	return dijk(L, end, lambda g,p,q: g[p][q] == 'a', \
	lambda g,p,q,r,s: ord(g[p][q]) <= ord(g[r][s]) + 1, Ni, Nj)


result_test_1 = day12_part1(deepcopy(Ltest))
result_real_1 = day12_part1(deepcopy(Lreal))

print(result_real_1)
print(result_test_1)
try:
	ctrl_C(result_real_1)
except:
	print("cannot copy result")

result_test_2 = day12_part2(Ltest)
result_real_2 = day12_part2(Lreal)

if result_test_2 is not None:
	print()
	print(result_real_2)
	print(result_test_2)
	try:
		ctrl_C(result_real_2)
	except:
		print("cannot copy result")