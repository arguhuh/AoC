from random import randrange, choice
from itertools import product
from pyperclip import copy as ctrl_C

def grid(message):
	screen = [['.' for _ in range(40)] for _ in range(6)]
	offset = 0
	for c in message:
		match c:
			case ' ':
				char = [\
						'.',\
						'.',\
						'.',\
						'.',\
						'.',\
						'.' \
						]
			case 'A':
				char = [\
						'.##.',\
						'#..#',\
						'#..#',\
						'####',\
						'#..#',\
						'#..#' \
						]
			case 'B':
				char = [\
						'###.',\
						'#..#',\
						'###.',\
						'#..#',\
						'#..#',\
						'###.' \
						]
			case 'C':
				char = [\
						'.###',\
						'#...',\
						'#...',\
						'#...',\
						'#...',\
						'.###' \
						]
			case 'D':
				char = [\
						'###.',\
						'#..#',\
						'#..#',\
						'#..#',\
						'#..#',\
						'###.' \
						]
			case 'E':
				char = [\
						'####',\
						'#...',\
						'###.',\
						'#...',\
						'#...',\
						'####' \
						]
			case 'F':
				char = [\
						'####',\
						'#...',\
						'###.',\
						'#...',\
						'#...',\
						'#...' \
						]
			case 'G':
				char = [\
						'.##.',\
						'#..#',\
						'#...',\
						'#.##',\
						'#..#',\
						'.###' \
						]
			case 'H':
				char = [\
						'#..#',\
						'#..#',\
						'####',\
						'#..#',\
						'#..#',\
						'#..#' \
						]
			case 'I':
				char = [\
						'###',\
						'.#.',\
						'.#.',\
						'.#.',\
						'.#.',\
						'###' \
						]
			case 'J':
				char = [\
						'####',\
						'..#.',\
						'..#.',\
						'..#.',\
						'#.#.',\
						'###.' \
						]
			case 'K':
				char = [\
						'#..#',\
						'#.#.',\
						'##..',\
						'##..',\
						'#.#.',\
						'#..#' \
						]
			case 'L':
				char = [\
						'#...',\
						'#...',\
						'#...',\
						'#...',\
						'#...',\
						'####' \
						]
			case 'M':
				char = [\
						'#...#',\
						'##.##',\
						'#.#.#',\
						'#.#.#',\
						'#.#.#',\
						'#.#.#' \
						]
			case 'N':
				char = [\
						'#..#',\
						'##.#',\
						'##.#',\
						'#.##',\
						'#.##',\
						'#..#' \
						]
			case 'O':
				char = [\
						'.##.',\
						'#..#',\
						'#..#',\
						'#..#',\
						'#..#',\
						'.##.' \
						]
			case 'P':
				char = [\
						'###.',\
						'#..#',\
						'#..#',\
						'###.',\
						'#...',\
						'#...' \
						]
			case 'Q':
				char = [\
						'.##.',\
						'#..#',\
						'#..#',\
						'#..#',\
						'#.##',\
						'.###' \
						]
			case 'R':
				char = [\
						'###.',\
						'#..#',\
						'#..#',\
						'###.',\
						'#..#',\
						'#..#' \
						]
			case 'S':
				char = [\
						'.###',\
						'#...',\
						'.##.',\
						'...#',\
						'...#',\
						'###.' \
						]
			case 'T':
				char = [\
						'#####',\
						'..#..',\
						'..#..',\
						'..#..',\
						'..#..',\
						'..#..' \
						]
			case 'U':
				char = [\
						'#..#',\
						'#..#',\
						'#..#',\
						'#..#',\
						'#..#',\
						'.##.' \
						]
			case 'V':
				char = [\
						'#...#',\
						'#...#',\
						'#...#',\
						'.#.#.',\
						'.#.#.',\
						'..#..' \
						]
			case 'W':
				char = [\
						'#.#.#',\
						'#.#.#',\
						'#.#.#',\
						'#.#.#',\
						'##.##',\
						'.#.#.' \
						]
			case 'X':
				char = [\
						'#..#',\
						'#..#',\
						'.##.',\
						'.##.',\
						'#..#',\
						'#..#' \
						]
			case 'Y':
				char = [\
						'#...#',\
						'#...#',\
						'.#.#.',\
						'..#..',\
						'..#..',\
						'..#..' \
						]
			case 'Z':
				char = [\
						'####',\
						'...#',\
						'..#.',\
						'.#..',\
						'#...',\
						'####' \
						]
		if offset + len(char[0]) > 40:
			print('string too long')
			return
		for i,j in product(range(6),range(len(char[0]))):
			screen[i][offset + j] = char[i][j]
		offset += len(char[0]) + 1
	for row in screen:
		print(''.join(row))
	print()
	return screen

def can_noop_func(G,cycle,X,M,maxcycle):
	return all(G[c // M][c % M] == '#' if abs(c % M - X) <= 1 \
	else G[c // M][c % M] == '.' for c in range(cycle,min(cycle+3,maxcycle)))

def can_move_func(G,cycle,X,M,maxcycle):
	return all(G[c // M][c % M] == '#' if abs(c % M - X) <= 1 \
	else G[c // M][c % M] == '.' for c in range(cycle+2,min(cycle+4,maxcycle)))

def possible_mvts_func(G,cycle,X,M,maxcycle):
	return [Y-X for Y in range(1,M-1) if Y != X and can_move_func(G,cycle,Y,M,maxcycle)]

def mvts_func(G):
	N = len(G)
	M = len(G[0])
	
	mvts = []
	X = 1
	cycle = 0
	maxcycle = N * M
	while cycle < maxcycle - 1:
		can_noop = can_noop_func(G,cycle,X,M,maxcycle)
		possible_mvts = possible_mvts_func(G,cycle,X,M,maxcycle)
		if can_noop and possible_mvts:
			if randrange(4):
				mvts.append(0)
				cycle += 1
			else:
				mvt = choice(possible_mvts)
				mvts.append(mvt)
				X += mvt
				cycle += 2
		elif can_noop:
			mvts.append(0)
			cycle += 1
		elif possible_mvts:
			mvt = choice(possible_mvts)
			mvts.append(mvt)
			X += mvt
			cycle += 2
		else:
			return
	if cycle == maxcycle - 1:
		mvts.append(0)
	return mvts

def main(message, outpath):
	G = grid(message)
	if G is None:
		return
	elif G[0][:2] != ['#','#']:
		print('invalid string; must start with B, D, E, F, I, J, P, R, T or Z')
		return
	
	mvts = mvts_func(G)
	Nattempt = 1
	while not mvts:
		mvts = mvts_func(G)
		Nattempt += 1
	with open(outpath,'w') as outfile:
		outfile.write('\n'.join(f'addx {mvt}' if mvt else 'noop' for mvt in mvts))
	print(f'succeeded in {Nattempt} attempt{"s" if Nattempt > 1 else ""}')
	print('written to', outpath)

message = input('message to encode (default = TEST MSG): ').upper()
if not message:
	message = 'TEST MSG'
outpath = input('path to write to (default = out.txt): ')
if not outpath:
	outpath = 'out.txt'
print()

main(message, outpath)