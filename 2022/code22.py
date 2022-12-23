from re import split
from itertools import zip_longest
from more_itertools import windowed
from pyperclip import copy as ctrl_C

Lboth = []
for filename in ["input/in22_test.txt", "input/in22_real.txt"]:
	with open(filename,"r") as infile:
		gridstr,inststr = infile.read().split('\n\n')
		gridLR = [list(filter(lambda p: p[1] != ' ', enumerate(row))) for row in gridstr.split('\n')]
		gridUD = [list(filter(lambda p: p[1] != ' ', enumerate(row))) for row in zip_longest(*gridstr.split('\n'), fillvalue = ' ')]
		insts = [(1 if s[0] == 'R' else -1, int(s[1:])) for s in split('(?=R|L)',inststr)[1:]] #start facing up, not right
		
		L = gridLR, gridUD, insts
		Lboth.append(L)
Ltest, Lreal = Lboth

def create_dict(gridLR, gridUD):
	move = {} #pos: [pos to R, pos to D, pos to L, pos to U]
	for i,row in enumerate(gridLR):
		rowdict = {(i,j): [(i,jR) if cR == '.' else (i,j), None, (i,jL) if cL == '.' else (i,j), None] for (jL,cL),(j,c),(jR,cR) in windowed(row + row[:2],3) if c == '.'}
		move |= rowdict
	for j,col in enumerate(gridUD):
		for (iU,cU),(i,c),(iD,cD) in windowed(col + col[:2],3):
			if c == '.':
				move[(i,j)][1] = (iD,j) if cD == '.' else (i,j)
				move[(i,j)][3] = (iU,j) if cU == '.' else (i,j)
	return move

def day22_part1(gridLR, gridUD, insts):
	move = create_dict(gridLR, gridUD)
	facing = 3
	pos = (0, gridLR[0][0][0])
	for turn, walk in insts:
		facing = (facing + turn) % 4
		for _ in range(walk):
			pos = move[pos][facing]
	return 1000 * (pos[0] + 1) + 4 * (pos[1] + 1) + facing

def create_dict_cube(gridLR, gridUD):
	#cube shape:
	#  UR
	#  F
	# LD
	# B
	#
	# R turned 90
	# L turned 90
	# B turned 90
	
	free = {(i,j): c == '.' for i,row in enumerate(gridLR) for j,c in row}
	Mf = 50
	
	move = {p: [None, None, None, None] for p, B in free.items() if B}
	for i,j in move.keys():
		Rp = (i,j+1)
		if Rp in free:
			if free[Rp]:
				R = (Rp, 0)
			else:
				R = ((i,j), 0)
		else:
			R = None
		Dp = (i+1,j)
		if Dp in free:
			if free[Dp]:
				D = (Dp, 1)
			else:
				D = ((i,j), 1)
		else:
			D = None
		Lp = (i,j-1)
		if Lp in free:
			if free[Lp]:
				L = (Lp, 2)
			else:
				L = ((i,j), 2)
		else:
			L = None
		Up = (i-1,j)
		if Up in free:
			if free[Up]:
				U = (Up, 3)
			else:
				U = ((i,j), 3)
		else:
			U = None
		move[(i,j)] = [R, D, L, U]
	
	# U left -> left L
	for i in range(0,Mf):
		p = (i, Mf)
		q = (3*Mf - 1 - i, 0)
		if free[p] and free[q]:
			move[p][2] = (q, 0)
			move[q][2] = (p, 0)
		elif free[p]:
			move[p][2] = (p, 2)
		elif free[q]:
			move[q][2] = (q, 2)
	
	# U up -> left B
	for j in range(Mf,2*Mf):
		p = (0, j)
		q = (j + 2*Mf, 0)
		if free[p] and free[q]:
			move[p][3] = (q, 0)
			move[q][2] = (p, 1)
		elif free[p]:
			move[p][3] = (p, 3)
		elif free[q]:
			move[q][2] = (q, 2)
	
	# R up -> bottom B
	for j in range(2*Mf,3*Mf):
		p = (0, j)
		q = (4*Mf - 1, j - 2*Mf)
		if free[p] and free[q]:
			move[p][3] = (q, 3)
			move[q][1] = (p, 1)
		elif free[p]:
			move[p][3] = (p, 3)
		elif free[q]:
			move[q][1] = (q, 1)
	
	# R right -> right D
	for i in range(0,Mf):
		p = (i, 3*Mf - 1)
		q = (3*Mf - 1 - i, 2*Mf - 1)
		if free[p] and free[q]:
			move[p][0] = (q, 2)
			move[q][0] = (p, 2)
		elif free[p]:
			move[p][0] = (p, 0)
		elif free[q]:
			move[q][0] = (q, 0)
	
	# R down -> right F
	for j in range(2*Mf,3*Mf):
		p = (Mf - 1, j)
		q = (j - Mf, 2*Mf - 1)
		if free[p] and free[q]:
			move[p][1] = (q, 2)
			move[q][0] = (p, 3)
		elif free[p]:
			move[p][1] = (p, 1)
		elif free[q]:
			move[q][0] = (q, 0)
	
	# F left -> top L
	for i in range(Mf,2*Mf):
		p = (i, Mf)
		q = (2*Mf, i - Mf)
		if free[p] and free[q]:
			move[p][2] = (q, 1)
			move[q][3] = (p, 0)
		elif free[p]:
			move[p][2] = (p, 2)
		elif free[q]:
			move[q][3] = (q, 3)
	
	# D down -> right B
	for j in range(Mf,2*Mf):
		p = (3*Mf - 1, j)
		q = (j + 2*Mf, Mf - 1)
		if free[p] and free[q]:
			move[p][1] = (q, 2)
			move[q][0] = (p, 3)
		elif free[p]:
			move[p][1] = (p, 1)
		elif free[q]:
			move[q][0] = (q, 0)
	
	return move

def day22_part2(gridLR, gridUD, insts):
	move = create_dict_cube(gridLR, gridUD)
	facing = 3
	pos = (0, gridLR[0][0][0])
	for turn, walk in insts:
		facing = (facing + turn) % 4
		for _ in range(walk):
			pos, facing = move[pos][facing]
	return 1000 * (pos[0] + 1) + 4 * (pos[1] + 1) + facing


result_test_1 = day22_part1(*Ltest)
result_real_1 = day22_part1(*Lreal)

print(result_real_1)
print(result_test_1)
try:
	ctrl_C(result_real_1)
except:
	print("cannot copy result")

result_real_2 = day22_part2(*Lreal)

if result_real_2 is not None:
	print()
	print(result_real_2)
	try:
		ctrl_C(result_real_2)
	except:
		print("cannot copy result")