infile = open("input/in08_real.txt","r")
# infile = open("input/in08_test.txt","r")
L = infile.readlines()

def day08_part1(L):
	return sum([sum([1 for s in line.split('|')[1].strip().split() if len(s) < 5 or len(s) == 7]) for line in L])

#e is the one that appears in 4 digits
#b is the one that appears in 6 digits
#f is the one that appears in 9 digits
#c is the other one that appears in the digit with 2 segments
#a is the other one that appears in the digit with 3 segments
#d is the other one that appears in the digit with 4 segments
#g is the only remaining one

def day08_part2(L):
	cv = "abcdefg"
	ss = {
		"abcefg": '0',
		"cf": '1',
		"acdeg": '2',
		"acdfg": '3',
		"bcdf": '4',
		"abdfg": '5',
		"abdefg": '6',
		"acf": '7',
		"abcdefg": '8',
		"abcdfg": '9'
	}
	T = 0
	for line in L:
		A,B = map(str.split, line.strip().split('|'))
		connections = [None] * 7
		Ndig = [0] * 7
		for s in A:
			for c in s:
				Ndig[cv.index(c)] += 1
		connections[Ndig.index(4)] = 'e'
		connections[Ndig.index(6)] = 'b'
		connections[Ndig.index(9)] = 'f'
		connections[cv.index([c for c in [s for s in A if len(s) == 2][0] if connections[cv.index(c)]==None][0])] = 'c'
		connections[cv.index([c for c in [s for s in A if len(s) == 3][0] if connections[cv.index(c)]==None][0])] = 'a'
		connections[cv.index([c for c in [s for s in A if len(s) == 4][0] if connections[cv.index(c)]==None][0])] = 'd'
		connections[connections.index(None)] = 'g'
		correct_digits = [[connections[cv.index(c)] for c in s] for s in B]
		T += int(''.join([ss[''.join(sorted(d))] for d in correct_digits]))
	return T

print(day08_part1(L))
print(day08_part2(L))