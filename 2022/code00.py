import re, itertools, math

Lboth = []
for filename in ["input/in##_test.txt", "input/in##_real.txt"]:
	with open(filename,"r") as infile:
		L = [line for line in map(str.strip,infile)]
		
		# L = [int(line) for line in map(str.strip,infile)]
		
		# L = [[i for i in line] for line in map(str.split,infile)]
		
		# L = [[int(i) for i in line] for line in map(str.split,infile)]
		
		# L = [(a,b) for a,b in map(str.split,infile)]
		
		# L = []
		# row = []
		# for line in map(str.strip,infile):
			# if len(line):
				# row.append(line)
			# else:
				# L.append(row)
				# row = []
		# if len(row):
			# L.append(row)
		
		# L = []
		# row = []
		# for line in map(str.strip,infile):
			# if len(line):
				# row.append(int(line))
			# else:
				# L.append(row)
				# row = []
		# if len(row):
			# L.append(row)
		
		# L = []
		# row = []
		# for line in map(str.split,infile):
			# if len(line):
				# row.append([i for i in line])
			# else:
				# L.append(row)
				# row = []
		# if len(row):
			# L.append(row)
		
		# L = []
		# row = []
		# for line in map(str.split,infile):
			# if len(line):
				# row.append([int(i) for i in line])
			# else:
				# L.append(row)
				# row = []
		# if len(row):
			# L.append(row)
		
		# L = []
		# row = []
		# for a,b in map(str.split,infile):
			# if len(line):
				# row.append((a,b))
			# else:
				# L.append(row)
				# row = []
		# if len(row):
			# L.append(row)
		
		Lboth.append(L)
Ltest, Lreal = Lboth

def day##_part1(L):
	return L

def day##_part2(L):
	return L

print(day##_part1(Ltest))
print(day##_part1(Lreal))
# print()
# print(day##_part2(Ltest))
# print(day##_part2(Lreal))