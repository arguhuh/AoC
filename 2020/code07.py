import re

with open("input/in07_real.txt","r") as infile:
# with open("input/in07_test.txt","r") as infile:
# with open("input/in07_test2.txt","r") as infile:
	L = [re.split(' bags contain | bags?, | bags?.',line.strip())[:-1] for line in infile]

def day07_part1(L):
	D = {rule[0]:None for rule in L}
	D['shiny gold'] = 1 #remember to discount this at the end
	for [rule, firstbag, *otherbags] in L:
		if firstbag == 'no other':
			D[rule] = 0
	while any(v is None for v in D.values()):
		for [rule, *bags] in L:
			if D[rule] is None:
				if any(D[bag[2:]] for bag in bags):
					D[rule] = 1
				elif all(D[bag[2:]]==0 for bag in bags):
					D[rule] = 0
	return sum(D.values()) - 1

def day07_part2(L):
	D = {rule[0]:None for rule in L}
	for [rule, firstbag, *otherbags] in L:
		if firstbag == 'no other':
			D[rule] = 1
	while D['shiny gold'] is None:
		for [rule, *bags] in L:
			if D[rule] is None and all(D[bag[2:]] is not None for bag in bags):
				D[rule] = sum(int(bag[0]) * D[bag[2:]] for bag in bags) + 1
	return D['shiny gold'] - 1

print(day07_part1(L))
print(day07_part2(L))