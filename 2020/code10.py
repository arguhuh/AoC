import itertools,math

infile = open("input/in10_real.txt","r")
# infile = open("input/in10_test.txt","r")
# infile = open("input/in10_test2.txt","r")
L = sorted([0] + [int(line.strip()) for line in infile])
L.append(L[-1] + 3)

def day10_part1(L):
	return \
	sum(q == p+1 for p,q in itertools.pairwise(L)) * \
	sum(q == p+3 for p,q in itertools.pairwise(L))

def combs(N): #OEIS A000073 - tribonacci sequence
	p = q = 0
	r = 1
	for _ in range(N):
		s = p+q+r
		p = q
		q = r
		r = s
	return r

# def day10_part2(L):
	# total = 0
	# return math.prod(map(combs, \
	# [(total := total + 1) * 0 if q == p+1 \
	# else total + (total := 0) for p,q in itertools.pairwise(L)]))

def day10_part2(L):
	streak = 0
	ans = 1
	for p,q in itertools.pairwise(L):
		if q == p + 1:
			streak += 1
		else:
			ans *= combs(streak)
			streak = 0
	return ans

print(day10_part1(L))
print(day10_part2(L))