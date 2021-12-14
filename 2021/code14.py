infile = open("input/in14_real.txt","r")
# infile = open("input/in14_test.txt","r")
s = next(infile).strip()
next(infile)
repdict = {m: [''.join([m[0],i]),''.join([i,m[1]])] for m,i in [line.strip().split(' -> ') for line in infile]}
countdict = {m: 0 for m in repdict}
for s1,s2 in zip(s,s[1:]):
	countdict[s1+s2] += 1
ends = s[0]+s[-1]

def rep(countdict,repdict):
	dcountdict = dict.fromkeys(countdict,0)
	for oldkey,value in countdict.items():
		newkey1, newkey2 = repdict[oldkey]
		dcountdict[oldkey] -= value
		dcountdict[newkey1] += value
		dcountdict[newkey2] += value
	return {key: value + dcountdict[key] for key,value in countdict.items()}

def repN(s,countdict,repdict,Nrep,ends):
	for irep in range(Nrep):
		countdict = rep(countdict,repdict)
	counts = dict.fromkeys(set(''.join(countdict.keys())),0)
	for key,value in countdict.items():
		counts[key[0]] += value
		counts[key[1]] += value
	counts[ends[0]] += 1
	counts[ends[1]] += 1
	counts = {key: value//2 for key,value in counts.items()}
	return max(counts.values()) - min(counts.values())

def day14_part1(s,countdict,repdict,ends):
	return repN(s,countdict,repdict,10,ends)

def day14_part2(s,countdict,repdict,ends):
	return repN(s,countdict,repdict,40,ends)

print(day14_part1(s,countdict,repdict,ends))
print(day14_part2(s,countdict,repdict,ends))