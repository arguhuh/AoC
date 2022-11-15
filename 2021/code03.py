infile = open("input/in03_real.txt","r")
# infile = open("input/in03_test.txt","r")
L = [[int(c) for c in line.strip()] for line in infile]

def day03_part1(L):
    L_gamma = ['1' if sum(t) > len(L)//2 else '0' for t in zip(*L)]
    gamma = int(''.join(L_gamma),2)
    epsilon = 2**len(L_gamma) - 1 - gamma
    return gamma*epsilon

def O_iter(L,b):
    if len(L) == 1:
        return L[0]
    
    if sum([n[b] for n in L]) < len(L)/2:
        MC = 0
    else:
        MC = 1
    
    L = [n for n in L if n[b] == MC]
    return O_iter(L,b+1)

def C_iter(L,b):
    if len(L) == 1:
        return L[0]
    
    if sum([n[b] for n in L]) < len(L)/2:
        MC = 1
    else:
        MC = 0
    
    L = [n for n in L if n[b] == MC]
    return C_iter(L,b+1)

def day03_part2(L):
    OG = int(''.join([str(c) for c in O_iter(L,0)]),2)
    CS = int(''.join([str(c) for c in C_iter(L,0)]),2)
    return OG * CS

print(day03_part1(L))
print(day03_part2(L))
