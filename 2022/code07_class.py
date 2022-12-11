from pyperclip import copy as ctrl_C

Lboth = []
for filename in ["input/in07_test.txt", "input/in07_real.txt"]:
	with open(filename,"r") as infile:
		next(infile)
		L = list(map(str.strip,infile))
		Lboth.append(L)
Ltest, Lreal = Lboth

class Folder():
	def __init__(self,parent):
		self.parent = parent
		self.children = {}
	def addChild(self,child,name):
		self.children[name] = child
	def size(self):
		return sum(child.size() for child in self.children.values())

class File():
	def __init__(self,size):
		self.size = lambda: size

def tree(L):
	root = Folder(None)
	dirs = [root]
	curr_dir = root
	for line in L:
		if line[:4] == '$ cd':
			if line[5:] == '..':
				curr_dir = curr_dir.parent
			else:
				curr_dir = curr_dir.children[line[5:]]
		elif line[0] != '$':
			if line[0] == 'd':
				_, name = line.split()
				child = Folder(curr_dir)
				curr_dir.addChild(child,name)
				dirs.append(child)
			else:
				size, name = line.split()
				child = File(int(size))
				curr_dir.addChild(child,name)
	return dirs

def sizes(L):
	dirs = tree(L)
	return [D.size() for D in dirs]

def day07_part1(L):
	return sum(i for i in sizes(L) if i <= 100000)

def day07_part2(L):
	D = sizes(L)
	return min(i for i in D if i >= D[0] - 40000000)


result_test_1 = day07_part1(Ltest)
result_real_1 = day07_part1(Lreal)

print(result_real_1)
print(result_test_1)
try:
	ctrl_C(result_real_1)
except:
	print("cannot copy result")

result_test_2 = day07_part2(Ltest)
result_real_2 = day07_part2(Lreal)

if result_test_2 is not None:
	print()
	print(result_real_2)
	print(result_test_2)
	try:
		ctrl_C(result_real_2)
	except:
		print("cannot copy result")