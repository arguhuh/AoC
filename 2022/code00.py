import re, itertools, math

Lboth = []
for filename in ["input/in##_test.txt", "input/in##_real.txt"]:
	with open(filename,"r") as infile:
		L = [line for line in infile]
		Lboth.append(L)
Ltest, Lreal = Lboth

def day##_part1(L):
	return L

print(day##_part1(Ltest))
print(day##_part1(Lreal))
# print()
# print(day##_part2(Ltest))
# print(day##_part2(Lreal))