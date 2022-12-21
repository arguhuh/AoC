from pyperclip import copy as ctrl_C

Lboth = []
for filename in ["input/in21_test.txt", "input/in21_real.txt"]:
	with open(filename,"r") as infile:
		L = [(a,b.split() if ' ' in b else int(b)) for a,b in [line.split(': ') for line in map(str.strip,infile)]]
		Lboth.append(L)
Ltest, Lreal = Lboth

def day21_part1(L):
	D = dict(L)
	while any(isinstance(v,list) for v in D.values()):
		for name, num in D.items():
			if isinstance(num,list):
				a, op, b = num
				if isinstance(D[a],int) and isinstance(D[b],int):
					match op:
						case '+':
							D[name] = D[a] + D[b]
						case '-':
							D[name] = D[a] - D[b]
						case '*':
							D[name] = D[a] * D[b]
						case '/':
							D[name] = D[a] // D[b]
	return D['root']

def parse(D, expr):
	if expr == 'D["humn"]':
		return expr
	
	res = D[expr[3:-2]]
	if isinstance(res,int):
		return res
	else:
		return [parse(D,res[0]), res[1], parse(D,res[2])]

def contains_human(g):
	if isinstance(g, int):
		return False
	elif isinstance(g, str):
		return True
	else:
		return contains_human(g[0]) or contains_human(g[2])

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

def day21_part2(L):
	D = dict((a,b if isinstance(b,int) else [f'D["{b[0]}"]', b[1] if b[1] != '/' else '//', f'D["{b[2]}"]']) if a != 'root' else (a, [f'D["{b[0]}"]', f'D["{b[2]}"]']) for a,b in L)
	
	LHS = parse(D, D['root'][0])
	if contains_human(LHS):
		RHS = compute(*parse(D, D['root'][1]))
	else:
		RHS = compute(*LHS)
		LHS = parse(D, D['root'][1])
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