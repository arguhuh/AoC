infile = open("input/in20_real.txt","r")
# infile = open("input/in20_test.txt","r")
convert = [1 if c=='#' else 0 for c in next(infile).strip()]
next(infile)
grid = [[1 if c=='#' else 0 for c in line.strip()] for line in infile]

def enhance(grid,convert,seaof):
	Ni = len(grid)
	Nj = len(grid[0])
	grid[:] = [[convert[int(''.join(map(str,t)),2)] for t in zip([seaof]+U[:-1],U,U[1:]+[seaof],[seaof]+C[:-1],C,C[1:]+[seaof],[seaof]+D[:-1],D,D[1:]+[seaof])] for U,C,D in zip([[seaof]*Nj]+grid[:-1],grid,grid[1:]+[[seaof]*Nj])]

def day20_part1(grid,convert,Nenhance):
	Nj = len(grid[0])
	grid = [[0]*(Nj+2*Nenhance)]*Nenhance \
		+ [[0]*Nenhance + row + [0]*Nenhance for row in grid] \
		+ [[0]*(Nj+2*Nenhance)]*Nenhance
	seaof = 0
	for ienhance in range(Nenhance):
		enhance(grid,convert,seaof)
		seaof = convert[seaof]
	return sum([i for row in grid for i in row])

# print(day20_part1(grid,convert,2))
print(day20_part1(grid,convert,50))

# for row in day20_part1(grid,convert):
	# print(''.join(['#' if c==1 else '.' for c in row]))