from math import prod

# infile = open("in2_test.txt","r")
infile = open("in2_real.txt","r")
L = [line.split() for line in infile.readlines()]
L2 = [[p[0],int(p[1])] for p in L]

def day2_part1(L):
    pos = [0, 0]
    for inst in L:
        if inst[0] == 'forward':
            pos[0] += inst[1]
        elif inst[0] == 'down':
            pos[1] += inst[1]
        elif inst[0] == 'up':
            pos[1] -= inst[1]
        else:
            print('invalid instruction')
            return None
    return prod(pos)

def day2_part2(L):
    pos = [0, 0]
    aim = 0
    for inst in L:
        if inst[0] == 'forward':
            pos[0] += inst[1]
            pos[1] += inst[1] * aim
        elif inst[0] == 'down':
            aim += inst[1]
        elif inst[0] == 'up':
            aim -= inst[1]
        else:
            print('invalid instruction')
            return None
    return prod(pos)

print(day2_part1(L2))
print(day2_part2(L2))