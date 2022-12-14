from itertools import pairwise
from numpy import sign
from pyperclip import copy as ctrl_C

Lboth = []
for filename in ["input/in14_test.txt", "input/in14_real.txt"]:
	with open(filename,"r") as infile:
		L = [[tuple(map(int,pair.split(','))) for pair in line.split(' -> ')] for line in map(str.strip,infile)]
		Lboth.append(L)
Ltest, Lreal = Lboth

def add_grain(occ, ymax, origin = (500,0)):
	x,y = origin
	while y < ymax:
		if (x,y+1) not in occ:
			y += 1
		elif (x-1,y+1) not in occ:
			x -= 1
			y += 1
		elif (x+1,y+1) not in occ:
			x += 1
			y += 1
		else:
			occ.add((x,y))
			return True
	return False

def add_grain2(occ, ymax, origin = (500,0)):
	if origin in occ:
		return False

	x,y = origin
	while y <= ymax:
		if (x,y+1) not in occ:
			y += 1
		elif (x-1,y+1) not in occ:
			x -= 1
			y += 1
		elif (x+1,y+1) not in occ:
			x += 1
			y += 1
		else:
			break
	occ.add((x,y))
	return True

def day14_part1(L, add_fun = add_grain):
	occ = set()
	for path in L:
		for (x0,y0),(x1,y1) in pairwise(path):
			if x0 == x1:#vert
				for y in range(y0,y1,sign(y1-y0)):
					occ.add((x0,y))
			else:#horz
				for x in range(x0,x1,sign(x1-x0)):
					occ.add((x,y0))
		occ.add((x1,y1))
	ymax = max(occ, key = lambda p: p[1])[1]
	S = 0
	while add_fun(occ,ymax):
		S += 1
	return S

def day14_part2(L):
	return day14_part1(L, add_fun = add_grain2)


result_test_1 = day14_part1(Ltest)
result_real_1 = day14_part1(Lreal)

print(result_real_1)
print(result_test_1)
try:
	ctrl_C(result_real_1)
except:
	print("cannot copy result")

result_test_2 = day14_part2(Ltest)
result_real_2 = day14_part2(Lreal)

if result_test_2 is not None:
	print()
	print(result_real_2)
	print(result_test_2)
	try:
		ctrl_C(result_real_2)
	except:
		print("cannot copy result")