import re

infile = open("input/in18_real.txt","r")
# infile = open("input/in18_test3.txt","r")
tosum = [line.strip() for line in infile]

def find_nested(N):
	layer = 0
	p = 0
	for c in N:
		if c == '[':
			layer += 1
		elif c == ']':
			layer -= 1
		if layer == 5:
			return p
		p += 1

def snail_reduce(N):
	while True:
		X1 = find_nested(N)
		mB = re.search(r'\d{2,}',N)
		if X1 is not None:
			mX = re.match(r'\[([^,]*),([^]]*)]',N[X1:])
			X2 = X1 + mX.end()
			
			Lstr = N[:X1]
			Rstr = N[X2:]
			
			mL = re.search(r'\d+',N[X1-1::-1])
			if mL:
				L1 = X1-mL.end()
				L2 = X1-mL.start()
				nL = int(mL.group(0)[::-1]) + int(mX.group(1))
				Lstr = N[:L1] + str(nL) + N[L2:X1]
			
			mR = re.search(r'\d+',N[X2:])
			if mR:
				R1 = X2+mR.start()
				R2 = X2+mR.end()
				nR = int(mR.group(0)) + int(mX.group(2))
				Rstr = N[X2:R1] + str(nR) + N[R2:]
			
			N = Lstr + '0' + Rstr
		elif mB:
			B1 = mB.start()
			B2 = mB.end()
			nB = int(mB.group(0))
			
			N = N[:B1] + str([nB//2,nB-nB//2]) + N[B2:]
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
		ans = snail_reduce('['+ans+','+summand+']')
	return mag(eval(ans))

def day18_part2(tosum):
	maxmag = 0
	for N1 in tosum:
		for N2 in tosum:
			if N1 is not N2:
				maxmag = max(maxmag,day18_part1([N1,N2]))
	return maxmag

print(day18_part1(tosum))
print(day18_part2(tosum))