from math import prod

infile = open("input/in02_test.txt","r")
# infile = open("input/in02_real.txt","r")
L = [line.split() for line in infile.readlines()]
L2 = [[p[0],int(p[1])] for p in L]

def day02_part1(L):
	pos = [0, 0]
	for dir,dist in L:
		match dir:
			case 'forward':
				pos[0] += dist
			case 'down':
				pos[1] += dist
			case 'up':
				pos[1] -= dist
			case _:
				print('invalid instruction')
				return None
	return prod(pos)

def day02_part2(L):
	pos = [0, 0]
	aim = 0
	for inst in L:
		if inst[0] == 'forward':
			pos[0] += inst[1]
			pos[1] += inst[1] * aim
		elif inst[0] == 'down':
			aim += inst[1]
		elif inst[0] == 'up':
			aim -= inst[1]
		else:
			print('invalid instruction')
			return None
	return prod(pos)

print(day02_part1(L2))
print(day02_part2(L2))