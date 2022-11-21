import itertools

infile = open("input/in09_real.txt","r"); window = 25
# infile = open("input/in09_test.txt","r"); window = 5
L = [int(line.strip()) for line in infile]

def day09_part1(L,window):
	for i in range(window,len(L)):
		if all([p + q != L[i] for p,q in itertools.combinations(L[i-window:i],2)]):
			return L[i]
			
def day09_part2(L,window):
	N0 = day09_part1(L,window)
	for i in range(len(L)):
		k = 2
		S = L[i] + L[i+1]
		while S < N0:
			k += 1
			S = sum(L[i:i+k])
		if S == N0:
			return min(L[i:i+k]) + max(L[i:i+k])

print(day09_part1(L,window))
print(day09_part2(L,window))