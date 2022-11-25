infile = open("input/in18_real.txt","r")
# infile = open("input/in18_test.txt","r")
L = [[c if c in '+*()' else int(c) for c in ''.join(line.split())] for line in infile]

def compute(expr,flat_computer):
	while '(' in expr:
		stop = 0
		for start,p in enumerate(expr):
			if p == '(':
				for stopcandidate,q in enumerate(expr[start+1:]):
					match q:
						case '(':
							break
						case ')':
							stop = stopcandidate + start + 2
							break
				if stop:
					break
		expr[start:stop] = [flat_computer(expr[start+1:stop-1])]
	return flat_computer(expr)

def flat_compute(expr):
	while len(expr) > 1:
		a, op, b = expr[:3]
		match op:
			case '+':
				expr[:3] = [a + b]
			case '*':
				expr[:3] = [a * b]
	return expr[0]

def day18_part1(L):
	S = 0
	for expr in L:
		result = compute(expr[:],flat_compute)
		S += result
	return S

def flat_compute2(expr):
	while '+' in expr:
		iop = expr.index('+')
		expr[iop-1:iop+2] = [expr[iop-1] + expr[iop+1]]
	while '*' in expr:
		iop = expr.index('*')
		expr[iop-1:iop+2] = [expr[iop-1] * expr[iop+1]]
	return expr[0]

def day18_part2(L):
	S = 0
	for expr in L:
		result = compute(expr[:],flat_compute2)
		S += result
	return S

print(day18_part1(L))
print(day18_part2(L))