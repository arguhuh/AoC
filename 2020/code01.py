infile = open("input/in01_real.txt","r")
# infile = open("input/in01_test.txt","r")
L = sorted([int(line.strip()) for line in infile])

def day01_part1(L,total):
	for p in reversed(L):
		target = total - p
		for q in L:
			if q == target:
				return p*q
			elif q > target:
				break

def day01_part2(L,total):
	N = len(L)
	for i in range(N):
		for j in range(i+1,N):
			target = total - L[i] - L[j]
			for k in range(j+1,N):
				if L[k] == target:
					return L[i]*L[j]*L[k]
				elif L[k] > target:
					break

def day01_recursive(L,i,ntochoose,target):
	if target < 0:
		return
	elif ntochoose == 0:
		return target == 0
	
	for j in range(i+1,len(L)):
		p = day01_recursive(L,j,ntochoose-1,target-L[j])
		if p:
			return p * L[j]
		elif p is None:
			return 0

def day01_recursive2(L,ntochoose,target):
	if target < 0:
		return
	elif ntochoose == 0:
		return target == 0
	
	for n in L:
		p = day01_recursive2(L,ntochoose-1,target-n)
		if p:
			return p * n
		elif p is None:
			return 0

print(day01_part1(L,2020))
print(day01_part2(L,2020))

print(day01_recursive(L,-1,2,2020))
print(day01_recursive(L,-1,3,2020))

print(day01_recursive2(L,2,2020))
print(day01_recursive2(L,3,2020))