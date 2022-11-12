# infile = open("input/in01_test.txt","r")
infile = open("input/in01_real.txt","r")
L = [int(line) for line in infile]

def day01_part1_method1(L):
    L_inc = [1 for p,q in zip(L,L[1:]) if q > p] #which readings increase?
    # N_inc = len(L_inc) #how many?
    return len(L_inc)

def day01_part1_method2(L):
    N_inc = 0
    for p in zip(L,L[1:]): #list of pairs of the form (reading, subsequent reading)
        if p[1] > p[0]: #reading increases
            N_inc += 1
    return N_inc

def day01_part2_method1(L):
    L3 = [sum(p) for p in zip(L,L[1:],L[2:])] #which readings increase?
    return day01_part1_method1(L3)

def day01_part2_method2(L):
    N_inc = 0
    for p,q in zip(L,L[3:]): #list of pairs of the form (reading, subsequent reading)
        if q > p: #reading increases
            N_inc += 1
    return N_inc

print(day01_part1_method1(L))
print(day01_part2_method1(L))
print(day01_part2_method2(L))