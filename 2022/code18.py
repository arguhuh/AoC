import numpy as np
from pyperclip import copy as ctrl_C

Lboth = []
for filename in ["input/in18_test.txt", "input/in18_real.txt"]:
	with open(filename,"r") as infile:
		L = [tuple(map(int,line.split(','))) for line in map(str.strip,infile)]
		Lboth.append(L)
Ltest, Lreal = Lboth

def day18_part1(L):
	xmin, ymin, zmin = [min(x[i] for x in L) - 1 for i in range(3)]
	xmax, ymax, zmax = [max(x[i] for x in L) + 1 for i in range(3)]
	state = np.zeros((xmax-xmin+1, ymax-ymin+1, zmax-zmin+1), dtype = int)
	
	for x,y,z in L:
		state[x-xmin][y-ymin][z-zmin] = 1
	
	return int(sum(np.sum(abs(np.diff(state, axis = i))) for i in range(3)))

def day18_part2(L):
	xmin, ymin, zmin = [min(x[i] for x in L) - 1 for i in range(3)]
	xmax, ymax, zmax = [max(x[i] for x in L) + 1 for i in range(3)]
	state = np.zeros((xmax-xmin+1, ymax-ymin+1, zmax-zmin+1), dtype = int)
	
	for x,y,z in L:
		state[x-xmin][y-ymin][z-zmin] = 2
	state[0][0][0] = 1
	
	queue = [(0,0,0)]
	while queue:
		x,y,z = queue.pop()
		for X,Y,Z in [(x+1,y,z),(x-1,y,z),(x,y+1,z),(x,y-1,z),(x,y,z+1),(x,y,z-1)]:
			try:
				if not state[X][Y][Z]:
					state[X][Y][Z] = 1
					queue.append((X,Y,Z))
			except IndexError:
				pass
	
	return int(sum(np.sum(abs(np.diff(state, axis = i)) == 1) for i in range(3)))


result_test_1 = day18_part1(Ltest)
result_real_1 = day18_part1(Lreal)

print(result_real_1)
print(result_test_1)
try:
	ctrl_C(result_real_1)
except:
	print("cannot copy result")

result_test_2 = day18_part2(Ltest)
result_real_2 = day18_part2(Lreal)

if result_test_2 is not None:
	print()
	print(result_real_2)
	print(result_test_2)
	try:
		ctrl_C(result_real_2)
	except:
		print("cannot copy result")