infile = open("input/in12_real.txt","r")
# infile = open("input/in12_test.txt","r")
# infile = open("input/in12_test2.txt","r")
# infile = open("input/in12_test3.txt","r")
L = [line.strip().split('-') for line in infile]

def find_paths1(L,pos,visited,ind):
	if pos == 'end':
		return 1
	else:
		if visited[ind[pos]] == 0:
			visited[ind[pos]] = 1
		elif visited[ind[pos]] == 1:
			return 0
		npaths = 0
		for p,q in L:
			if q == pos:
				npaths += find_paths1(L,p,visited[:],ind)
			elif p == pos:
				npaths += find_paths1(L,q,visited[:],ind)
	return npaths

def day12_part1(L):
	ind = {s: i for i,s in enumerate(set([s for p in L for s in p]))}
	visited = [0 if s.islower() else None for s in ind.keys()]
	return find_paths1(L,'start',visited,ind)


def find_paths1_OG(L,npaths,pos,visited):
	if pos == 'end':
		npaths[0] += 1
	else:
		if visited[pos] == 0:
			visited[pos] = 1
		elif visited[pos] == 1:
			return
		for pos in [p for p,q in L if q == pos] + [q for p,q in L if p == pos]:
			find_paths1_OG(L,npaths,pos,visited.copy())

def day12_part1_OG(L):
	visited = {s: 0 if s.islower() else None for p in L for s in p}
	npaths = [0]
	find_paths1_OG(L,npaths,'start',visited)
	return npaths[0]


def find_paths2(L,pos,visited,ind):
	if pos == 'end':
		return 1
	else:
		if visited[ind[pos]] == 0:
			visited[ind[pos]] = 1
		elif visited[ind[pos]] == 1:
			if pos == 'start' or len([i for i in visited if i==2]):
				return 0
			else:
				visited[ind[pos]] = 2
		elif visited[ind[pos]] == 2:
			return 0
		npaths = 0
		for p,q in L:
			if q == pos:
				npaths += find_paths2(L,p,visited[:],ind)
			elif p == pos:
				npaths += find_paths2(L,q,visited[:],ind)
	return npaths

def day12_part2(L):
	ind = {s: i for i,s in enumerate(set([s for p in L for s in p]))}
	visited = [0 if s.islower() else None for s in ind.keys()]
	return find_paths2(L,'start',visited,ind)


def find_paths2_OG(L,npaths,pos,visited,extra_done):
	if pos == 'end':
		npaths[0] += 1
	else:
		if visited[pos] == 0:
			visited[pos] = 1
		elif visited[pos] == 1:
			if extra_done or pos == 'start':
				return
			else:
				extra_done = 1
		for pos in [p for p,q in L if q == pos] + [q for p,q in L if p == pos]:
			find_paths2_OG(L,npaths,pos,visited.copy(),extra_done)

def day12_part2_OG(L):
	extra_done = 0
	visited = {s: 0 if s.islower() else None for p in L for s in p}
	npaths = [0]
	find_paths2_OG(L,npaths,'start',visited,extra_done)
	return npaths[0]


print(day12_part1(L))
print(day12_part1_OG(L))
print(day12_part2(L))
print(day12_part2_OG(L))