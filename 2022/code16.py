import re, math, functools as ft, itertools as it, more_itertools as mi
from queue import PriorityQueue, Empty
import time
from pyperclip import copy as ctrl_C

Lboth = []
for filename in ["input/in16_test.txt", "input/in16_real.txt"]:
	with open(filename,"r") as infile:
		lines = [(line[1],int(line[4][5:-1]),[c[:2] for c in line[9:]]) for line in map(str.split,infile)]
		neighs = {valve: neigh for valve,_,neigh in lines}
		FR = {valve: fr for valve,fr,_ in lines if fr}
		L = neighs, FR
		Lboth.append(L)
Ltest, Lreal = Lboth

def most_pressure(dist, FR, closed, pos, t):
	if not t or not closed:
		return 0
	
	max_pressure = 0
	for dest in closed:
		dt = dist[pos][dest] + 1
		if t >= dt:
			dp = FR[dest]*(t - dt)
			pressure = dp + most_pressure(dist, FR, closed - {dest}, dest, t - dt)
			if pressure > max_pressure:
				max_pressure = pressure
	
	return max_pressure
		

def dijk(neighs, start, end):
	visited = set()
	dist = dict.fromkeys(neighs,float('inf'))
	dist[start] = 0
	Q = PriorityQueue()
	Q.put((0,start))
	while True:
		try:
			d, pos = Q.get_nowait()
		except Empty:
			return float('inf')
		if pos == end:
			return d
		visited.add(pos)
		newd = d + 1
		for dest in list(set(neighs[pos]) - visited):
			if newd < dist[dest]:
				dist[dest] = newd
				Q.put((newd,dest))

def day16_part1(neighs, FR, startat = 'AA'):
	dist = {}
	for start in neighs:
		if start == startat or start in FR:
			distfromvalve = {}
			for end in FR:
				distfromvalve[end] = dijk(neighs, start, end)
			dist[start] = distfromvalve
	closed = set(FR.keys())
	return most_pressure(dist, FR, closed, startat, 30)

def upperbound(dist, FR, closed, pos1, pos2, t1, t2):
	#go to closest, then assume everywhere 1 dist away
	t1 -= min(dist[pos1][valve] for valve in closed) - 1
	t2 -= min(dist[pos2][valve] for valve in closed) - 1
	FRs = sorted((fr for valve, fr in FR.items() if valve in closed), reverse = True)
	tb = max(t1,t2); ts = min(t1,t2); eq1 = False; sub1 = True; eq2 = False; sub2 = True
	return sum(fr * (tb := tb - (sub1 := sub1 ^ (eq1 := eq1 or tb < ts)) - (sub2 := sub2 ^ (eq2 := eq2 or tb < ts-1))) * (tb > 0) for i,fr in enumerate(FRs) if tb > 0)

def most_pressure2(dist, FR, closed, pos1, pos2, t1, t2, threshold = 0):
	if not t1 and not t2 or not closed \
	or upperbound(dist, FR, closed, pos1, pos2, t1, t2) <= threshold:
		return 0
	
	max_pressure = 0
	for dest1, dest2 in it.permutations(closed, 2):
		dt1 = dist[pos1][dest1] + 1
		dt2 = dist[pos2][dest2] + 1
		if t1 >= dt1 and t2 >= dt2:
			dp = FR[dest1]*(t1 - dt1) + FR[dest2]*(t2 - dt2)
			pressure = dp + most_pressure2(dist, FR, closed - {dest1,dest2}, dest1, dest2, t1 - dt1, t2 - dt2, max_pressure - dp)
			if pressure > max_pressure:
				max_pressure = pressure
	
	pressure = most_pressure(dist, FR, closed, pos1, t1)
	if pressure > max_pressure:
		max_pressure = pressure
		
	pressure = most_pressure(dist, FR, closed, pos2, t2)
	if pressure > max_pressure:
		max_pressure = pressure
	
	return max_pressure

def day16_part2(neighs, FR, startat = 'AA'):
	dist = {}
	for start in neighs:
		if start == startat or start in FR:
			distfromvalve = {}
			for end in FR:
				distfromvalve[end] = dijk(neighs, start, end)
			dist[start] = distfromvalve
	closed = set(FR.keys())
	return most_pressure2(dist, FR, closed, startat, startat, 26, 26)


result_test_1 = day16_part1(*Ltest)
result_real_1 = day16_part1(*Lreal)

print(result_real_1)
print(result_test_1)
try:
	ctrl_C(result_real_1)
except:
	print("cannot copy result")

result_test_2 = day16_part2(*Ltest)
result_real_2 = day16_part2(*Lreal)

if result_test_2 is not None:
	print()
	print(result_real_2)
	print(result_test_2)
	try:
		ctrl_C(result_real_2)
	except:
		print("cannot copy result")