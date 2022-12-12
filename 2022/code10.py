from more_itertools import repeat_each
from pyperclip import copy as ctrl_C

Lboth = []
for filename in ["input/in10_test.txt", "input/in10_real.txt"]:
	with open(filename,"r") as infile:
		L = [0 if line[0] == 'n' else int(line[5:]) for line in map(str.strip,infile)]
		Lboth.append(L)
Ltest, Lreal = Lboth

def day10_part1(L):
	cycle = S = 0
	X = 1
	next_milestone = 20
	for inst in L:
		if inst:
			cycle += 2
		else:
			cycle += 1
		if cycle >= next_milestone:
			S += next_milestone * X
			next_milestone += 40
		X += inst
	return S

def draw(row,cycle,X,thicken):
	x = cycle % 40
	if abs(x-X) <= 1:
		row[x] = '#'
	if x == 39:
		if thicken:
			print(''.join(repeat_each(row)))
		else:
			print(''.join(row))
		row[:] = ['.' for _ in range(40)]

def day10_part2(L,thicken):
	print()
	row = ['.' for _ in range(40)]
	cycle = -1
	X = 1
	for inst in L:
		for cycle in range(cycle + 1, cycle + 2 + bool(inst)):
			draw(row,cycle,X,thicken)
		X += inst

result_test_1 = day10_part1(Ltest)
result_real_1 = day10_part1(Lreal)

print(result_real_1)
print(result_test_1)
try:
	ctrl_C(result_real_1)
except:
	print("cannot copy result")

result_test_2 = day10_part2(Ltest, thicken = False)
result_real_2 = day10_part2(Lreal, thicken = True)

if result_test_2 is not None:
	print()
	print(result_real_2)
	print(result_test_2)
	try:
		ctrl_C(result_real_2)
	except:
		print("cannot copy result")