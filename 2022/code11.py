from math import prod
from pyperclip import copy as ctrl_C
from copy import deepcopy

class Monkey():
	def __init__(self,block):
		self.items = list(map(int,block[1][18:].split(', ')))
		if block[2][23:] == '* old':
			self.operation = '**'
			self.number = 2
		else:
			self.operation = block[2][23]
			self.number = int(block[2][25:])
		self.test = int(block[3][21:])
		self.ondivis = int(block[4][29])
		self.onindivis = int(block[5][30])
		self.Ninspect = 0
	def add(self,item):
		self.items.append(item)
	def throw(self,item,candidates,mod):
		match self.operation:
			case '+':
				item += self.number
			case '*':
				item *= self.number
			case '**':
				item *= item
		if mod:
			item %= mod
		else:
			item //= 3
		if item % self.test:
			candidates[self.onindivis].add(item)
		else:
			candidates[self.ondivis].add(item)
	def throwall(self,candidates,mod = 0):
		self.Ninspect += len(self.items)
		while self.items:
			item = self.items.pop()
			self.throw(item,candidates,mod)

Lboth = []
for filename in ["input/in11_test.txt", "input/in11_real.txt"]:
	with open(filename,"r") as infile:
		L = [Monkey(block.split('\n')) for block in infile.read().split('\n\n')]
		Lboth.append(L)
Ltest, Lreal = Lboth

def day11_part1(L,Nrounds = 20):
	for _ in range(Nrounds):
		for monkey in L:
			monkey.throwall(L)
	return prod(sorted(monkey.Ninspect for monkey in L)[-2:])

def day11_part2(L,Nrounds = 10000):
	mod = prod(monkey.test for monkey in L)
	for _ in range(Nrounds):
		for monkey in L:
			monkey.throwall(L,mod)
	return prod(sorted(monkey.Ninspect for monkey in L)[-2:])
	

result_test_1 = day11_part1(deepcopy(Ltest))
result_real_1 = day11_part1(deepcopy(Lreal))

print(result_real_1)
print(result_test_1)
try:
	ctrl_C(result_real_1)
except:
	print("cannot copy result")

result_test_2 = day11_part2(Ltest)
result_real_2 = day11_part2(Lreal)

if result_test_2 is not None:
	print()
	print(result_real_2)
	print(result_test_2)
	try:
		ctrl_C(result_real_2)
	except:
		print("cannot copy result")