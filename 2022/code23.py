from itertools import count
from pyperclip import copy as ctrl_C

Lboth = []
for filename in ["input/in23_test.txt", "input/in23_real.txt"]:
	with open(filename,"r") as infile:
		L = [(i,j) for i,line in enumerate(map(str.strip,infile)) for j,c in enumerate(line) if c == '#']
		Lboth.append(L)
Ltest, Lreal = Lboth

def facing_free(L,facing,i,j):
	match facing:
		case 0:
			return (i-1,j), \
			(i-1,j-1) not in L and (i-1,j) not in L and (i-1,j+1) not in L #N
		case 1:
			return (i+1,j), \
			(i+1,j-1) not in L and (i+1,j) not in L and (i+1,j+1) not in L #S
		case 2:
			return (i,j-1), \
			(i-1,j-1) not in L and (i,j-1) not in L and (i+1,j-1) not in L #W
		case 3:
			return (i,j+1), \
			(i-1,j+1) not in L and (i,j+1) not in L and (i+1,j+1) not in L #E

def step(L,facing0):
	curr_poses = set(L)
	new_poses = {} #pos: (first used, came from)
	Nchanged = 0
	for p, (i,j) in enumerate(L):
		if (i-1,j-1) in curr_poses or (i-1,j) in curr_poses \
		or (i-1,j+1) in curr_poses or (i,j-1) in curr_poses \
		or (i,j+1) in curr_poses or (i+1,j-1) in curr_poses \
		or (i+1,j) in curr_poses or (i+1,j+1) in curr_poses:
			for dfacing in range(4):
				dest, free = facing_free(curr_poses,(facing0 + dfacing) % 4,i,j)
				if free:
					if dest not in new_poses:
						L[p] = dest
						new_poses[dest] = (p, (i,j))
						Nchanged += 1
					else:
						q, pos = new_poses[dest]
						if L[q] != pos:
							L[q] = pos
							Nchanged -= 1
					break
	return Nchanged == 0

def day23_part1(L, Nrounds = 10):
	for facing in range(Nrounds):
		step(L,facing % 4)
	
	return (max(L,key = lambda p: p[0])[0] - min(L,key = lambda p: p[0])[0] + 1) \
	* (max(L,key = lambda p: p[1])[1] - min(L,key = lambda p: p[1])[1] + 1) - len(L)

def day23_part2(L, Nroundsdone = 10):
	for facing in count(Nroundsdone):
		stop = step(L,facing % 4)
		if stop:
			break
	return facing + 1


result_test_1 = day23_part1(Ltest)
result_real_1 = day23_part1(Lreal)

print(result_real_1)
print(result_test_1)
try:
	ctrl_C(result_real_1)
except:
	print("cannot copy result")

result_test_2 = day23_part2(Ltest)
result_real_2 = day23_part2(Lreal)

if result_test_2 is not None:
	print()
	print(result_real_2)
	print(result_test_2)
	try:
		ctrl_C(result_real_2)
	except:
		print("cannot copy result")