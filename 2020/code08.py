infile = open("input/in08_real.txt","r")
# infile = open("input/in08_test.txt","r")
L = [(instr,int(value)) for instr,value in map(str.split,infile)]

def day08_part1(L):
	accumulator = p = 0
	visited = [False] * len(L)
	while not visited[p]:
		visited[p] = True
		instr,value = L[p]
		match instr:
			case 'nop':
				p += 1
			case 'acc':
				accumulator += value
				p += 1
			case 'jmp':
				p += value
			case _:
				return
	return accumulator

def day08_part2(L):
	for q in range(len(L)):
		if L[q][0] != 'acc':
			accumulator = p = 0
			visited = [False] * len(L)
			while p < len(L):
				if visited[p]:
					break
				visited[p] = True
				instr,value = L[p]
				if p == q:
					match instr:
						case 'nop':
							p += value
						case 'jmp':
							p += 1
						case _:
							return
				else:
					match instr:
						case 'nop':
							p += 1
						case 'acc':
							accumulator += value
							p += 1
						case 'jmp':
							p += value
						case _:
							return
			if p == len(L):
				return accumulator

print(day08_part1(L))
print(day08_part2(L))