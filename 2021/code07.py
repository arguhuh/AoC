infile = open("in7_real.txt","r")
# infile = open("in7_test.txt","r")
L = [int(i) for i in next(infile).split(',')]

def cost1(L,p):
	return sum([abs(i-p) for i in L])

def day7_part1(L):
	C = float("inf")
	P = float("nan")
	for p in list(range(min(L),max(L)+1)):
		c = cost1(L,p)
		if c < C:
			C = c
			P = p
		#C = min(C,cost(L,p))
	return (C,P)

def cost2(L,p):
	return sum([abs(i-p)*(abs(i-p)+1)/2 for i in L])

def day7_part2(L):
	C = float("inf")
	P = float("nan")
	for p in list(range(min(L),max(L)+1)):
		c = cost2(L,p)
		if c < C:
			C = c
			P = p
		#C = min(C,cost(L,p))
	return (C,P)

print(day7_part1(L))
print(day7_part2(L))