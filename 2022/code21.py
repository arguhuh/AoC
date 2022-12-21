from re import sub
from pyperclip import copy as ctrl_C

Lboth = []
for filename in ["input/in21_test.txt", "input/in21_real.txt"]:
	with open(filename,"r") as infile:
		L = {a: b.split() if ' ' in b else int(b) for a,b in [sub('/','//',line).split(': ') for line in map(str.strip,infile)]}
		Lboth.append(L)
Ltest, Lreal = Lboth

def day21_part1(L):
	return compute(*parse(L, 'root', ignore = ''))

def parse(L, expr, ignore = 'humn'):
	if expr == ignore:
		return expr
	
	res = L[expr]
	if isinstance(res,int):
		return res
	else:
		return [parse(L,res[0],ignore), res[1], parse(L,res[2],ignore)]

def compute(a, op, b):
	if isinstance(a, list):
		a = compute(*a)
	if isinstance(b, list):
		b = compute(*b)
	match op:
		case '+':
			return a + b
		case '-':
			return a - b
		case '*':
			return a * b
		case '//':
			return a // b

def contains_human(g):
	if isinstance(g, int):
		return False
	elif isinstance(g, str):
		return True
	else:
		return contains_human(g[0]) or contains_human(g[2])

def day21_part2(L):
	LHS = parse(L, L['root'][0])
	if contains_human(LHS):
		RHS = compute(*parse(L, L['root'][2]))
	else:
		RHS = compute(*LHS)
		LHS = parse(L, L['root'][2])
	#LHS always contains humn, RHS is num
	
	a, op, b = LHS
	while True:
		if contains_human(a):
			if isinstance(b, list):
				b = compute(*b)
			match op:
				case '+':
					RHS -= b
				case '-':
					RHS += b
				case '*':
					RHS //= b
				case '//':
					RHS *= b
			if isinstance(a,list):
				a, op, b = a
			else:
				return RHS
		else:
			if isinstance(a, list):
				a = compute(*a)
			match op:
				case '+':
					RHS -= a
				case '-':
					RHS = a - RHS
				case '*':
					RHS //= a
				case '//':
					RHS = a // RHS
			if isinstance(b,list):
				a, op, b = b
			else:
				return RHS


result_test_1 = day21_part1(Ltest)
result_real_1 = day21_part1(Lreal)

print(result_real_1)
print(result_test_1)
try:
	ctrl_C(result_real_1)
except:
	print("cannot copy result")

result_test_2 = day21_part2(Ltest)
result_real_2 = day21_part2(Lreal)

if result_test_2 is not None:
	print()
	print(result_real_2)
	print(result_test_2)
	try:
		ctrl_C(result_real_2)
	except:
		print("cannot copy result")