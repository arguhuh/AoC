infile = open("input/in04_real.txt","r")
# infile = open("input/in04_test.txt","r")

when_called = [i for i,j in sorted(enumerate(map(int,next(infile).strip().split(','))), key = lambda p: p[1])]

boards = []
for line in infile:
	if line == '\n':
		k = 0
		board = []
	else:
		k += 1
		board.append([(n,when_called[n]) for n in map(int,line.split())])
		if k == 5:
			boards.append(board)

def sum_board(board,T):
	total = 0
	for row in board:
		for n,t in row:
			if t > T:
				total += n
	return total
	# return sum([n for row in board for n,t in row if t > T])

def day04_part1_with_diags(boards):
	ID, (N, T) = min(enumerate([min([max(row, key = lambda p: p[1]) for row in board + list(zip(*board)) + [[row[i] for i, row in enumerate(board)], \
		[row[-i-1] for i, row in enumerate(board)]]], key = lambda p: p[1]) for board in boards]), key = lambda p: p[1][1])
	return sum_board(boards[ID],T) * N

def day04_part2_with_diags(boards):
	ID, (N, T) = max(enumerate([min([max(row, key = lambda p: p[1]) for row in board + list(zip(*board)) + [[row[i] for i, row in enumerate(board)], \
		[row[-i-1] for i, row in enumerate(board)]]], key = lambda p: p[1]) for board in boards]), key = lambda p: p[1][1])
	return sum_board(boards[ID],T) * N

print(day04_part1_with_diags(boards))
print(day04_part2_with_diags(boards))