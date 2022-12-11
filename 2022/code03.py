from more_itertools import divide, chunked
from functools import partial
from pyperclip import copy as ctrl_C

Lboth = []
for filename in ["input/in03_test.txt", "input/in03_real.txt"]:
	with open(filename,"r") as infile:
		L = list(map(str.strip,infile))
		Lboth.append(L)
Ltest, Lreal = Lboth

def pri(n):
	o = ord(n)
	if o >= ord('a'):
		return o - ord('a') + 1
	else:
		return o - ord('A') + 27

def day03_part1(L):
	return sum(pri(list(p & q)[0]) for p,q in \
	map(partial(map,set), map(partial(divide,2), L)))

def day03_part2(L):
	return sum(pri(list(p & q & r)[0]) for p,q,r in \
	map(partial(map,set), chunked(L,3)))


result_test_1 = day03_part1(Ltest)
result_real_1 = day03_part1(Lreal)

print(result_real_1)
print(result_test_1)
try:
	ctrl_C(result_real_1)
except:
	print("cannot copy result")

result_test_2 = day03_part2(Ltest)
result_real_2 = day03_part2(Lreal)

if result_test_2 is not None:
	print()
	print(result_real_2)
	print(result_test_2)
	try:
		ctrl_C(result_real_2)
	except:
		print("cannot copy result")