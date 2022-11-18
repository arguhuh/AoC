infile = open("input/in03_real.txt","r")
# infile = open("input/in03_test.txt","r")
L = [[0 if c=='.' else 1 for c in line.strip()] for line in infile]

def day03_part1(L,right,down):
	Nrows = len(L)
	Ncols = len(L[0])
	Ntrees = j = 0
	for i in range(0,Nrows,down): #row counter
		if L[i][j]:
			Ntrees += 1
		j = (j + right) % Ncols
	return Ntrees

def day03_part2(L):
	p = 1
	for right,down in zip([1,3,5,7,1],[1,1,1,1,2]):
		p *= day03_part1(L,right,down)
	return p


print(day03_part1(L,3,1))
print(day03_part2(L))