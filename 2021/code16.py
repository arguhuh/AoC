import math

infile = open("input/in16_real.txt","r")
# infile = open("input/in16_test.txt","r")

def read_packets(s,version,Ntoread):
	p = 0
	packets = []
	while Ntoread > 0 and p < len(s):
		Ntoread -= 1
		version[0] += int(s[p:p+3],2)
		if s[p+3:p+6] == '100': #4 represent a literal value
			numstr = ''
			p += 6
			done = 0
			while not done:
				done = s[p] != '1'
				numstr += s[p+1:p+5]
				p += 5
		else:
			if s[p+6] == '1': #the next 11 bits are a number that represents the number of sub-packets
				Npack = int(s[p+7:p+18],2)
				p += 18
				p += read_packets(s[p:],version,Npack)
			else: #the next 15 bits are a number that represents the total length in bits of the sub-packets
				Lpack = int(s[p+7:p+22],2)
				p += 22
				p += read_packets(s[p:p+Lpack],version,float("inf"))
	return p
			

def day16_part1(hexstr):
	hextobin = {
		"0": "0000",
		"1": "0001",
		"2": "0010",
		"3": "0011",
		"4": "0100",
		"5": "0101",
		"6": "0110",
		"7": "0111",
		"8": "1000",
		"9": "1001",
		"A": "1010",
		"B": "1011",
		"C": "1100",
		"D": "1101",
		"E": "1110",
		"F": "1111"
		}
	binstr = ''.join([hextobin[c] for c in hexstr])
	version = [0]
	read_packets(binstr,version,1)
	return version[0]
	

def interpret_packets(s,Ntoread=float("inf")):
	p = 0
	packets = []
	while Ntoread > 0 and p < len(s):
		Ntoread -= 1
		ID = s[p+3:p+6]
		if ID == '100': #4 represent a literal value
			numstr = ''
			p += 6
			done = 0
			while not done:
				done = s[p] != '1'
				numstr += s[p+1:p+5]
				p += 5
			packets.append(int(numstr,2))
		else: #operator
			if s[p+6] == '1': #the next 11 bits are a number that represents the number of sub-packets
				Npack = int(s[p+7:p+18],2)
				p += 18
				dp,subpackets = interpret_packets(s[p:],Npack)
			else: #the next 15 bits are a number that represents the total length in bits of the sub-packets
				Lpack = int(s[p+7:p+22],2)
				p += 22
				dp,subpackets = interpret_packets(s[p:p+Lpack])
			p += dp
			match ID:
				case '000': #sum
					packets.append(sum(subpackets))
				case '001': #product
					packets.append(math.prod(subpackets))
				case '010': #minimum
					packets.append(min(subpackets))
				case '011': #maximum
					packets.append(max(subpackets))
				case '101': #first greater than second
					packets.append(int(subpackets[0] > subpackets[1]))
				case '110': #first less than second
					packets.append(int(subpackets[0] < subpackets[1]))
				case '111': #first equal to second
					packets.append(int(subpackets[0] == subpackets[1]))
	return (p,packets)
			

def day16_part2(hexstr):
	hextobin = {
		"0": "0000",
		"1": "0001",
		"2": "0010",
		"3": "0011",
		"4": "0100",
		"5": "0101",
		"6": "0110",
		"7": "0111",
		"8": "1000",
		"9": "1001",
		"A": "1010",
		"B": "1011",
		"C": "1100",
		"D": "1101",
		"E": "1110",
		"F": "1111"
		}
	binstr = ''.join([hextobin[c] for c in hexstr])
	return interpret_packets(binstr,1)[1][0]

for line in infile:
	print(day16_part1(line.strip()))
	print(day16_part2(line.strip()))