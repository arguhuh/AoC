from pyperclip import copy as ctrl_C
from numpy import sign

Lboth = []
for filename in ["input/in09_test.txt", "input/in09_real.txt"]:
	with open(filename,"r") as infile:
		L = [(a,int(b)) for a,b in map(str.split,infile)]
		Lboth.append(L)
Ltest, Lreal = Lboth

def day09_part2(L,Nk = 10):
	xs = [0] * Nk
	ys = [0] * Nk
	visited = [(0,0)]
	for d,dist in L:
		for _ in range(dist):
			match d:
				case 'R':
					xs[0] += 1
				case 'L':
					xs[0] -= 1
				case 'U':
					ys[0] += 1
				case 'D':
					ys[0] -= 1
			for k in range(1,Nk):
				xd = xs[k-1]-xs[k]
				yd = ys[k-1]-ys[k]
				if max(abs(xd),abs(yd)) > 1:
					xs[k] += sign(xd)
					ys[k] += sign(yd)
			visited.append((xs[-1],ys[-1]))
	return len(set(visited))


result_test_1 = day09_part2(Ltest,Nk = 2)
result_real_1 = day09_part2(Lreal,Nk = 2)

print(result_real_1)
print(result_test_1)
try:
	ctrl_C(result_real_1)
except:
	print("cannot copy result")

result_test_2 = day09_part2(Ltest)
result_real_2 = day09_part2(Lreal)

if result_test_2 is not None:
	print()
	print(result_real_2)
	print(result_test_2)
	try:
		ctrl_C(result_real_2)
	except:
		print("cannot copy result")