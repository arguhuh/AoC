import re,itertools

infile = open("input/in05_real.txt","r")
# infile = open("input/in05_test.txt","r")
L = [[int(i) for i in re.split(',| -> ',line.strip())] for line in infile]

def day05_part1(L):
	N = max(itertools.chain(*L)) + 1 #len of grid
	G = [[0] * N for _ in range(N)] #because mutability
	for x0,y0,x1,y1 in L:
		dx = x1 - x0
		dy = y1 - y0
		if dx == 0:
			i = x0
			sy = (dy>0)-(dy<0)
			for j in range(y0,y1+sy,sy):
				G[j][i] += 1
		elif dy == 0:
			j = y0
			sx = (dx>0)-(dx<0)
			for i in range(x0,x1+sx,sx):
				G[j][i] += 1
	return sum([sum([1 for i in row if i > 1]) for row in G]) #could probably be a function

def day05_part2(L):
	N = max(itertools.chain(*L)) + 1 #len of grid
	G = [[0] * N for _ in range(N)] #because mutability
	for x0,y0,x1,y1 in L:
		dx = x1 - x0
		dy = y1 - y0
		if dx == 0:
			i = x0
			sy = (dy>0)-(dy<0)
			for j in range(y0,y1+sy,sy):
				G[j][i] += 1
		elif dy == 0:
			j = y0
			sx = (dx>0)-(dx<0)
			for i in range(x0,x1+sx,sx):
				G[j][i] += 1
		else:
			sx = (dx>0)-(dx<0)
			sy = (dy>0)-(dy<0)
			for i,j in zip(range(x0,x1+sx,sx),range(y0,y1+sy,sy)):
				G[j][i] += 1
	return sum([sum([1 for i in row if i > 1]) for row in G])

print(day05_part1(L))
print(day05_part2(L))