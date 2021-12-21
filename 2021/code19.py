infile = open("input/in19_real.txt","r")
# infile = open("input/in19_test.txt","r")
scanners = []
for line in infile:
	if line == '\n':
		#flush scanner
		scanners.append(scanner)
	elif line[:2] == '--':
		#get ready to read a scanner
		scanner = []
	else:
		#read in beacon
		scanner.append(tuple(int(i) for i in line.strip().split(',')))

#X,Y,Z = facing,left,up
#if a scanner is at x0,y0,z0, it shifts beacons by -x0,-y0,-z0
R_group = [ #real coords = (+X,-Y,-Z) -> (1,0,-1,1,-1,2)
	(1,0,1,1,1,2),
	(1,0,-1,1,-1,2),
	(1,0,-1,2,1,1),
	(1,0,1,2,-1,1),
	(-1,0,-1,1,1,2),
	(-1,0,1,1,-1,2),
	(-1,0,1,2,1,1),
	(-1,0,-1,2,-1,1),
	(1,1,1,2,1,0),
	(1,1,-1,2,-1,0),
	(1,1,-1,0,1,2),
	(1,1,1,0,-1,2),
	(-1,1,-1,2,1,0),
	(-1,1,1,2,-1,0),
	(-1,1,1,0,1,2),
	(-1,1,-1,0,-1,2),
	(1,2,-1,1,1,0),
	(1,2,1,1,-1,0),
	(1,2,1,0,1,1),
	(1,2,-1,0,-1,1),
	(-1,2,1,1,1,0),
	(-1,2,-1,1,-1,0),
	(-1,2,-1,0,1,1),
	(-1,2,1,0,-1,1) #real coords (-Z,+X,-Y) = (-1*X[2],1*X[0],-1*X[1])
	] #real coords are transformed according to orientation and then shifted

def find_12_in_common(scanner1,scanner2,R_group):
	for sx,ix,sy,iy,sz,iz in R_group:
		for x in scanner1: #little x real coords
			for X in scanner2: #big X transformed coords
				xshift = x[0] - sx*X[ix]
				yshift = x[1] - sy*X[iy]
				zshift = x[2] - sz*X[iz]
				Nmatch = 0
				for Y in scanner2:
					y = (sx*Y[ix] + xshift,
						 sy*Y[iy] + yshift,
						 sz*Y[iz] + zshift)
					Nmatch += y in scanner1
					if Nmatch == 12:
						scanner2[:] = [
							(sx*Z[ix] + xshift,
							 sy*Z[iy] + yshift,
							 sz*Z[iz] + zshift)
							for Z in scanner2]
						print((xshift, yshift, zshift))
						return (xshift, yshift, zshift)

def day19_part1(scanners,R_group):
	unresolved = [True] * len(scanners)
	unresolved[0] = False
	base_queue = [0]
	while sum(unresolved):
		i1 = base_queue.pop(0)
		print(i1)
		for i2,todo in enumerate(unresolved):
			if todo and find_12_in_common(scanners[i1],scanners[i2],R_group):
				print("success with "+str(i2)) 
				base_queue.append(i2)
				unresolved[i2] = False
	beacons = {beacon for scanner in scanners for beacon in scanner}
	return len(beacons)

def day19_part2(scanners,R_group):
	unresolved = [True] * len(scanners)
	unresolved[0] = False
	centres = [None] * len(scanners)
	centres[0] = (0,0,0)
	base_queue = [0]
	while sum(unresolved):
		i1 = base_queue.pop(0)
		print(i1)
		for i2,todo in enumerate(unresolved):
			if todo:
				centre = find_12_in_common(scanners[i1],scanners[i2],R_group)
				if centre is not None:
					print("success with "+str(i2)) 
					base_queue.append(i2)
					unresolved[i2] = False
					centres[i2] = centre
					print(str(sum(unresolved))+" remain")
	dist = 0
	for c1 in centres:
		for c2 in centres:
			dist = max(dist,sum([abs(x-y) for x,y in zip(c1,c2)]))
	return dist

# print(day19_part1(scanners,R_group))
print(day19_part2(scanners,R_group))