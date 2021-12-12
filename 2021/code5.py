import re

infile = open("in5_real.txt","r")
# infile = open("in5_test.txt","r")
L = [[int(i) for i in re.split(',| -> ',line.strip())] for line in infile.readlines()]

def day5_part1(L):
	N = max([max(line) for line in L]) + 1 #len of grid
	G = [[0] * N for i in range(N)] #because mutability
	for line in L:
		dx = line[2] - line[0]
		dy = line[3] - line[1]
		if dx == 0:
			i = line[0]
			sy = (dy>0)-(dy<0)
			for j in range(line[1],line[3]+sy,sy):
				G[j][i] += 1
		elif dy == 0:
			j = line[1]
			sx = (dx>0)-(dx<0)
			for i in range(line[0],line[2]+sx,sx):
				G[j][i] += 1
	return sum([sum([1 for i in row if i > 1]) for row in G])

def day5_part2(L):
	N = max([max(line) for line in L]) + 1 #len of grid
	G = [[0] * N for i in range(N)] #because mutability
	for line in L:
		dx = line[2] - line[0]
		dy = line[3] - line[1]
		if dx == 0:
			i = line[0]
			sy = (dy>0)-(dy<0)
			for j in range(line[1],line[3]+sy,sy):
				G[j][i] += 1
		elif dy == 0:
			j = line[1]
			sx = (dx>0)-(dx<0)
			for i in range(line[0],line[2]+sx,sx):
				G[j][i] += 1
		else:
			sx = (dx>0)-(dx<0)
			sy = (dy>0)-(dy<0)
			for i,j in zip(range(line[0],line[2]+sx,sx),range(line[1],line[3]+sy,sy)):
				G[j][i] += 1
	return sum([sum([1 for i in row if i > 1]) for row in G])

print(day5_part1(L))
print(day5_part2(L))