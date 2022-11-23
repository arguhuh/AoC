import itertools

infile = open("input/in17_real.txt","r")
# infile = open("input/in17_test.txt","r")
L = [[3 if c == '#' else 0 for c in line] for line in map(str.strip,infile)]

def step3D(G):
	Nlays = len(G)
	Nrows = len(G[0])
	Ncols = len(G[0][0])
	for i0,j0,k0 in itertools.product(range(Nlays),range(Nrows),range(Ncols)):
		match G[i0][j0][k0]:
			case 3:
				if not 3 <= sum([G[i][j][k] > 1 for i,j,k in itertools.product(\
				range(i0-1,i0+2),range(j0-1,j0+2),range(k0-1,k0+2)) \
				if 0 <= i < Nlays and 0 <= j < Nrows and 0 <= k < Ncols]) <= 4:
					G[i0][j0][k0] = 2
			case 0:
				if sum([G[i][j][k] > 1 for i,j,k in itertools.product(\
				range(i0-1,i0+2),range(j0-1,j0+2),range(k0-1,k0+2)) \
				if 0 <= i < Nlays and 0 <= j < Nrows and 0 <= k < Ncols]) == 3:
					G[i0][j0][k0] = 1
	for i0,j0,k0 in itertools.product(range(Nlays),range(Nrows),range(Ncols)):
		match G[i0][j0][k0]:
			case 2:
				G[i0][j0][k0] = 0
			case 1:
				G[i0][j0][k0] = 3
	return G

def day17_part1(L,Ncycles):
	Nrows = len(L) + 2*Ncycles
	Ncols = len(L[0]) + 2*Ncycles
	Nlays = 1 + 2*Ncycles
	
	G = [[[0 for _ in range(Ncols)] for _ in range(Nrows)] for _ in range(Nlays)]
	
	for irow in range(len(L)):
		G[Ncycles][Ncycles+irow][Ncycles:-Ncycles] = L[irow]
	
	for _ in range(Ncycles):
		step3D(G)
	
	return [elm for layer in G for row in layer for elm in row].count(3)

def step4D(G):
	Nhyps = len(G)
	Nlays = len(G[0])
	Nrows = len(G[0][0])
	Ncols = len(G[0][0][0])
	for i0,j0,k0,m0 in itertools.product(range(Nhyps),range(Nlays),range(Nrows),range(Ncols)):
		match G[i0][j0][k0][m0]:
			case 3:
				if not 3 <= sum([G[i][j][k][m] > 1 for i,j,k,m in itertools.product(range(i0-1,i0+2),range(j0-1,j0+2),range(k0-1,k0+2),range(m0-1,m0+2)) if 0 <= i < Nhyps and 0 <= j < Nlays and 0 <= k < Nrows and 0 <= m < Ncols]) <= 4:
					G[i0][j0][k0][m0] = 2
			case 0:
				if sum([G[i][j][k][m] > 1 for i,j,k,m in itertools.product(\
				range(i0-1,i0+2),range(j0-1,j0+2),range(k0-1,k0+2),range(m0-1,m0+2)) if 0 <= i < Nhyps and 0 <= j < Nlays and 0 <= k < Nrows and 0 <= m < Ncols]) == 3:
					G[i0][j0][k0][m0] = 1
	for i0,j0,k0,m0 in itertools.product(range(Nhyps),range(Nlays),range(Nrows),range(Ncols)):
		match G[i0][j0][k0][m0]:
			case 2:
				G[i0][j0][k0][m0] = 0
			case 1:
				G[i0][j0][k0][m0] = 3
	return G

def day17_part2(L,Ncycles):
	Nrows = len(L) + 2*Ncycles
	Ncols = len(L[0]) + 2*Ncycles
	Nlays = 1 + 2*Ncycles
	Nhyps = 1 + 2*Ncycles
	
	G = [[[[0 for _ in range(Ncols)] for _ in range(Nrows)] for _ in range(Nlays)] for _ in range(Nhyps)]
	
	for irow in range(len(L)):
		G[Ncycles][Ncycles][Ncycles+irow][Ncycles:-Ncycles] = L[irow]
	
	for _ in range(Ncycles):
		step4D(G)
	
	return [s for hyp in G for layer in hyp for row in layer for s in row].count(3)

print(day17_part1(L,6))
print(day17_part2(L,6))