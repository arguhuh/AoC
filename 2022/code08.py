from itertools import product
from pyperclip import copy as ctrl_C

Lboth = []
for filename in ["input/in08_test.txt", "input/in08_real.txt"]:
	with open(filename,"r") as infile:
		L = [line for line in map(lambda x: list(map(int,list(x))),map(str.strip,infile))]
		Lboth.append(L)
Ltest, Lreal = Lboth

def mymax(L):
	if len(L):
		return max(L)
	else:
		return -1

def day08_part1(L):
	M = len(L)
	N = len(L[0])
	Nvis = 0
	Lt = list(zip(*L))
	for i,j in product(range(M),range(N)):
		h = L[i][j]
		if mymax(L[i][:j]) < h or mymax(L[i][j+1:]) < h or mymax(Lt[j][:i]) < h or mymax(Lt[j][i+1:]) < h:
			Nvis += 1
	return Nvis

def score(L,Lt,i,j):
	h = L[i][j]
	score = 1
	
	W = [k < h for k in L[i][j-1::-1]]
	if W:
		if all(W):
			score *= len(W)
		else:
			score *= W.index(False) + 1
	else:
		score = 0
	W = [k < h for k in L[i][j+1:]]
	if W:
		if all(W):
			score *= len(W)
		else:
			score *= W.index(False) + 1
	else:
		score = 0
	W = [k < h for k in Lt[j][i-1::-1]]
	if W:
		if all(W):
			score *= len(W)
		else:
			score *= W.index(False) + 1
	else:
		score = 0
	W = [k < h for k in Lt[j][i+1:]]
	if W:
		if all(W):
			score *= len(W)
		else:
			score *= W.index(False) + 1
	else:
		score = 0
	return score

def day08_part2(L):
	M = len(L)
	N = len(L[0])
	Lt = list(zip(*L))
	return max(score(L,Lt,i,j) for i,j in product(range(1,M-1),range(1,N-1)))


result_test_1 = day08_part1(Ltest)
result_real_1 = day08_part1(Lreal)

print(result_real_1)
print(result_test_1)
try:
	ctrl_C(result_real_1)
except:
	print("cannot copy result")

result_test_2 = day08_part2(Ltest)
result_real_2 = day08_part2(Lreal)

if result_test_2 is not None:
	print()
	print(result_real_2)
	print(result_test_2)
	try:
		ctrl_C(result_real_2)
	except:
		print("cannot copy result")