import random,math,itertools

infile = open("input/in09_real.txt","r")
# infile = open("input/in09_test.txt","r")
L = [[int(i) for i in line.strip()] for line in infile] #L[i][j] is j-th height in the i-th line

def day09_part1(L):
	N = len(L[0])
	return sum([sum([t[0]+1 for t in
		zip(C,C[1:]+[float("inf")],[float("inf")]+C[:-1],D,U) if t[0] < min(t[1:])])
		for C,D,U in zip(L,L[1:]+[[float("inf")] * N],[[float("inf")] * N]+L[:-1])])


def walk(L,M,i,j):
	Ni = len(L)
	Nj = len(L[0])
	di = [1, -1, 0, 0]
	dj = [0, 0, 1, -1]
	while not M[i][j]:
		d = random.randint(0,3)
		ii = i+di[d]
		jj = j+dj[d]
		while ii == -1 or jj == -1 or ii == Ni or jj == Nj or L[ii][jj] == 9:
			d = random.randint(0,3)
			ii = i+di[d]
			jj = j+dj[d]
		i = ii
		j = jj
	return (i,j)

def day09_part2(L):
	Ni = len(L)
	Nj = len(L[0])
	M = [[t[0] < min(t[1:]) for t in
		zip(C,C[1:]+[float("inf")],[float("inf")]+C[:-1],D,U)] for C,D,U in
		zip(L,L[1:]+[[float("inf")] * Nj],[[float("inf")] * Nj]+L[:-1])]
		#M[i][j] is true exactly when L[i][j] is a local minimum
	minima = [(i,j) for i,row in enumerate(M) for j,B in enumerate(row) if B]
		#list of minima (i,j)
	Nm = len(minima) #number of minima
	basins = [0] * Nm #initialise each basin with 0 spaces
	for i in range(Ni):
		for j in range(Nj):
			if L[i][j] < 9:
				basins[minima.index(walk(L,M,i,j))] += 1
	return math.prod(sorted(basins)[-3:])


def day09_part2_test(L):
	Ni = len(L)
	Nj = len(L[0])
	M = [[t[0] < min(t[1:]) for t in
		zip(C,C[1:]+[float("inf")],[float("inf")]+C[:-1],D,U)] for C,D,U in
		zip(L,L[1:]+[[float("inf")] * Nj],[[float("inf")] * Nj]+L[:-1])]
		#M[i][j] is true exactly when L[i][j] is a local minimum
	minima = [(i,j) for i,row in enumerate(M) for j,B in enumerate(row) if B]
		#list of minima (i,j)
	Nm = len(minima) #number of minima
	basins = [0] * Nm #initialise each basin with 0 spaces
	di = [1, -1, 0, 0]
	dj = [0, 0, 1, -1]
	for i0 in range(Ni):
		for j in range(Nj):
			i = i0
			if L[i][j] < 9:
				while not M[i][j]:
					d = random.randint(0,3)
					ii = i+di[d]
					jj = j+dj[d]
					while ii == -1 or jj == -1 or ii == Ni or jj == Nj or L[ii][jj] == 9:
						d = random.randint(0,3)
						ii = i+di[d]
						jj = j+dj[d]
					i = ii
					j = jj
				basins[minima.index((i,j))] += 1
	return math.prod(sorted(basins)[-3:])


def day09_part2_test2(L):
	Ni = len(L)
	Nj = len(L[0])
	M = [[t[0] < min(t[1:]) for t in
		zip(C,C[1:]+[float("inf")],[float("inf")]+C[:-1],D,U)] for C,D,U in
		zip(L,L[1:]+[[float("inf")] * Nj],[[float("inf")] * Nj]+L[:-1])]
		#M[i][j] is true exactly when L[i][j] is a local minimum
	minima = [(i,j) for i,row in enumerate(M) for j,B in enumerate(row) if B]
		#list of minima (i,j)
	Nm = len(minima) #number of minima
	basins = [0] * Nm #initialise each basin with 0 spaces
	di = [1, -1, 0, 0]
	dj = [0, 0, 1, -1]
	for i,j in itertools.product(range(Ni),range(Nj)):
		if L[i][j] < 9:
			while not M[i][j]:
				d = random.randint(0,3)
				ii = i+di[d]
				jj = j+dj[d]
				while ii == -1 or jj == -1 or ii == Ni or jj == Nj or L[ii][jj] == 9:
					d = random.randint(0,3)
					ii = i+di[d]
					jj = j+dj[d]
				i = ii
				j = jj
			basins[minima.index((i,j))] += 1
	return math.prod(sorted(basins)[-3:])


def day09_part2_flood(L):
	Ni = len(L)
	Nj = len(L[0])
	minima = [(i,j) for i,(C,D,U) in \
		enumerate(zip(L,L[1:]+[[float("inf")] * Nj],[[float("inf")] * Nj]+L[:-1])) \
		for j,t in enumerate(zip(C,C[1:]+[float("inf")],[float("inf")]+C[:-1],D,U)) \
		if t[0] < min(t[1:])]
		#list of minima (i,j)
	M = [[0 if elm == 9 else 1 for elm in row] for row in L]
		#whether each tile is still to be done
	basins = [0] * len(minima) #initialise each basin with 0 spaces
	for b,t in enumerate(minima):
		queue = [t]
		while len(queue) > 0:
			i,j = queue.pop()
			if i >= 0 and i < Ni and j >= 0 and j < Nj and M[i][j]:
				M[i][j] = 0
				basins[b] += 1
				queue.extend([(i-1,j), (i+1,j), (i,j-1), (i,j+1)])
	return math.prod(sorted(basins)[-3:])


print(day09_part1(L))
print(day09_part2(L))
# print(day09_part2_test(L))
# print(day09_part2_test2(L))
print(day09_part2_flood(L))