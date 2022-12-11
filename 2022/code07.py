from itertools import count
from pyperclip import copy as ctrl_C

Lboth = []
for filename in ["input/in07_test.txt", "input/in07_real.txt"]:
	with open(filename,"r") as infile:
		next(infile)
		L = list(map(str.strip,infile))
		Lboth.append(L)
Ltest, Lreal = Lboth

def tree(L):
	d = '/'
	D = {d: []}
	for line in L:
		if line[:4] == '$ cd':
			if line[5:] == '..':
				for i in count(2):
					if d[-i] == '/':
						d = d[:1-i]
						break
			else:
				d += line[5:] + '/'
				D[d] = []
		elif line[0] != '$':
			if line[0] == 'd':
				D[d].append(d + line[4:] + '/')
			else:
				size, _ = line.split()
				D[d].append(int(size))
	return D

def sizes(L):
	D = tree(L)
	while any(isinstance(v,list) for v in D.values()):
		for k,v in D.items():
			if isinstance(v,list):
				S = 0
				for i in v:
					if isinstance(i,str):
						if isinstance(D[i],list):
							S = None
							break
						else:
							S += D[i]
					else:
						S += i
				if S is not None:
					D[k] = S
	return D

def day07_part1(L):
	return sum(i for i in sizes(L).values() if i <= 100000)

def day07_part2(L):
	D = sizes(L)
	return min(i for i in D.values() if i >= D['/'] - 40000000)


result_test_1 = day07_part1(Ltest)
result_real_1 = day07_part1(Lreal)

print(result_real_1)
print(result_test_1)
try:
	ctrl_C(result_real_1)
except:
	print("cannot copy result")

result_test_2 = day07_part2(Ltest)
result_real_2 = day07_part2(Lreal)

if result_test_2 is not None:
	print()
	print(result_real_2)
	print(result_test_2)
	try:
		ctrl_C(result_real_2)
	except:
		print("cannot copy result")