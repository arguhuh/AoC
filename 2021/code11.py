infile = open("input/in11_real.txt","r")
# infile = open("input/in11_test.txt","r")
L = [[int(i) for i in line.strip()] for line in infile]

def step(L):
	Ni = len(L)
	Nj = len(L[0])
	L[:] = [[(elm+1)%10 for elm in row] for row in L]
	flash_queue = [(i,j) for i,row in enumerate(L)
		for j,elm in enumerate(row) if not elm]
	Nflash = len(flash_queue)
	while len(flash_queue) > 0:
		i0,j0 = flash_queue.pop()
		for i in range(max(0,i0-1),min(Ni,i0+2)):
			for j in range(max(0,j0-1),min(Nj,j0+2)):
				if L[i][j] == 9:
					L[i][j] = 0
					flash_queue.append((i,j))
					Nflash += 1
				elif L[i][j] > 0:
					L[i][j] += 1
	return Nflash

def day11_part1(L,Nsteps):
	Nflash = 0
	for _ in range(Nsteps):
		Nflash += step(L)
	return Nflash

def day11_part2(L):
	istep = 1
	while step(L) != 100:
		istep += 1
	return istep

print(day11_part1(L[:],100))
print(day11_part2(L[:]))
