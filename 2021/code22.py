infile = open("input/in22_real.txt","r")
# infile = open("input/in22_test2.txt","r")
instructions = [(dir,int(x1),int(x2),int(y1),int(y2),int(z1),int(z2)) for dir,[x1,x2],[y1,y2],[z1,z2] in [(dir,x[2:].split('..'),y[2:].split('..'),z[2:].split('..')) for dir,[x,y,z] in [(1,pos.split(',')) if dir=='on' else (0,pos.split(',')) for dir,pos in [line.split() for line in infile]]]]

def execute_instruction(instructions,tally,limits):
	X1,X2,Y1,Y2,Z1,Z2 = limits
	if X1 > X2 or Y1 > Y2 or Z1 > Z2:
		return
	while len(instructions) > 0 and tally[2] > 0:
		dir,x1,x2,y1,y2,z1,z2 = instructions.pop()
		x1 = max(x1,X1)
		y1 = max(y1,Y1)
		z1 = max(z1,Z1)
		x2 = min(x2,X2)
		y2 = min(y2,Y2)
		z2 = min(z2,Z2)
		# print("resolving cuboid " + str((x1,x2,y1,y2,z1,z2)))
		if x1 <= x2 and y1 <= y2 and z1 <= z2:
			Nsettled = (x2-x1+1) * (y2-y1+1) * (z2-z1+1)
			# print("resolving " + str(Nsettled) + " points")
			tally[2] -= Nsettled
			tally[dir] += Nsettled
			#now it's divided into remaining subregions
			#X1:X2, Y1:Y2, Z1:z1-1 = 9
			# print("entering subcuboid " + str((X1,X2,Y1,Y2,Z1,z1-1)))
			execute_instruction(instructions[:],tally,
				(X1,X2,Y1,Y2,Z1,z1-1))
			#X1:X2, Y1:Y2, z2+1:Z2 = 9
			# print("entering subcuboid " + str((X1,X2,Y1,Y2,z2+1,Z2)))
			execute_instruction(instructions[:],tally,
				(X1,X2,Y1,Y2,z2+1,Z2))
			#X1:X2, Y1:y1-1, z1:z2 = 3
			# print("entering subcuboid " + str((X1,X2,Y1,y1-1,z1,z2)))
			execute_instruction(instructions[:],tally,
				(X1,X2,Y1,y1-1,z1,z2))
			#X1:X2, y2+1:Y2, z1:z2 = 3
			# print("entering subcuboid " + str((X1,X2,y2+1,Y2,z1,z2)))
			execute_instruction(instructions[:],tally,
				(X1,X2,y2+1,Y2,z1,z2))
			#X1:x1-1, y1:y2, z1:z2 = 1
			# print("entering subcuboid " + str((X1,x1-1,y1,y2,z1,z2)))
			execute_instruction(instructions[:],tally,
				(X1,x1-1,y1,y2,z1,z2))
			#x2+1:X2, y1:y2, z1:z2 = 1
			# print("entering subcuboid " + str((x2+1,X2,y1,y2,z1,z2)))
			execute_instruction(instructions[:],tally,
				(x2+1,X2,y1,y2,z1,z2))
			return

def day22_part1(instructions):
	tally = [0,0,101**3] #definitely off, definitely on, unsure
	execute_instruction(instructions[:],tally,(-50,50,-50,50,-50,50))
	return tally[1]

def day22_part2(instructions):
	X1 = float("inf")
	Y1 = float("inf")
	Z1 = float("inf")
	X2 = float("-inf")
	Y2 = float("-inf")
	Z2 = float("-inf")
	for dir,x1,x2,y1,y2,z1,z2 in instructions:
		X1 = min(x1,X1)
		Y1 = min(y1,Y1)
		Z1 = min(z1,Z1)
		X2 = max(x2,X2)
		Y2 = max(y2,Y2)
		Z2 = max(z2,Z2)
	tally = [0,0,(X2-X1+1) * (Y2-Y1+1) * (Z2-Z1+1)] #definitely off, definitely on, unsure
	execute_instruction(instructions[:],tally,(X1,X2,Y1,Y2,Z1,Z2))
	return tally[1]

# print(day22_part1(instructions))
print(day22_part2(instructions))