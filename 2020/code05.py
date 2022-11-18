infile = open("input/in05_real.txt","r")
# infile = open("input/in05_test.txt","r")
L = [''.join(['1' if c=='B' or c=='R' else '0' for c in line.strip()]) for line in infile]

def seatID(row,col):
	return int(row,2)*8 + int(col,2)

def day05_part1(L):
	return max([seatID(P[:7],P[-3:]) for P in L])
	
def day05_part2(L):
	taken_seats = sorted([seatID(P[:7],P[-3:]) for P in L])
	for i,j in zip(taken_seats,taken_seats[1:]):
		if j-i == 2:
			return i+1

print(day05_part1(L))
print(day05_part2(L))