import math

def day17_part2(x1,x2,y1,y2):
	n1 = math.ceil(-1/2 + math.sqrt(1/4 + 2*x1))
	n2 = math.ceil(x2/2)
	Nshot = 0
	for n in range(n1,n2+1):
		if round(n*(n+1)/2) <= x2:
			b = float("inf")
			m2 = -y1-1
		else:
			b = math.floor((2*n+1)/2 - math.sqrt(((2*n+1)/2)**2 - 2*x2))
			m2 = math.floor(y2/b + (b-1)/2)
		a = math.ceil((2*n+1)/2 - math.sqrt(((2*n+1)/2)**2 - 2*x1))
		m1 = math.ceil(y1/a + (a-1)/2)
		if b >= a:
			Nshot += m2-m1+1
		print(str(n)+": ["+str(a)+","+str(b)+"]; "+str(m1)+":"+str(m2)+", total: "+str(Nshot))
	print("plus "+str(x2-x1+1)+" * "+str(y2-y1+1))
	return Nshot + (x2-x1+1)*(y2-y1+1)

def sim(x1,x2,y1,y2,u0,v0):
	x = 0
	y = 0
	u = u0
	v = v0
	while x <= x2 and y >= y1:
		if x >= x1 and y <= y2:
			print((u0,v0))
			return 1
		x += u
		y += v
		if u > 0:
			u -= 1
		v -= 1
	return 0

def day17_brute(x1,x2,y1,y2):
	Nshot = 0
	for u0 in range(0,x2+1):
		for v0 in range(y1,-y1):
			Nshot += sim(x1,x2,y1,y2,u0,v0)
	return Nshot

# print(day17_part2(20,30,-10,-5))
print(day17_part2(281,311,-74,-54))

# print(day17_brute(20,30,-10,-5))
# print(day17_brute(281,311,-74,-54))