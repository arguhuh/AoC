infile = open("input/in12_real.txt","r")
# infile = open("input/in12_test.txt","r")
L = [(line[0],int(line[1:])) for line in map(str.strip,infile)]

def day12_part1(L):
	xdir = 1; ydir = 0 #east
	x = y = 0
	for dir,dist in L:
		match dir:
			case 'N':
				y += dist
			case 'S':
				y -= dist
			case 'E':
				x += dist
			case 'W':
				x -= dist
			case 'F':
				x += dist*xdir
				y += dist*ydir
		match (dir,dist):
			case ('L',90)|('R',270):
				temp = ydir
				ydir = xdir
				xdir = -temp
			case ('L',270)|('R',90):
				temp = ydir
				ydir = -xdir
				xdir = temp
			case (_,180):
				xdir = -xdir
				ydir = -ydir
	return abs(x) + abs(y)

def day12_part2(L):
	xdir = 10; ydir = 1
	x = y = 0
	for dir,dist in L:
		match dir:
			case 'N':
				ydir += dist
			case 'S':
				ydir -= dist
			case 'E':
				xdir += dist
			case 'W':
				xdir -= dist
			case 'F':
				x += dist*xdir
				y += dist*ydir
		match (dir,dist):
			case ('L',90)|('R',270):
				temp = ydir
				ydir = xdir
				xdir = -temp
			case ('L',270)|('R',90):
				temp = ydir
				ydir = -xdir
				xdir = temp
			case (_,180):
				xdir = -xdir
				ydir = -ydir
	return abs(x) + abs(y)

print(day12_part1(L))
print(day12_part2(L))