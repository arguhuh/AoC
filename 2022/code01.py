Lboth = []
for filename in ["input/in01_test.txt", "input/in01_real.txt"]:
	with open(filename,"r") as infile:
		L = []
		row = []
		for line in map(str.strip,infile):
			if len(line):
				row.append(int(line))
			else:
				L.append(row)
				row = []
		if len(row):
			L.append(row)
		Lboth.append(L)
Ltest, Lreal = Lboth

def day01_part1(L):
	return max(sum(row) for row in L)

def day01_part2(L):
	return sum(sorted(sum(row) for row in L)[-3:])

print(day01_part1(Ltest))
print(day01_part1(Lreal))
print()
print(day01_part2(Ltest))
print(day01_part2(Lreal))