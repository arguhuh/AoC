import math, itertools

infile = open("input/in13_real.txt","r")
# infile = open("input/in13_test.txt","r")
T = int(next(infile).strip())
L = [(int(n),i) for i,n in enumerate(next(infile).split(',')) if n != 'x']

def day13_part1(L,T):
	return math.prod(min([(n, -T % n) for n,_ in L], key = lambda p: p[1]))

def day13_part2(L):
	T = 0
	F = 1
	for k, s in L:
		N = next(filter(lambda n: not (F*n + T + s) % k, itertools.count()))
		T += F*N
		F *= k
	return T

print(day13_part1(L,T))
print(day13_part2(L))