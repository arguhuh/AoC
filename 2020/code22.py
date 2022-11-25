infile = open("input/in22_real.txt","r")
# infile = open("input/in22_test.txt","r")

p1 = []
next(infile)
for line in infile:
	if line == '\n':
		break
	p1.append(int(line.strip()))

p2 = []
next(infile)
for line in infile:
	if line == '\n':
		break
	p2.append(int(line.strip()))

def score(p):
	return sum([n*(i+1) for i,n in enumerate(reversed(p))])

def day22_part1(p1,p2):
	while len(p1) and len(p2):
		c1 = p1.pop(0)
		c2 = p2.pop(0)
		if c1 > c2:
			p1.extend([c1,c2])
		else:
			p2.extend([c2,c1])
	if len(p1):
		return score(p1)
	else:
		return score(p2)

def day22_part2(p1,p2,depth,Nmax):
	Nturns = 0
	while len(p1) and len(p2):
		Nturns += 1
		if Nturns > Nmax: #probably repeating, call it quits
			return True
		c1 = p1.pop(0)
		c2 = p2.pop(0)
		if len(p1) >= c1 and len(p2) >= c2:
			if day22_part2(p1[:c1],p2[:c2],depth + 1,Nmax):
				p1.extend([c1,c2])
			else:
				p2.extend([c2,c1])
		else:
			if c1 > c2:
				p1.extend([c1,c2])
			else:
				p2.extend([c2,c1])
	if depth:
		if len(p1):
			return True
		else:
			return False
	else:
		if len(p1):
			return score(p1)
		else:
			return score(p2)

print(day22_part1(p1[:],p2[:]))
print(day22_part2(p1[:],p2[:],0,600))