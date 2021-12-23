import heapq

infile = open("input/in23_real.txt","r")
# infile = open("input/in23_test.txt","r")

next(infile)
next(infile)

species = {'A': 2, 'B': 4, 'C': 6, 'D': 8} #associate each species with the column number they want to end up in

rows = [next(infile).strip()[3:-3].split('#'), next(infile).strip()[1:-1].split('#')]
rooms = [[species[t],species[b]] for t,b in zip(*rows)]

def dijk(ps,nR):
	visited = set()
	hallway_destinations = [0,1,3,5,7,9,10] #everywhere except doorways
	costs = {2: 1, 4: 10, 6: 100, 8: 1000}
	Q = []
	heapq.heappush(Q,(0,sorted(ps))) #sorted positions because needs to be an unambiguously labelled node
	while True:
		dist,ps = heapq.heappop(Q)
		if tuple(ps) not in visited: #usually list because mutable, here tuple because hashable
			if ps == [(i,j,i) for i in range(2,9,2) for j in range(1,nR+1)]: #final state
				return dist
			visited.add(tuple(ps))
			occ = [[None] * 11 for i in range(nR+1)]
			for s,r,c in ps:
				occ[r][c] = s #building up a map of occupancy because it's easier to work with than ps directly
			for i in range(4*nR):
				s,r,c = ps.pop(0) #species, row, col
				#move if you're in a room, there are only empty spaces above you, you or someone below you is in the wrong room, and your current room isn't surrounded
				if r > 0 \
				and not any([occ[R][c] for R in range(1,r)]) \
				and any([occ[R][c] != c for R in range(r,nR+1)]) \
				and (occ[0][c-1] is None or occ[0][c+1] is None):
					for C in hallway_destinations:
						c1 = min(c,C)
						c2 = max(c,C)
						if not any(occ[0][c1:c2+1]):
							heapq.heappush(Q,
								(dist + (r+c2-c1)*costs[s],
								sorted(ps + [(s,0,C)])))
				#move if you're in the hallway, there are no strangers in your room and there's no-one in the way
				elif r == 0 \
				and all([occ[R][s] is None or occ[R][s] == s for R in range(1,nR+1)]) \
				and not any(occ[0][min(c,s)+1:max(c,s)]):
					R = [R for R in range(1,nR+1)
						if occ[R][s] is None][-1]
					heapq.heappush(Q,
						(dist + (R+abs(c-s))*costs[s],
						sorted(ps + [(s,R,s)])))
				ps.append((s,r,c))

def day23_part1(rooms):
	ps = [] #list of positions (species,row,column)
	nR = len(rooms[0]) #depth of each room
	for room,species in enumerate(rooms):
		for i in range(nR):
			ps.append((species[i],i+1,2*(room+1)))
	return dijk(ps,nR)

def day23_part2(rooms):
	rooms[0].insert(1,8)
	rooms[0].insert(1,8)
	rooms[1].insert(1,4)
	rooms[1].insert(1,6)
	rooms[2].insert(1,2)
	rooms[2].insert(1,4)
	rooms[3].insert(1,6)
	rooms[3].insert(1,2)
	return day23_part1(rooms)

print(day23_part1(rooms))
print(day23_part2(rooms))