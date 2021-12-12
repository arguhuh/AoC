infile = open("in1_test.txt","r")
# infile = open("in1_real.txt","r")
L = [int(line) for line in infile.readlines()]

def day1_part1_method1(L):
    L_inc = [p[1]>p[0] for p in zip(L,L[1:])] #which readings increase?
    N_inc = sum(L_inc) #how many?
    return N_inc

def day1_part1_method2(L):
    N_inc = 0
    for p in zip(L,L[1:]): #list of pairs of the form (reading, subsequent reading)
        if p[1] > p[0]: #reading increases
            N_inc += 1
    return N_inc

def day1_part2_method1(L):
    L3 = [sum(p) for p in zip(L,L[1:],L[2:])] #which readings increase?
    return day1_part1_method1(L3)

print(day1_part1_method1(L))
print(day1_part2_method1(L))