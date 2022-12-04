import pyperclip

Lboth = []
for filename in ["input/in03_test.txt", "input/in03_real.txt"]:
	with open(filename,"r") as infile:
		L = list(map(str.strip,infile))
		Lboth.append(L)
Ltest, Lreal = Lboth

def pri(n):
	o = ord(n)
	if o >= ord('a'):
		return o - ord('a') + 1
	else:
		return o - ord('A') + 27

def day03_part1(L):
	S = 0
	for sack in L:
		n2 = len(sack) // 2
		for c in sack[:n2]:
			if c in sack[n2:]:
				S += pri(c)
				break
	return S

def day03_part2(L):
	S = 0
	while L:
		p, q, r, *L = L
		for c in p:
			if c in q and c in r:
				S += pri(c)
				break
	return S


result_test_1 = day03_part1(Ltest)
result_real_1 = day03_part1(Lreal)

print(result_test_1)
print(result_real_1)
pyperclip.copy(result_real_1)

result_test_2 = day03_part2(Ltest)
result_real_2 = day03_part2(Lreal)

if result_test_2 is not None:
	print()
	print(result_test_2)
	print(result_real_2)
	pyperclip.copy(result_real_2)