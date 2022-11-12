infile = open("input/in01_real.txt","r")
# infile = open("input/in01_test.txt","r")
L = [int(line) for line in infile]

def day01_part1(L,offset):
    N_inc = 0
    for p,q in zip(L,L[offset:]): #list of pairs of the form (reading, subsequent reading)
        if q > p: #reading increases
            N_inc += 1
    return N_inc

print(day01_part1(L,1))
print(day01_part1(L,3))