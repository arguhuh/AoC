from more_itertools import windowed, all_unique
from pyperclip import copy as ctrl_C

Lboth = []
for filename in ["input/in06_test.txt", "input/in06_real.txt"]:
	with open(filename,"r") as infile:
		L = infile.read()
		Lboth.append(L)
Ltest, Lreal = Lboth

def day06_part1(L, window = 4):
	return next(filter(lambda p: all_unique(p[1]), \
	enumerate(windowed(L,window))))[0] + window

def day06_part2(L):
	return day06_part1(L,14)


result_test_1 = day06_part1(Ltest)
result_real_1 = day06_part1(Lreal)

print(result_real_1)
print(result_test_1)
try:
	ctrl_C(result_real_1)
except:
	print("cannot copy result")

result_test_2 = day06_part2(Ltest)
result_real_2 = day06_part2(Lreal)

if result_test_2 is not None:
	print()
	print(result_real_2)
	print(result_test_2)
	try:
		ctrl_C(result_real_2)
	except:
		print("cannot copy result")