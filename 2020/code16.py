import re

infile = open("input/in16_real.txt","r")
# infile = open("input/in16_test.txt","r")
# infile = open("input/in16_test2.txt","r")

invalid_numbers = [True] * 1000
rules = []
for line in infile:
	if line == '\n':
		break
	[rule, *ranges] = re.split(': | or |-',line.strip())
	p,q,r,s = map(int,ranges)
	rules.append((rule, [p,q,r,s]))
	invalid_numbers[p:q+1] = [False] * (q - p + 1)
	invalid_numbers[r:s+1] = [False] * (s - r + 1)

next(infile)#heading
my_ticket = [int(n) for n in next(infile).strip().split(',')]
next(infile)
next(infile)

S = 0
tickets = []
for line in infile:
	ticket = list(map(int,line.strip().split(',')))
	invalid_list = [n for n in ticket if invalid_numbers[n]]
	if len(invalid_list):
		S += sum(invalid_list)
	else:
		tickets.append(ticket)
print(S)

Nfields = len(rules)
fieldcanbeindex = {field: [True] * Nfields for field,_ in rules}
for ticket in tickets:
	for field, [p,q,r,s] in rules:
		for i in range(Nfields):
			if fieldcanbeindex[field][i] and \
			not (p <= ticket[i] <= q or r <= ticket[i] <= s):
				fieldcanbeindex[field][i] = False

fieldisindex = {field: None for field,_ in rules}
while len(fieldcanbeindex):
	for key, value in fieldcanbeindex.items():
		if sum(value) == 1:
			i = value.index(True)
			fieldisindex[key] = i
			del fieldcanbeindex[key]
			for k in fieldcanbeindex:
				fieldcanbeindex[k][i] = False
			break

p = 1
for key, i in fieldisindex.items():
	if re.match('departure', key):
		p *= my_ticket[fieldisindex[key]]
print(p)