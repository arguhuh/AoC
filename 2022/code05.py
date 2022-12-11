from copy import deepcopy
from pyperclip import copy as ctrl_C

Lboth = []
for filename in ["input/in05_test.txt", "input/in05_real.txt"]:
	with open(filename,"r") as infile:
		contents, instructions = infile.read().split('\n\n')
		
		*lines, _ = contents.split('\n')
		
		cont = [list(''.join(reversed(t)).strip()) for t in list(zip(*lines))[1::4]]
		
		inst = [list(map(int,line[1::2])) for line in map(str.split,instructions.split('\n'))]
		
		L = cont, inst
		
		Lboth.append(L)
Ltest, Lreal = Lboth

def popN(N,L):
	popped = L[-N:]
	L[-N:] = []
	return popped

def day05_part1(cont, inst):
	for M,F,T in inst:
		cont[T-1].extend(reversed(popN(M,cont[F-1])))
	return ''.join(map(list.pop, cont))

def day05_part2(cont, inst):
	for M,F,T in inst:
		cont[T-1].extend(popN(M,cont[F-1]))
	return ''.join(map(list.pop, cont))


result_test_1 = day05_part1(*deepcopy(Ltest))
result_real_1 = day05_part1(*deepcopy(Lreal))

print(result_real_1)
print(result_test_1)
try:
	ctrl_C(result_real_1)
except:
	print("cannot copy result")

result_test_2 = day05_part2(*Ltest)
result_real_2 = day05_part2(*Lreal)

if result_test_2 is not None:
	print()
	print(result_real_2)
	print(result_test_2)
	try:
		ctrl_C(result_real_2)
	except:
		print("cannot copy result")