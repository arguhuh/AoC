infile = open("input/in02_real.txt","r")
# infile = open("input/in02_test.txt","r")
L = [list(map(int,a.split('-'))) + [b[:-1], c] for a,b,c in map(str.split,infile)]

def day02_part1(L):
	return sum([1 for a,b,c,d in L if a <= sum([1 for t in d if t == c]) <= b])

def day02_part2(L):
	return sum([1 for a,b,c,d in L if (d[a-1]==c) != (d[b-1]==c)])



# def day02_part1(L):
	# Nmatch = 0
	# for a,b,c,d in L:
		# print(f'{c}{{{a},{b}}}')
		# print(d)
		# if re.search(f'{c}{{{a},{b}}}',d):
			# Nmatch += 1
			# print('match')
	# return Nmatch

print(day02_part1(L))
print(day02_part2(L))