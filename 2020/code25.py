from itertools import count

infile = open("input/in25_real.txt","r")
# infile = open("input/in25_test.txt","r")

card_key = int(next(infile).strip())
door_key = int(next(infile).strip())

def transform(subject,loop_size):
	n = 1
	for _ in range(loop_size):
		n = n * subject % 20201227
	return n

def day25_part1(card_key, door_key):
	card_loop = door_loop = None
	key = 1
	for loop_size in count(1):
		key = key * 7 % 20201227
		if key == card_key:
			card_loop = loop_size
			break
		if key == door_key:
			door_loop = loop_size
			break
	if card_loop:
		return transform(door_key,card_loop)
	else:
		return transform(card_key,door_loop)

print(day25_part1(card_key, door_key))