L_test1 = [0,3,6]
L_test2 = [1,3,2]
L_test3 = [2,1,3]
L_test4 = [1,2,3]
L_test5 = [2,3,1]
L_test6 = [3,2,1]
L_test7 = [3,1,2]
L_real = [0,3,1,6,7,5]

def day15_part1(L,target):
	D = {n:[i] for i,n in enumerate(L[:-1])}
	prev = L[-1]
	for pos in range(len(L)-1,target-1):
		if prev in D:
			D[prev].append(pos)
			prev = pos - D[prev][-2]
		else:
			D[prev] = [pos]
			prev = 0
	return prev

print(day15_part1(L_test1,2020))
print(day15_part1(L_test2,2020))
print(day15_part1(L_test3,2020))
print(day15_part1(L_test4,2020))
print(day15_part1(L_test5,2020))
print(day15_part1(L_test6,2020))
print(day15_part1(L_test7,2020))
print(day15_part1(L_real,2020))
print(day15_part1(L_real,30_000_000))