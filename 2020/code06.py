import re

infile = open("input/in06_real.txt","r")
# infile = open("input/in06_test.txt","r")

groups = []
group = []
for line in infile:
	if line == '\n':
		groups.append(group)
		group = []
	else:
		group.append(line.strip())
groups.append(group)

def day06_part1(groups):
	return sum([len(set(''.join(g))) for g in groups])

def day06_part2(groups):
	return sum([sum([all([re.match(f'.*{c}',p) for p in g[1:]]) for c in g[0]]) for g in groups])

print(day06_part1(groups))
print(day06_part2(groups))