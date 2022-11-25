from itertools import product

infile = open("input/in24_real.txt","r")
# infile = open("input/in24_test.txt","r")

instructions = []
for line in map(str.strip,infile):
	instruction = []
	pos = 0
	while pos < len(line):
		match line[pos]:
			case 'n'|'s':
				instruction.append(line[pos:pos+2])
				pos += 2
			case _:
				instruction.append(line[pos])
				pos += 1
	instructions.append(instruction)

def position(instruction):
	x = y = 0
	for dir in instruction:
		match dir:
			case 'w':
				x -= 1
			case 'e':
				x += 1
			case 'nw':
				x -= 1
				y += 1
			case 'se':
				x += 1
				y -= 1
			case 'ne':
				y += 1
			case 'sw':
				y -= 1
	return (x,y)

def day24_part1(instructions):
	black = []
	for instruction in instructions:
		to_flip = position(instruction)
		if to_flip in black:
			black.remove(to_flip)
		else:
			black.append(to_flip)
	return black

def step(grid):
	Nrows = len(grid)
	for x,y in product(range(1,Nrows-1),range(1,Nrows-1)):
		match grid[x][y]:
			case 0:
				if sum([s > 1 for s in grid[x-1][y:y+2] + grid[x+1][y-1:y+1] + grid[x][y-1:y+2]]) == 2:
					grid[x][y] = 1
			case 3:
				if not 2 <= sum([s > 1 for s in grid[x-1][y:y+2] + grid[x+1][y-1:y+1] + grid[x][y-1:y+2]]) <= 3:
					grid[x][y] = 2
	for x,y in product(range(1,Nrows-1),range(1,Nrows-1)):
		match grid[x][y]:
			case 1:
				grid[x][y] = 3
			case 2:
				grid[x][y] = 0
	return grid

def day24_part2(instructions,Ndays):
	black = day24_part1(instructions)
	
	max_xy = max(abs(max(black, key = lambda p: abs(p[0]))[0]), abs(max(black, key = lambda p: abs(p[1]))[1]))
	shift = Ndays + max_xy + 1 #to only do interior
	res = 2 * shift + 1
	
	grid = [[0 for _ in range(res)] for _ in range(res)]
	for x,y in black:
		grid[x + shift][y + shift] = 3
	
	for _ in range(Ndays):
		step(grid)
	return sum(s == 3 for row in grid for s in row)

print(len(day24_part1(instructions)))
print(day24_part2(instructions,100))