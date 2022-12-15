from re import sub
from itertools import product
from pyperclip import copy as ctrl_C

Lboth = []
for filename in ["input/in15_test.txt", "input/in15_real.txt"]:
	with open(filename,"r") as infile:
		L = [list(map(int,sub('[^-0-9]+','@',line).strip('@').split('@'))) for line in map(str.strip,infile)]
		Lboth.append(L)
Ltest, Lreal = Lboth

def day15_part1(L, ycheck = 2_000_000):
	covered = set() #set of positions that are in a sensor region (inc. beacons)
	beacons = set()
	for xS,yS,xB,yB in L:
		dist = abs(xS-xB) + abs(yS-yB)
		if ycheck in range(yS - dist, yS + dist + 1):
			covered |= set(range(xS-dist+abs(yS-ycheck),xS+dist-abs(yS-ycheck)+1))
			if yB == ycheck:
				beacons.add(xB)
	return len(covered) - len(beacons)

def day15_part2(L, maxcoord = 4_000_000):
	candidates = set()
	for (xS,yS,xB,yB),(Xs,Ys,Xb,Yb) in product(L,L):
		#the only places that a single free space can be are:
		#	next to the intersection of two edges (see left diagram, where x and + delinate the edges of two sensor regions, O is an intersection and C is a candidate single space)
		#	or between two adjacent edges (see right diagram, where C are the outside candidates and N are inside candidates [not considered here])
		
		#                                 +
		#       x     +                  + +
		#      x x   + +                +   +
		#     x   xC+   +              +     +
		#    x     O     +             C+   +
		#   x     + x     +            xN+ +
		#  x     +   x     +          x xN+
		# x       +   x   +          x   xC
		#  x       + x   +          x     x
		#   x       O   +          x       x
		#    x     xC+ +            x     x
		#     x   x   +              x   x
		#      x x                    x x
		#       x                      x
		
		d = abs(xS-xB) + abs(yS-yB)
		D = abs(Xs-Xb) + abs(Ys-Yb)
		
		x2 = (Ys+Xs+D) - (yS-xS+d)
		x = x2 // 2 # intersection point
		if x2 % 2 == 0 and x in range(xS-d-1, xS): #NW of 1st intersects NE of 2nd
			y = yS-xS+d + x
			candidates.add((x, y + 1)) #candidate is N of intersection
		
		x2 = (Ys+Xs-D) - (yS-xS+d)
		x = x2 // 2 # intersection point
		if x2 % 2 == 0 and x in range(xS-d+1, xS+2): #NW of 1st intersects SW of 2nd
			y = yS-xS+d + x
			candidates.add((x - 1, y)) #candidate is W of intersection
		
		x2 = (Ys+Xs+D) - (yS-xS-d)
		x = x2 // 2 # intersection point
		if x2 % 2 == 0 and x in range(xS-1, xS+d): #SE of 1st intersects NE of 2nd
			y = yS-xS-d + x
			candidates.add((x + 1, y)) #candidate is E of intersection
		
		x2 = (Ys+Xs-D) - (yS-xS-d)
		x = x2 // 2 # intersection point
		if x2 % 2 == 0 and x in range(xS+1, xS+d+2): #SE of 1st intersects SW of 2nd
			y = yS-xS-d + x
			candidates.add((x, y - 1)) #candidate is S of intersection
	
	for x,y in candidates:
		if x in range(maxcoord + 1) and y in range(maxcoord + 1) and \
		all(abs(x-xS)+abs(y-yS) > abs(xS-xB) + abs(yS-yB) for xS,yS,xB,yB in L):
			return x * 4_000_000 + y


result_test_1 = day15_part1(Ltest, ycheck = 10)
result_real_1 = day15_part1(Lreal)

print(result_real_1)
print(result_test_1)
try:
	ctrl_C(result_real_1)
except:
	print("cannot copy result")

result_test_2 = day15_part2(Ltest, maxcoord = 20)
result_real_2 = day15_part2(Lreal)

if result_test_2 is not None:
	print()
	print(result_real_2)
	print(result_test_2)
	try:
		ctrl_C(result_real_2)
	except:
		print("cannot copy result")