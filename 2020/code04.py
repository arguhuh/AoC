import re

infile = open("input/in04_real.txt","r")
# infile = open("input/in04_test.txt","r")

passports = []
passport = []
for line in infile:
	if line == '\n':
		passports.append(passport)
		passport = []
	else:
		passport += line.split()
passports.append(passport)

def day04_part1(passports):
	Nvalid = 0
	fields = ['byr','iyr','eyr','hgt','hcl','ecl','pid']
	for passport in passports:
		hasfields = [False] * len(fields)
		for field in passport:
			for i in range(len(fields)):
				if field[:3] == fields[i]:
					hasfields[i] = True
					break
		if all(hasfields):
			Nvalid += 1
	return Nvalid

def day04_part2(passports):
	Nvalid = 0
	for passport in passports:
		hasfields = [False] * 7
		for field in passport:
			key = field[:3]
			value = field[4:]
			match key:
				case 'byr':
					if re.match('^[0-9]{4}$',value) and 1920 <= int(value) <= 2002:
						hasfields[0] = True
				case 'iyr':
					if re.match('^[0-9]{4}$',value) and 2010 <= int(value) <= 2020:
						hasfields[1] = True
				case 'eyr':
					if re.match('^[0-9]{4}$',value) and 2020 <= int(value) <= 2030:
						hasfields[2] = True
				case 'hgt':
					num = value[:-2]
					units = value[-2:]
					match units:
						case 'cm':
							if re.match('^[0-9]{3}$',num) and 150 <= int(num) <= 193:
								hasfields[3] = True
						case 'in':
							if re.match('^[0-9]{2}$',num) and 59 <= int(num) <= 76:
								hasfields[3] = True
				case 'hcl':
					if re.match('^#[0-9a-f]{6}$',value):
						hasfields[4] = True
				case 'ecl':
					if re.match('^amb|blu|brn|gry|grn|hzl|oth$',value):
						hasfields[5] = True
				case 'pid':
					if re.match('^[0-9]{9}$',value):
						hasfields[6] = True
		if all(hasfields):
			Nvalid += 1
	return Nvalid

print(day04_part1(passports))
print(day04_part2(passports))