from math import prod,sqrt
from itertools import product

infile = open("input/in20_real.txt","r")
# infile = open("input/in20_test.txt","r")

tiles = []
tile = []
n = int(next(infile).split()[1][:-1])
for line in infile:
	if line == '\n':
		tiles.append((n,tile))
		tile = []
		n = int(next(infile).split()[1][:-1])
	else:
		tile.append(line.strip())
tiles.append((n,tile))

def border_match_tile(border,tile):
	for i,b in enumerate([tile[0], tile[0][::-1], tile[-1], tile[-1][::-1], \
	list(map(''.join,zip(*tile)))[0], list(map(''.join,zip(*tile)))[0][::-1], \
	list(map(''.join,zip(*tile)))[-1], list(map(''.join,zip(*tile)))[-1][::-1]]):
		if border == b:
			return i

def day20_part1(tiles):
	corners = []
	for i,tile in tiles:
		Nmatch = 0
		for border in [tile[0], tile[-1], list(map(''.join,zip(*tile)))[0], \
		list(map(''.join,zip(*tile)))[-1]]:
			for j,t in tiles:
				if i != j and border_match_tile(border,t) is not None:
					Nmatch += 1
					break
			if Nmatch == 3:
				break
		if Nmatch == 2:
			corners.append(i)
	return corners

def ismonster(snapshot,monster):
	for i,j in product(range(len(monster)),range(len(monster[0]))):
		if monster[i][j] == '#' and snapshot[i][j] != '#':
			return False
	return True

def day20_part2(tiles):
	width = round(sqrt(len(tiles)))
	grid = [[None for _ in range(width)] for _ in range(width)]
	
	corners = day20_part1(tiles)
	for i,tile in tiles:
		if i in corners:
			tiles.remove((i,tile))
			break

	internals = []
	for b,border in enumerate([tile[0], tile[-1], list(map(''.join,zip(*tile)))[0], \
	list(map(''.join,zip(*tile)))[-1]]):
		for j,t in tiles:
			if border_match_tile(border,t) is not None:
				internals.append(b)
				break

	match internals:
		case [0,2]:#top, left
			grid[0][0] = [row[::-1] for row in tile[::-1]]
		case [0,3]:#top, right
			grid[0][0] = tile[::-1]
		case [1,2]:#bottom, left
			grid[0][0] = [row[::-1] for row in tile]
		case [1,3]: #bottom, right
			grid[0][0] = tile
	
	for i in range(width):
		if i != width - 1:
			for k,tile in tiles:
				b = border_match_tile(grid[i][0][-1],tile)
				if b is not None:
					match b:
						case 0:
							grid[i+1][0] = tile
						case 1: #horz flipped
							grid[i+1][0] = [row[::-1] for row in tile]
						case 2: #vert flipped
							grid[i+1][0] = tile[::-1]
						case 3: #double flipped
							grid[i+1][0] = [row[::-1] for row in tile[::-1]]
						case 4: #transposed
							grid[i+1][0] = list(map(''.join,zip(*tile)))
						case 5: #transposed then horz flipped
							grid[i+1][0] = [row[::-1] for row in map(''.join,zip(*tile))]
						case 6: #transposed then vert flipped
							grid[i+1][0] = list(map(''.join,zip(*tile)))[::-1]
						case 7: #transposed then double flipped
							grid[i+1][0] = [row[::-1] for row in list(map(''.join,zip(*tile)))[::-1]]
					tiles.remove((k,tile))
					break
		for j in range(width-1):
			for k,tile in tiles:
				b = border_match_tile(list(map(''.join,zip(*grid[i][j])))[-1],tile)
				if b is not None:
					match b:
						case 0: #transposed
							grid[i][j+1] = list(map(''.join,zip(*tile)))
						case 1: #transposed then vert flipped
							grid[i][j+1] = list(map(''.join,zip(*tile)))[::-1]
						case 2: #transposed then horz flipped
							grid[i][j+1] = [row[::-1] for row in map(''.join,zip(*tile))]
						case 3: #transposed then double flipped
							grid[i][j+1] = [row[::-1] for row in list(map(''.join,zip(*tile)))[::-1]]
						case 4:
							grid[i][j+1] = tile
						case 5: #vert flipped
							grid[i][j+1] = tile[::-1]
						case 6: #horz flipped
							grid[i][j+1] = [row[::-1] for row in tile]
						case 7: #double flipped
							grid[i][j+1] = [row[::-1] for row in tile[::-1]]
					tiles.remove((k,tile))
					break
	
	for i,j in product(range(width),range(width)):
		grid[i][j] = [row[1:-1] for row in grid[i][j][1:-1]]
	image = [''.join(grid[itile][jtile][irow] for jtile in range(width)) for itile in range(width) for irow in range(len(grid[0][0]))]
	
	monster = ['                  # ','#    ##    ##    ###',' #  #  #  #  #  #   ']
	Mrows = len(monster)
	Mcols = len(monster[0])
	res = len(image)
	
	for orientation in [image, [row[::-1] for row in image], image[::-1], [row[::-1] for row in image[::-1]], list(map(''.join,zip(*image))), [row[::-1] for row in map(''.join,zip(*image))], list(map(''.join,zip(*image)))[::-1], [row[::-1] for row in list(map(''.join,zip(*image)))[::-1]]]:
		Nmonsters = 0
		for ishift, jshift in product(range(res-Mrows+1),range(res-Mcols+1)):
			if ismonster([row[jshift:jshift+Mcols] for row in \
			orientation[ishift:ishift+Mrows]], monster):
				Nmonsters += 1
		if Nmonsters:
			break
	
	return sum([row.count('#') for row in image]) - Nmonsters * sum([row.count('#') for row in monster])

print(prod(day20_part1(tiles)))
print(day20_part2(tiles))