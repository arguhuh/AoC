import pyperclip

Lboth = []
for filename in ["input/in01_test.txt", "input/in01_real.txt"]:
	with open(filename,"r") as infile:
		L = [list(map(int,grp.split('\n'))) for grp in infile.read().split('\n\n')]
		Lboth.append(L)
Ltest, Lreal = Lboth

def day01_part1(L):
	return max(sum(row) for row in L)

def day01_part2(L):
	return sum(sorted(sum(row) for row in L)[-3:])


result_test_1 = day01_part1(Ltest)
result_real_1 = day01_part1(Lreal)

print(result_test_1)
print(result_real_1)
pyperclip.copy(result_real_1)

result_test_2 = day01_part2(Ltest)
result_real_2 = day01_part2(Lreal)

if result_test_2 is not None:
	print()
	print(result_test_2)
	print(result_real_2)
	pyperclip.copy(result_real_2)