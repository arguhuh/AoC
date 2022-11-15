infile = open("input/in06_real.txt","r")
# infile = open("input/in06_test.txt","r")

#initialise population
P = [0] * 9 #populations of ages 0-8
for i in map(int,next(infile).split(',')):
	P[i] += 1

def day06_part1(P,N):
	for _ in range(N):
		P.append(P.pop(0))
		P[6] += P[8]
	return sum(P)

print(day06_part1(P[:],80))
print(day06_part1(P[:],256))
