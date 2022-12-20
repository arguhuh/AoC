from itertools import dropwhile
from more_itertools import windowed
from pyperclip import copy as ctrl_C

Lboth = []
for filename in ["input/in20_test.txt", "input/in20_real.txt"]:
	with open(filename,"r") as infile:
		L = list(map(int,map(str.strip,infile)))
		Lboth.append(L)
Ltest, Lreal = Lboth

class num():
	def __init__(self, i, N):
		self.child = None
		self.parent = None
		
		self.i = i
		self.N = N
		self.n = (i + (N-1) // 2) % (N-1) - (N-1) // 2
	
	def set_parent(self, parent):
		self.parent = parent
	def set_child(self, child):
		self.child = child
	
	def get_parent(self, n):
		ans = self
		for _ in range(-n):
			ans = ans.parent
		return ans
	def get_child(self, n):
		ans = self
		for _ in range(n):
			ans = ans.child
		return ans
	def get_family(self, n):
		n = (n + self.N // 2) % self.N - self.N // 2
		if not n:
			return self
		elif n > 0:
			return self.get_child(n)
		else:
			return self.get_parent(n)
	
	def move(self):
		if not self.n:
			return
		elif self.n > 0:
			dest_parent = self.get_child(self.n)
			dest_child = dest_parent.child
		else:
			dest_child = self.get_parent(self.n)
			dest_parent = dest_child.parent
		curr_parent = self.parent
		curr_child = self.child
		
		curr_parent.set_child(curr_child)
		curr_child.set_parent(curr_parent)
		
		self.set_parent(dest_parent)
		dest_parent.set_child(self)
		
		self.set_child(dest_child)
		dest_child.set_parent(self)

def get_sum(nums):
	N = len(nums)
	O = next(dropwhile(lambda obj: obj.i, nums))
	
	return O.get_family(1000).i + O.get_family(2000).i + O.get_family(3000).i

def create_nums(L, fact = 1):
	N = len(L)
	nums = [num(i * fact,N) for i in L]
	for p,s,c in windowed(nums + nums[:2],3):
		s.set_parent(p)
		s.set_child(c)
	
	return nums

def day20_part1(L):
	nums = create_nums(L)
	
	for obj in nums:
		obj.move()
	
	return get_sum(nums)

def day20_part2(L, key = 811589153, Nmix = 10):
	nums = create_nums(L, fact = key)
	
	for _ in range(Nmix):
		for obj in nums:
			obj.move()
	
	return get_sum(nums)


result_test_1 = day20_part1(Ltest)
result_real_1 = day20_part1(Lreal)

print(result_real_1)
print(result_test_1)
try:
	ctrl_C(result_real_1)
except:
	print("cannot copy result")

result_test_2 = day20_part2(Ltest)
result_real_2 = day20_part2(Lreal)

if result_test_2 is not None:
	print()
	print(result_real_2)
	print(result_test_2)
	try:
		ctrl_C(result_real_2)
	except:
		print("cannot copy result")