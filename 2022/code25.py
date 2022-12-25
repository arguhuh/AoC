from pyperclip import copy as ctrl_C

Lboth = []
for filename in ["input/in25_test.txt", "input/in25_real.txt"]:
	with open(filename,"r") as infile:
		L = [line for line in map(str.strip,infile)]
		Lboth.append(L)
Ltest, Lreal = Lboth

def day25_part1(L):
	S = 0
	for s in L:
		P = 1
		for c in reversed(s):
			match c:
				case '=':
					S -= 2*P
				case '-':
					S -= P
				case _:
					S += int(c)*P
			P *= 5
	
	s = ''
	while S:
		S, r = divmod(S,5)
		if r > 2:
			S += 1
			if r == 3:
				s += '='
			else:
				s += '-'
		else:
			s += str(r)
		
	return s[::-1]


result_test_1 = day25_part1(Ltest)
result_real_1 = day25_part1(Lreal)

print(result_real_1)
print(result_test_1)
try:
	ctrl_C(result_real_1)
except:
	print("cannot copy result")