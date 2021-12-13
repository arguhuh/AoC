infile = open("input/in13_real.txt","r")
# infile = open("input/in13_test.txt","r")
points = []
for line in infile:
	if len(line.strip()) == 0:
		break
	points.append([int(i) for i in line.strip().split(',')][::-1])
instructions = [(d,int(m)) for d,m in [inst.strip()[11:].split('=') for inst in infile]]

def gridify(points):
	grid = [[0] * (max([point[1] for point in points])+1) for i in range(max([point[0] for point in points])+1)]
	for i,j in points:
		grid[i][j] = 1
	return grid

def fold(grid,instructions):
	for dir,mid in instructions:
		match dir:
			case 'x':
				grid = [[i or j for i,j in zip(row[:mid],row[:mid:-1])] for row in grid]
			case 'y':
				grid = [[i or j for i,j in zip(p,q)] for p,q in zip(grid[:mid],grid[:mid:-1])]
	return grid

def day13_part1(points,instructions):
	return sum([i for row in fold(gridify(points),instructions[:1]) for i in row])

def day13_part2(points,instructions):
	for row in fold(gridify(points),instructions):
		print(''.join(['#' if i else '.' for i in row]))

print(day13_part1(points,instructions))
day13_part2(points,instructions)