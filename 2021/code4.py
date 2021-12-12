infile = open("in4_real.txt","r")
# infile = open("in4_test.txt","r")

order = [int(i) for i in next(infile).strip().split(',')]
boards = []
for line in infile:
	if line == '\n':
		k = 0
		board = []
	else:
		k += 1
		board.append([int(i) for i in line.split()])
		if k == 5:
			boards.append(board)

def day4_part1(order,boards):
	inv_order = [i for i,j in sorted(enumerate(order), key = lambda p: p[1])]
	q = min(enumerate([min([max([inv_order[i] for i in row]) for row in board + list(zip(*board))]) for board in boards]), key = lambda p: p[1])
	return sum([sum([i for i in row if inv_order[i] > q[1]]) for row in boards[q[0]]]) * order[q[1]]

def day4_part2(order,boards):
	inv_order = [i for i,j in sorted(enumerate(order), key = lambda p: p[1])]
	q = max(enumerate([min([max([inv_order[i] for i in row]) for row in board + list(zip(*board))]) for board in boards]), key = lambda p: p[1])
	return sum([sum([i for i in row if inv_order[i] > q[1]]) for row in boards[q[0]]]) * order[q[1]]

def day4_part3(order,boards):
	inv_order = [i for i,j in sorted(enumerate(order), key = lambda p: p[1])]
	q = min(enumerate([min([max([inv_order[i] for i in row]) for row in board + list(zip(*board)) + [[row[i] for i, row in enumerate(board)], \
		[row[-i-1] for i, row in enumerate(board)]]]) for board in boards]), key = lambda p: p[1])
	return sum([sum([i for i in row if inv_order[i] > q[1]]) for row in boards[q[0]]]) * order[q[1]]

def day4_part4(order,boards):
	inv_order = [i for i,j in sorted(enumerate(order), key = lambda p: p[1])]
	q = max(enumerate([min([max([inv_order[i] for i in row]) for row in board + list(zip(*board)) + [[row[i] for i, row in enumerate(board)], \
		[row[-i-1] for i, row in enumerate(board)]]]) for board in boards]), key = lambda p: p[1])
	return sum([sum([i for i in row if inv_order[i] > q[1]]) for row in boards[q[0]]]) * order[q[1]]

print(day4_part1(order,boards))
print(day4_part2(order,boards))
print(day4_part3(order,boards))
print(day4_part4(order,boards))