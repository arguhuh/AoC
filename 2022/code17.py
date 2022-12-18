from itertools import count
from pyperclip import copy as ctrl_C

Lboth = []
for filename in ["input/in17_test.txt", "input/in17_real.txt"]:
	with open(filename,"r") as infile:
		L = [1 if c == '>' else 0 for c in infile.read()]
		Lboth.append(L)
Ltest, Lreal = Lboth

def is_obstacle(G, y, x, ny = 1, nx = 1):
	return any(G[Y][X] for Y in range(y, min(y+ny, len(G))) for X in range(x, x+nx))

def day17_part1(L, rock_limit = 2022):
	G = [[1 for _ in range(7)]]
	ymax = 0
	i_instr = 0
	N_instr = len(L)
	width = 4
	for i_rock in range(rock_limit):
		y = ymax + 5 #starting with vert so add another unit
		x = 2
		match i_rock % 5:
			case 0:
				# @@@@
				while not is_obstacle(G, y-1, x, nx = width):
					y -= 1
					if L[i_instr % N_instr]: #>
						if x + width < 7 and not is_obstacle(G, y, x+width):
							x += 1
					else: #<
						if x and not is_obstacle(G, y, x-1):
							x -= 1
					i_instr += 1
				
				ytop = y
				if ytop > ymax:
					G.extend([[0 for _ in range(7)] for _ in range(ytop - ymax)])
					ymax = ytop
				G[y][x:x+width] = [1,1,1,1]
				
				width = 3
			case 1:
				# .@.
				# @@@
				# .@.
				while not (\
				is_obstacle(G, y-1, x+1) or \
				is_obstacle(G, y, x) or \
				is_obstacle(G, y, x+2)):
					y -= 1
					if L[i_instr % N_instr]: #>
						if x + width < 7 and not (\
						is_obstacle(G, y, x+2) or \
						is_obstacle(G, y+1, x+3) or \
						is_obstacle(G, y+2, x+2)):
							x += 1
					else: #<
						if x and not (\
						is_obstacle(G, y, x) or \
						is_obstacle(G, y+1, x-1) or \
						is_obstacle(G, y+2, x)):
							x -= 1
					i_instr += 1
				
				ytop = y + 2
				if ytop > ymax:
					G.extend([[0 for _ in range(7)] for _ in range(ytop - ymax)])
					ymax = ytop
				G[y][x+1] = 1
				G[y+1][x:x+width] = [1,1,1]
				G[y+2][x+1] = 1
				
				width = 3
			case 2:
				# ..@
				# ..@
				# @@@
				while not is_obstacle(G, y-1, x, nx = width):
					y -= 1
					if L[i_instr % N_instr]: #>
						if x + width < 7 and not is_obstacle(G, y, x+width, ny = 3):
							x += 1
					else: #<
						if x and not (\
						is_obstacle(G, y, x-1) or \
						is_obstacle(G, y+1, x+1) or \
						is_obstacle(G, y+2, x+1)):
							x -= 1
					i_instr += 1
				
				ytop = y + 2
				if ytop > ymax:
					G.extend([[0 for _ in range(7)] for _ in range(ytop - ymax)])
					ymax = ytop
				G[y][x:x+width] = [1,1,1]
				G[y+1][x+2] = 1
				G[y+2][x+2] = 1
				
				width = 1
			case 3:
				# @
				# @
				# @
				# @
				while not is_obstacle(G, y-1, x):
					y -= 1
					if L[i_instr % N_instr]: #>
						if x + width < 7 and not is_obstacle(G, y, x+1, ny = 4):
							x += 1
					else: #<
						if x and not is_obstacle(G, y, x-1, ny = 4):
							x -= 1
					i_instr += 1
				
				ytop = y + 3
				if ytop > ymax:
					G.extend([[0 for _ in range(7)] for _ in range(ytop - ymax)])
					ymax = ytop
				G[y][x] = 1
				G[y+1][x] = 1
				G[y+2][x] = 1
				G[y+3][x] = 1
				
				width = 2
			case 4:
				# @@
				# @@
				while not is_obstacle(G, y-1, x, nx = width):
					y -= 1
					if L[i_instr % N_instr]: #>
						if x + width < 7 and not is_obstacle(G, y, x+width, ny = 2):
							x += 1
					else: #<
						if x and not is_obstacle(G, y, x-1, ny = 2):
							x -= 1
					i_instr += 1
				
				ytop = y + 1
				if ytop > ymax:
					G.extend([[0 for _ in range(7)] for _ in range(ytop - ymax)])
					ymax = ytop
				G[y][x:x+width] = [1,1]
				G[y+1][x:x+width] = [1,1]
				
				width = 4
	return ymax

def find_cycle(L):
	G = [[1 for _ in range(7)]]
	ymax = 0
	i_instr = 0
	N_instr = len(L)
	width = 4
	
	cache = []
	ymaxes = []
	for i_rock in count():
		state = (i_rock % 5, i_instr % N_instr)
		if cache.count(state) > 1:
			i_state = [i for i,elm in enumerate(cache) if elm == state]
			if cache[i_state[-2]:i_state[-1]] == cache[i_state[-1]:]:
				return i_state[-2], ymaxes[i_state[-2]], \
				[elm - ymaxes[i_state[-1]] for elm in ymaxes[i_state[-1]:]], \
				ymaxes[i_state[-1]] - ymaxes[i_state[-2]]
		cache.append(state)
		ymaxes.append(ymax)
		
		y = ymax + 5
		x = 2
		match i_rock % 5:
			case 0:
				# @@@@
				while not is_obstacle(G, y-1, x, nx = width):
					y -= 1
					if L[i_instr % N_instr]: #>
						if x + width < 7 and not is_obstacle(G, y, x+width):
							x += 1
					else: #<
						if x and not is_obstacle(G, y, x-1):
							x -= 1
					i_instr += 1
				
				ytop = y
				if ytop > ymax:
					G.extend([[0 for _ in range(7)] for _ in range(ytop - ymax)])
					ymax = ytop
				G[y][x:x+width] = [1,1,1,1]
				
				width = 3
			case 1:
				# .@.
				# @@@
				# .@.
				while not (\
				is_obstacle(G, y-1, x+1) or \
				is_obstacle(G, y, x) or \
				is_obstacle(G, y, x+2)):
					y -= 1
					if L[i_instr % N_instr]: #>
						if x + width < 7 and not (\
						is_obstacle(G, y, x+2) or \
						is_obstacle(G, y+1, x+3) or \
						is_obstacle(G, y+2, x+2)):
							x += 1
					else: #<
						if x and not (\
						is_obstacle(G, y, x) or \
						is_obstacle(G, y+1, x-1) or \
						is_obstacle(G, y+2, x)):
							x -= 1
					i_instr += 1
				
				ytop = y + 2
				if ytop > ymax:
					G.extend([[0 for _ in range(7)] for _ in range(ytop - ymax)])
					ymax = ytop
				G[y][x+1] = 1
				G[y+1][x:x+width] = [1,1,1]
				G[y+2][x+1] = 1
				
				width = 3
			case 2:
				# ..@
				# ..@
				# @@@
				while not is_obstacle(G, y-1, x, nx = width):
					y -= 1
					if L[i_instr % N_instr]: #>
						if x + width < 7 and not is_obstacle(G, y, x+width, ny = 3):
							x += 1
					else: #<
						if x and not (\
						is_obstacle(G, y, x-1) or \
						is_obstacle(G, y+1, x+1) or \
						is_obstacle(G, y+2, x+1)):
							x -= 1
					i_instr += 1
				
				ytop = y + 2
				if ytop > ymax:
					G.extend([[0 for _ in range(7)] for _ in range(ytop - ymax)])
					ymax = ytop
				G[y][x:x+width] = [1,1,1]
				G[y+1][x+2] = 1
				G[y+2][x+2] = 1
				
				width = 1
			case 3:
				# @
				# @
				# @
				# @
				while not is_obstacle(G, y-1, x):
					y -= 1
					if L[i_instr % N_instr]: #>
						if x + width < 7 and not is_obstacle(G, y, x+1, ny = 4):
							x += 1
					else: #<
						if x and not is_obstacle(G, y, x-1, ny = 4):
							x -= 1
					i_instr += 1
				
				ytop = y + 3
				if ytop > ymax:
					G.extend([[0 for _ in range(7)] for _ in range(ytop - ymax)])
					ymax = ytop
				G[y][x] = 1
				G[y+1][x] = 1
				G[y+2][x] = 1
				G[y+3][x] = 1
				
				width = 2
			case 4:
				# @@
				# @@
				while not is_obstacle(G, y-1, x, nx = width):
					y -= 1
					if L[i_instr % N_instr]: #>
						if x + width < 7 and not is_obstacle(G, y, x+width, ny = 2):
							x += 1
					else: #<
						if x and not is_obstacle(G, y, x-1, ny = 2):
							x -= 1
					i_instr += 1
				
				ytop = y + 1
				if ytop > ymax:
					G.extend([[0 for _ in range(7)] for _ in range(ytop - ymax)])
					ymax = ytop
				G[y][x:x+width] = [1,1]
				G[y+1][x:x+width] = [1,1]
				
				width = 4

def day17_part2(L, rock_limit = 1_000_000_000_000):
	N0, h0, cycle, h = find_cycle(L)
	N, i = divmod(rock_limit - N0, len(cycle))
	return h0 + N * h + cycle[i]


result_test_1 = day17_part1(Ltest)
result_real_1 = day17_part1(Lreal)

print(result_real_1)
print(result_test_1)
try:
	ctrl_C(result_real_1)
except:
	print("cannot copy result")

result_test_2 = day17_part2(Ltest)
result_real_2 = day17_part2(Lreal)

if result_test_2 is not None:
	print()
	print(result_real_2)
	print(result_test_2)
	try:
		ctrl_C(result_real_2)
	except:
		print("cannot copy result")