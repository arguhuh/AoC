import re,itertools

infile = open("input/in19_real.txt","r")
# infile = open("input/in19_test.txt","r")
# infile = open("input/in19_test2.txt","r")

rules = []
seeds = []
for line in infile:
	if line == '\n':
		break
	rule_no, *cont = re.split('[:|] ',line.strip())
	if re.match('"[ab]"', cont[0]):
		seeds.append((int(rule_no), cont[0][1]))
	else:
		rules.append((int(rule_no), *(list(map(int,elm.split())) for elm in cont)))

lines = [line.strip() for line in infile]

def day19_part1(rules, seeds, lines):
	rule_res = [None] * (max(rules + seeds, key = lambda p: p[0])[0] + 1)
	for rule_no, seed in seeds:
		rule_res[rule_no] = seed
	while rule_res[0] is None:
		for rule_no, *patterns in rules:
			if all([rule_res[n] for n in itertools.chain(*patterns)]):
				rule_res[rule_no] = '|'.join([''.join(['('+rule_res[n]+')' for n in pattern]) for pattern in patterns])
				rules.remove((rule_no, *patterns))
				break
	Nmatch = 0
	for line in lines:
		if re.match('('+rule_res[0]+')$',line):
			Nmatch += 1
	return Nmatch

def day19_part2(rules, seeds, lines, repmax):
	rule_res = [None] * (max(rules + seeds, key = lambda p: p[0])[0] + 1)
	for rule_no, seed in seeds:
		rule_res[rule_no] = seed
	while rule_res[0] is None:
		for rule_no, *patterns in rules:
			if all([rule_res[n] for n in itertools.chain(*patterns)]):
				match rule_no:
					case 8:
						rule_res[8] = '(' + rule_res[42] + ')+'
					case 11:
						rule_res[11] = '|'.join(['(' + rule_res[42] + '){' + str(i+1) + '}(' + rule_res[31] + '){' + str(i+1) + '}' \
						for i in range(repmax)])
					case _:
						rule_res[rule_no] = '|'.join([''.join(['('+rule_res[n]+')' for n in pattern]) for pattern in patterns])
				rules.remove((rule_no, *patterns))
				break
	Nmatch = 0
	for line in lines:
		if re.match('('+rule_res[0]+')$',line):
			Nmatch += 1
	return Nmatch

print(day19_part1(rules[:], seeds, lines))
print(day19_part2(rules[:], seeds, lines, 5))