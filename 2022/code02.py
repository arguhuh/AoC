import pyperclip

Lboth = []
for filename in ["input/in02_test.txt", "input/in02_real.txt"]:
	with open(filename,"r") as infile:
		L = list(map(str.split,infile))
		Lboth.append(L)
Ltest, Lreal = Lboth

def day02_part1(L):
	S = 0
	for a,b in L:
		match a:
			case 'A':
				match b:
					case 'X':
						S += 3
						S += 1
					case 'Y':
						S += 6
						S += 2
					case 'Z':
						S += 3
			case 'B':
				match b:
					case 'X':
						S += 1
					case 'Y':
						S += 3
						S += 2
					case 'Z':
						S += 6
						S += 3
			case 'C':
				match b:
					case 'X':
						S += 6
						S += 1
					case 'Y':
						S += 2
					case 'Z':
						S += 3
						S += 3
	return S

def day02_part2(L):
	S = 0
	for a,b in L:
		match a:
			case 'A':
				match b:
					case 'Y':
						S += 3
						S += 1
					case 'Z':
						S += 6
						S += 2
					case 'X':
						S += 3
			case 'B':
				match b:
					case 'X':
						S += 1
					case 'Y':
						S += 3
						S += 2
					case 'Z':
						S += 6
						S += 3
			case 'C':
				match b:
					case 'Z':
						S += 6
						S += 1
					case 'X':
						S += 2
					case 'Y':
						S += 3
						S += 3
	return S


result_test_1 = day02_part1(Ltest)
result_real_1 = day02_part1(Lreal)

print(result_test_1)
print(result_real_1)
pyperclip.copy(result_real_1)

result_test_2 = day02_part2(Ltest)
result_real_2 = day02_part2(Lreal)

if result_test_2 is not None:
	print()
	print(result_test_2)
	print(result_real_2)
	pyperclip.copy(result_real_2)