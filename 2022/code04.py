from re import split
from pyperclip import copy as ctrl_C

Lboth = []
for filename in ["input/in04_test.txt", "input/in04_real.txt"]:
	with open(filename,"r") as infile:
		L = [list(map(int,split(',|-',line))) for line in map(str.strip,infile)]
		Lboth.append(L)
Ltest, Lreal = Lboth

def day04_part1(L):
	N = 0
	for p,q,r,s in L:
		R = set(range(p,q+1))
		S = set(range(r,s+1))
		if R <= S or S <= R: #if one is a subset of the other
			N += 1
	return N

def day04_part2(L):
	N = 0
	for p,q,r,s in L:
		R = set(range(p,q+1))
		S = set(range(r,s+1))
		if R & S: #if intersection is nonempty
			N += 1
	return N


result_test_1 = day04_part1(Ltest)
result_real_1 = day04_part1(Lreal)

print(result_real_1)
print(result_test_1)
try:
	ctrl_C(result_real_1)
except:
	print("cannot copy result")

result_test_2 = day04_part2(Ltest)
result_real_2 = day04_part2(Lreal)

if result_test_2 is not None:
	print()
	print(result_real_2)
	print(result_test_2)
	try:
		ctrl_C(result_real_2)
	except:
		print("cannot copy result")