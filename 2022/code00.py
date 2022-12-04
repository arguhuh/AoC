import re, itertools, math, pyperclip

Lboth = []
for filename in ["input/in##_test.txt", "input/in##_real.txt"]:
	with open(filename,"r") as infile:
		L = [line for line in map(str.strip,infile)]
		
		# L = [i for i in map(int,map(str.strip,infile))]
		
		# L = [[elm for elm in line] for line in map(str.split,infile)]
		
		# L = [[i for i in map(int,line)] for line in map(str.split,infile)]
		
		# L = [(a,b) for a,b in map(str.split,infile)]
		
		# L = [[line for line in grp.split('\n')] for grp in infile.read().split('\n\n')]
		
		# L = [[i for i in map(int,grp.split('\n'))] for grp in infile.read().split('\n\n')]
		
		# L = [[[elm for elm in line] for line in map(str.split,grp.split('\n'))] for grp in infile.read().split('\n\n')]
		
		# L = [[[i for i in map(int,line)] for line in map(str.split,grp.split('\n'))] for grp in infile.read().split('\n\n')]
		
		# L = [[(a,b) for a,b in map(str.split,grp.split('\n'))] for grp in infile.read().split('\n\n')]
		
		Lboth.append(L)
Ltest, Lreal = Lboth

def day##_part1(L):
	return L

def day##_part2(L):
	return


result_test_1 = day##_part1(Ltest)
result_real_1 = day##_part1(Lreal)

print(result_test_1)
print(result_real_1)
pyperclip.copy(result_real_1)

result_test_2 = day##_part2(Ltest)
result_real_2 = day##_part2(Lreal)

if result_test_2 is not None:
	print()
	print(result_test_2)
	print(result_real_2)
	pyperclip.copy(result_real_2)