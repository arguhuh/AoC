from copy import deepcopy

# infile = open("input/in18_real.txt","r")
infile = open("input/in18_test3.txt","r")
tosum = [eval(line.strip()) for line in infile]

def find_nested(N):
	for i1 in range(2): #N as a whole must be a len-2 list, so it must contain at the very least N[0] and N[1]
		if isinstance(N[i1],list): #if it's a list, then we can go deeper
			for i2 in range(2): #because we know N[i1] is a list, it must contain N[i1][0] and N[i1][1]
				if isinstance(N[i1][i2],list):
					for i3 in range(2):
						if isinstance(N[i1][i2][i3],list):
							for i4 in range(2):
								if isinstance(N[i1][i2][i3][i4],list):
									return (i1,i2,i3,i4)

def find_big(N):
	for i1 in range(2): #N as a whole must be a len-2 list, so it must contain at the very least N[0] and N[1]
		if isinstance(N[i1],list): #if it's a list, then we can go deeper
			for i2 in range(2): #because we know N[i1] is a list, it must contain N[i1][0] and N[i1][1]
				if isinstance(N[i1][i2],list):
					for i3 in range(2):
						if isinstance(N[i1][i2][i3],list):
							for i4 in range(2):
								if isinstance(N[i1][i2][i3][i4],list):
									for i5 in range(2):
										if N[i1][i2][i3][i4][i5] > 9:
											return (5,(i1,i2,i3,i4,i5))
								elif N[i1][i2][i3][i4] > 9:
									return (4,(i1,i2,i3,i4))
						elif N[i1][i2][i3] > 9:
							return (3,(i1,i2,i3))
				elif N[i1][i2] > 9:
					return (2,(i1,i2))
		elif N[i1] > 9:
			return (1,i1)

def snail_reduce(N):
	while True:
		first_nest = find_nested(N)
		first_big = find_big(N)
		if first_nest is not None:
			i1,i2,i3,i4 = first_nest
			p,q = N[i1][i2][i3][i4]
			N[i1][i2][i3][i4] = 0
			if i4 == 1: #list N[i1][i2][i3][1] is on the right and so the left exploding number p goes to the left N[i1][i2][i3][0], which must be a regular number; the right exploding number q goes elsewhere
				N[i1][i2][i3][0] += p
				if i3 == 0:
					if isinstance(N[i1][i2][1],list):
						if isinstance(N[i1][i2][1][0],list):
							N[i1][i2][1][0][0] += q
						else:
							N[i1][i2][1][0] += q
					else:
						N[i1][i2][1] += q
				elif i2 == 0:
					if isinstance(N[i1][1],list):
						if isinstance(N[i1][1][0],list):
							if isinstance(N[i1][1][0][0],list):
								N[i1][1][0][0][0] += q
							else:
								N[i1][1][0][0] += q
						else:
							N[i1][1][0] += q
					else:
						N[i1][1] += q
				elif i1 == 0:
					if isinstance(N[1],list):
						if isinstance(N[1][0],list):
							if isinstance(N[1][0][0],list):
								if isinstance(N[1][0][0][0],list):
									N[1][0][0][0][0] += q
								else:
									N[1][0][0][0] += q
							else:
								N[1][0][0] += q
						else:
							N[1][0] += q
					else:
						N[1] += q
			else: #list N[i1][i2][i3][0] is on the left and so the right exploding number q goes to the right N[i1][i2][i3][1], which can be a list; the left exploding number p goes elsewhere
				if isinstance(N[i1][i2][i3][1],list):
					N[i1][i2][i3][1][0] += q
				else:
					N[i1][i2][i3][1] += q
				
				if i3 == 1:
					if isinstance(N[i1][i2][0],list):
						if isinstance(N[i1][i2][0][1],list):
							N[i1][i2][0][1][1] += p
						else:
							N[i1][i2][0][1] += p
					else:
						N[i1][i2][0] += p
				elif i2 == 1:
					if isinstance(N[i1][0],list):
						if isinstance(N[i1][0][1],list):
							if isinstance(N[i1][0][1][1],list):
								N[i1][0][1][1][1] += p
							else:
								N[i1][0][1][1] += p
						else:
							N[i1][0][1] += p
					else:
						N[i1][0] += p
				elif i1 == 1:
					if isinstance(N[0],list):
						if isinstance(N[0][1],list):
							if isinstance(N[0][1][1],list):
								if isinstance(N[0][1][1][1],list):
									N[0][1][1][1][1] += p
								else:
									N[0][1][1][1] += p
							else:
								N[0][1][1] += p
						else:
							N[0][1] += p
					else:
						N[0] += p
		elif first_big is not None:
			depth,indices = first_big
			match depth:
				case 1:
					i1 = indices
					N[i1] = [N[i1]//2,N[i1]-N[i1]//2]
				case 2:
					i1,i2 = indices
					N[i1][i2] = [N[i1][i2]//2,N[i1][i2]-N[i1][i2]//2]
				case 3:
					i1,i2,i3 = indices
					N[i1][i2][i3] = [N[i1][i2][i3]//2,N[i1][i2][i3]-N[i1][i2][i3]//2]
				case 4:
					i1,i2,i3,i4 = indices
					N[i1][i2][i3][i4] = [N[i1][i2][i3][i4]//2,N[i1][i2][i3][i4]-N[i1][i2][i3][i4]//2]
				case 5:
					i1,i2,i3,i4,i5 = indices
					N[i1][i2][i3][i4][i5] = [N[i1][i2][i3][i4][i5]//2,N[i1][i2][i3][i4][i5]-N[i1][i2][i3][i4][i5]//2]
		else:
			return N

def mag(N):
	if isinstance(N,list):
		return 3*mag(N[0]) + 2*mag(N[1])
	else:
		return N

def day18_part1(tosum):
	ans = tosum[0]
	for summand in tosum[1:]:
		ans = snail_reduce([deepcopy(ans),deepcopy(summand)])
	return mag(ans)

def day18_part2(tosum):
	maxmag = 0
	for N1 in tosum:
		for N2 in tosum:
			if N1 is not N2:
				maxmag = max(maxmag,day18_part1([N1,N2]))
	return maxmag

print(day18_part1(tosum))
print(day18_part2(tosum))