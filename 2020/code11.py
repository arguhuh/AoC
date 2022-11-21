import itertools,copy

infile = open("input/in11_real.txt","r")
# infile = open("input/in11_test.txt","r")
L = [[1 if c == 'L' else 0 for c in line] for line in map(str.strip,infile)]

def step(L): #0: floor, 1: empty, 2: seating, 3: unseating, 4: seated
	hasanythingchangedyet = False
	Nrows = len(L)
	Ncols = len(L[0])
	for i0,j0 in itertools.product(range(len(L)),range(len(L[0]))):
		match L[i0][j0]:
			case 1:
				if all(L[i][j] < 3 for i,j in \
				itertools.product(range(i0-1,i0+2),range(j0-1,j0+2)) \
				if 0 <= i < Nrows and 0 <= j < Ncols):
					L[i0][j0] = 2
			case 4:
				if sum(L[i][j] > 2 for i,j in \
				itertools.product(range(i0-1,i0+2),range(j0-1,j0+2)) \
				if 0 <= i < Nrows and 0 <= j < Ncols) > 4:
					L[i0][j0] = 3
	for i0,j0 in itertools.product(range(len(L)),range(len(L[0]))):
		match L[i0][j0]:
			case 2:
				L[i0][j0] = 4
				hasanythingchangedyet = True
			case 3:
				L[i0][j0] = 1
				hasanythingchangedyet = True
	return hasanythingchangedyet,L

def day11_part1(L):
	while step(L)[0]:
		pass
	return sum(x == 4 for x in itertools.chain(*L))

def step2(L): #0: floor, 1: empty, 2: seating, 3: unseating, 4: seated
	hasanythingchangedyet = False
	Nrows = len(L)
	Ncols = len(L[0])
	for i0,j0 in itertools.product(range(len(L)),range(len(L[0]))):
		match L[i0][j0]:
			case 1:
				for xdir,ydir in itertools.product(range(-1,2),range(-1,2)):
					if not xdir and not ydir:
						continue
					match xdir:
						case -1:
							xgen = range(i0-1,-1,-1)
						case 0:
							xgen = itertools.repeat(i0)
						case 1:
							xgen = range(i0+1,Nrows)
					match ydir:
						case -1:
							ygen = range(j0-1,-1,-1)
						case 0:
							ygen = itertools.repeat(j0)
						case 1:
							ygen = range(j0+1,Ncols)
					if next(itertools.chain(itertools.dropwhile(lambda s: not s, \
					(L[i][j] for i,j in zip(xgen,ygen))), [0])) > 2:
						break
				else: #didn't break
					L[i0][j0] = 2
			case 4:
				Nseated = 0
				for xdir,ydir in itertools.product(range(-1,2),range(-1,2)):
					if not xdir and not ydir:
						continue
					match xdir:
						case -1:
							xgen = range(i0-1,-1,-1)
						case 0:
							xgen = itertools.repeat(i0)
						case 1:
							xgen = range(i0+1,Nrows)
					match ydir:
						case -1:
							ygen = range(j0-1,-1,-1)
						case 0:
							ygen = itertools.repeat(j0)
						case 1:
							ygen = range(j0+1,Ncols)
					if next(itertools.chain(itertools.dropwhile(lambda s: not s, \
					(L[i][j] for i,j in zip(xgen,ygen))), [0])) > 2:
						Nseated += 1
				if Nseated > 4:
					L[i0][j0] = 3
	for i0,j0 in itertools.product(range(len(L)),range(len(L[0]))):
		match L[i0][j0]:
			case 2:
				L[i0][j0] = 4
				hasanythingchangedyet = True
			case 3:
				L[i0][j0] = 1
				hasanythingchangedyet = True
	return hasanythingchangedyet,L

def day11_part2(L):
	while step2(L)[0]:
		pass
	return sum(x == 4 for x in itertools.chain(*L))

print(day11_part1(copy.deepcopy(L)))
print(day11_part2(copy.deepcopy(L)))