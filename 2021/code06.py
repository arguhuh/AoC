infile = open("in6_real.txt","r")
# infile = open("in6_test.txt","r")
L = [int(i) for i in next(infile).split(',')]

def day6_part1(L,N):
	P = [0] * 9 #populations of ages 0-8
	for i in L:
		P[i] += 1
	for x in range(N):
		P.append(P.pop(0))
		P[6] += P[8]
	return sum(P)

print(day6_part1(L,80))
print(day6_part1(L,256))