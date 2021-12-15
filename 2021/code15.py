import heapq,queue

infile = open("input/in15_real.txt","r")
# infile = open("input/in15_test.txt","r")
grid = [[int(i) for i in line.strip()] for line in infile]

def dijk_fun(grid,pos,Ni,Nj):
	unvisited = {(i,j) for i in range(Ni) for j in range(Nj)}
	dist = [[float("inf")] * Nj for i in range(Ni)]
	dist[pos[0]][pos[1]] = 0
	Q = []
	heapq.heappush(Q,(0,pos))
	while len(unvisited) > 0:
		d,(p,q) = heapq.heappop(Q)
		if (p,q) == (Ni-1,Nj-1):
			return d
		unvisited.remove((p,q))
		neighs = []
		if p > 0 and (p-1,q) in unvisited:
			neighs.append((p-1,q))
		if p < Ni-1 and (p+1,q) in unvisited:
			neighs.append((p+1,q))
		if q > 0 and (p,q-1) in unvisited:
			neighs.append((p,q-1))
		if q < Nj-1 and (p,q+1) in unvisited:
			neighs.append((p,q+1))
		for r,s in neighs:
			newd = d + grid[r][s]
			if newd < dist[r][s]:
				dist[r][s] = newd
				heapq.heappush(Q,(newd,(r,s)))

def dijk_obj(grid,pos,Ni,Nj):
	unvisited = {(i,j) for i in range(Ni) for j in range(Nj)}
	dist = [[float("inf")] * Nj for i in range(Ni)]
	dist[pos[0]][pos[1]] = 0
	Q = queue.PriorityQueue()
	Q.put((0,pos))
	while len(unvisited) > 0:
		d,(p,q) = Q.get()
		if (p,q) == (Ni-1,Nj-1):
			return d
		unvisited.remove((p,q))
		neighs = []
		if p > 0 and (p-1,q) in unvisited:
			neighs.append((p-1,q))
		if p < Ni-1 and (p+1,q) in unvisited:
			neighs.append((p+1,q))
		if q > 0 and (p,q-1) in unvisited:
			neighs.append((p,q-1))
		if q < Nj-1 and (p,q+1) in unvisited:
			neighs.append((p,q+1))
		for r,s in neighs:
			newd = d + grid[r][s]
			if newd < dist[r][s]:
				dist[r][s] = newd
				Q.put((newd,(r,s)))

def repgrid(grid,Ri,Rj):
	return [[(i+ri+rj-1)%9+1 for ri in range(Ri) for i in row] for rj in range(Rj) for row in grid]

def day15_part1(grid):
	Ni = len(grid)
	Nj = len(grid[0])
	pos = (0,0)
	return dijk_fun(grid,pos,Ni,Nj)
	# return dijk_obj(grid,pos,Ni,Nj)

def day15_part2(grid):
	Ni = 5*len(grid)
	Nj = 5*len(grid[0])
	pos = (0,0)
	return dijk_fun(repgrid(grid,5,5),pos,Ni,Nj)
	# return dijk_obj(repgrid(grid,5,5),pos,Ni,Nj)

print(day15_part1(grid))
print(day15_part2(grid))