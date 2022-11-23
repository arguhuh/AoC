import re

infile = open("input/in14_real.txt","r")
# infile = open("input/in14_test.txt","r")
# infile = open("input/in14_test2.txt","r")
L = [re.split('\[|]? = ',line.strip()) for line in infile]

def day14_part1(L):
	Dlist = []
	for [inst, *values] in L:
		match inst:
			case 'mask':
				mask = values[0]
			case 'mem':
				key, unmasked = values
				masked = int(''.join([n if m == 'X' else m for m,n in \
				zip(mask, bin(int(unmasked))[2:].rjust(36,'0'))]),2)
				Dlist.append((key, masked))
	return sum(dict(Dlist).values())

def day14_part2(L):
	Dlist = []
	for [inst, *values] in L:
		match inst:
			case 'mask':
				mask = values[0]
			case 'mem':
				unmasked, value = values
				masked = [n if m == '0' else m for m,n in \
				zip(mask, bin(int(unmasked))[2:].rjust(36,'0'))]
				floaters = [i for i,c in enumerate(masked) if c == 'X']
				Nfloaters = len(floaters)
				for overwrite in range(2**Nfloaters):
					for f,o in zip(floaters,bin(overwrite)[2:].rjust(Nfloaters,'0')):
						masked[f] = o
					Dlist.append((int(''.join(masked),2), int(value)))
	return sum(dict(Dlist).values())

print(day14_part1(L))
print(day14_part2(L))