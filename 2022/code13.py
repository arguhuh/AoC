from itertools import zip_longest, chain
from functools import cmp_to_key
from pyperclip import copy as ctrl_C

Lboth = []
for filename in ["input/in13_test.txt", "input/in13_real.txt"]:
	with open(filename,"r") as infile:
		L = [list(map(eval,grp.split('\n'))) for grp in infile.read().split('\n\n')]
		Lboth.append(L)
Ltest, Lreal = Lboth

def compare(L,R):
	if L is None:
		return -1
	elif R is None:
		return 1
	elif isinstance(L,int) and isinstance(R,int):
		if L < R:
			return -1
		elif R < L:
			return 1
		else:
			return 0
	elif isinstance(L,int):
		L = [L]
	elif isinstance(R,int):
		R = [R]
	
	for pair in zip_longest(L,R):
		c = compare(*pair)
		if c:
			return c
	return 0

def day13_part1(L):
	return sum(i+1 for i,pair in enumerate(L) if compare(*pair) == -1)

def day13_part2(L):
	S = sorted(chain(*L, [[[2]], [[6]], None]), key = cmp_to_key(compare))
	return S.index([[2]]) * S.index([[6]])


result_test_1 = day13_part1(Ltest)
result_real_1 = day13_part1(Lreal)

print(result_real_1)
print(result_test_1)
try:
	ctrl_C(result_real_1)
except:
	print("cannot copy result")

result_test_2 = day13_part2(Ltest)
result_real_2 = day13_part2(Lreal)

if result_test_2 is not None:
	print()
	print(result_real_2)
	print(result_test_2)
	try:
		ctrl_C(result_real_2)
	except:
		print("cannot copy result")