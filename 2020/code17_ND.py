import itertools

infile = open("input/in17_real.txt","r")
# infile = open("input/in17_test.txt","r")
L = [[3 if c == '#' else 0 for c in line] for line in map(str.strip,infile)]

def access(G,indices):
	if len(indices):
		i, *js = indices
		return access(G[i],js)
	else:
		return G

def assign(G,indices,value):
	if len(indices) > 1:
		i, *js = indices
		assign(G[i],js,value)
	else:
		G[indices[0]] = value

def dims(G):
	if isinstance(G,list):
		return [len(G)] + dims(G[0])
	else:
		return []

def build_from_dims(dG):
	if len(dG) > 1:
		i, *js = dG
		return [build_from_dims(js) for _ in range(i)]
	else:
		return [0 for _ in range(dG[0])]

def flatten(G):
	if isinstance(G[0],list):
		Gflat = []
		for g in G:
			Gflat += g
		return flatten(Gflat)
	else:
		return G

def day17_ND(L,Ncycles,D):
	dL = dims(L)
	dG = [n + 2*Ncycles for n in \
	itertools.chain(itertools.repeat(1,D-len(dL)),dL)]
	
	G = build_from_dims(dG)
	
	for i,j in itertools.product(*(range(dim) for dim in dL)):
		assign(G,list(itertools.repeat(Ncycles,D-2)) + [Ncycles+i,Ncycles+j],L[i][j])
	
	for _ in range(Ncycles):
		stepND(G)
	
	return flatten(G).count(3)

def stepND(G):
	dG = dims(G)
	for i0 in itertools.product(*(range(dim) for dim in dG)):
		match access(G,i0):
			case 3:
				if not 3 <= sum([access(G,i) > 1 for i in \
				itertools.product(*(range(j0-1,j0+2) for j0 in i0)) \
				if all([0 <= j < dim for j,dim in zip(i,dG)])]) <= 4:
					assign(G,i0,2)
			case 0:
				if sum([access(G,i) > 1 for i in \
				itertools.product(*(range(j0-1,j0+2) for j0 in i0)) \
				if all([0 <= j < dim for j,dim in zip(i,dG)])]) == 3:
					assign(G,i0,1)
	for i0 in itertools.product(*(range(dim) for dim in dG)):
		match access(G,i0):
			case 2:
				assign(G,i0,0)
			case 1:
				assign(G,i0,3)
	return G

print(day17_ND(L,6,3))
print(day17_ND(L,6,4))