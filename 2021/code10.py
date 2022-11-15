infile = open("input/in10_real.txt","r")
# infile = open("input/in10_test.txt","r")
L = [list(line.strip()) for line in infile]

def first_illegal(s):
	type = {"(":"l",")":"r","[":"l","]":"r","{":"l","}":"r","<":"l",">":"r"}
	pair = {")":"(","]":"[","}":"{",">":"<"}
	i = 1
	while i < len(s):
		if type[s[i]] == 'r':
			if pair[s[i]] == s[i-1]:
				s[i-1:i+1] = []
				i -= 1
			else:
				return s[i]
		else:
			i += 1
	return None

def day10_part1(L):
	score = {None: 0, ")": 3, "]": 57, "}": 1197, ">": 25137}
	return sum([score[first_illegal(s)] for s in L])

def complete_line(s):
	type = {"(":"l",")":"r","[":"l","]":"r","{":"l","}":"r","<":"l",">":"r"}
	pair = {"(":")","[":"]","{":"}","<":">"}
	i = len(s)-1
	ending = ''
	while i >= 0:
		if type[s[i]] == 'l':
			if i == len(s)-1:
				ending += pair[s[-1]]
				s[-1:] = []
			else:
				if pair[s[i]] == s[i+1]:
					s[i:i+2] = []
				else:
					return None
		i -= 1
	return ending

def score_completion(s):
	score = {")": 1, "]": 2, "}": 3, ">": 4}
	S = 0
	for c in s:
		S *= 5
		S += score[c]
	return S

def day10_part2(L):
	C = [complete_line(s) for s in L]
	S = [score_completion(s) for s in C if s != None]
	return sorted(S)[len(S)//2]

print(day10_part1(L))
print(day10_part2(L))
