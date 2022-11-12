infile = open("input/in02_real.txt","r")
# infile = open("input/in02_test.txt","r")
L = [line.split() for line in infile]
L2 = [[dir,int(dist)] for dir,dist in L]

def day02_part1(L):
	x = y = 0
	for dir,dist in L:
		match dir:
			case 'forward':
				x += dist
			case 'down':
				y += dist
			case 'up':
				y -= dist
			case _:
				print('invalid instruction')
				return None
	return x * y

def day02_part2(L):
	x = y = aim = 0
	for dir,dist in L:
		match dir:
			case 'forward':
				x += dist
				y += dist * aim
			case 'down':
				aim += dist
			case 'up':
				aim -= dist
			case _:
				print('invalid instruction')
				return None
	return x * y

print(day02_part1(L2))
print(day02_part2(L2))