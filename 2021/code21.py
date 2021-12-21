def day21_part1(p1,p2):
	s1 = 0
	s2 = 0
	d = 0
	while True:
		for j in range(3):
			d += 1
			p1 = (p1 + d - 1)%10 + 1
		s1 += p1
		if s1 > 999:
			return s2 * d
		for j in range(3):
			d += 1
			p2 = (p2 + d - 1)%10 + 1
		s2 += p2
		if s2 > 999:
			return s1 * d

def day21_part2(p1,p2):
	possible_scores = [(pi,pj,si,sj) for pi in range(1,11)
		for pj in range(1,11) for si in range(22) for sj in range(21)]\
		+ [(pi,pj,si,21) for pi in range(1,11) for pj in range(1,11)
		for si in range(21)]
	scores = dict.fromkeys(possible_scores,0)
	scores[(p1,p2,0,0)] = 1
	doing_anything = True
	while doing_anything:
		doing_anything = False
		#p1's turn
		scores_old = scores.copy()
		for pi,pj,si,sj in scores_old:
			n = scores_old[(pi,pj,si,sj)]
			if n > 0 and si < 21 and sj < 21:
				doing_anything = True
				scores[(pi,pj,si,sj)] -= n
				#3 rolls split the universe into 27
				#p1 rolls 3 in 1 universe
				pafter = (pi + 2)%10 + 1
				safter = min(21,si + pafter)
				scores[(pafter,pj,safter,sj)] += n
				#p1 rolls 4 in 3 universes
				pafter = (pi + 3)%10 + 1
				safter = min(21,si + pafter)
				scores[(pafter,pj,safter,sj)] += n*3
				#p1 rolls 5 in 6 universes
				pafter = (pi + 4)%10 + 1
				safter = min(21,si + pafter)
				scores[(pafter,pj,safter,sj)] += n*6
				#p1 rolls 6 in 7 universes
				pafter = (pi + 5)%10 + 1
				safter = min(21,si + pafter)
				scores[(pafter,pj,safter,sj)] += n*7
				#p1 rolls 7 in 6 universes
				pafter = (pi + 6)%10 + 1
				safter = min(21,si + pafter)
				scores[(pafter,pj,safter,sj)] += n*6
				#p1 rolls 8 in 3 universes
				pafter = (pi + 7)%10 + 1
				safter = min(21,si + pafter)
				scores[(pafter,pj,safter,sj)] += n*3
				#p1 rolls 9 in 1 universe
				pafter = (pi + 8)%10 + 1
				safter = min(21,si + pafter)
				scores[(pafter,pj,safter,sj)] += n
		#p2's turn
		scores_old = scores.copy()
		for pi,pj,si,sj in scores_old:
			n = scores_old[(pi,pj,si,sj)]
			if n > 0 and si < 21 and sj < 21:
				doing_anything = True
				scores[(pi,pj,si,sj)] -= n
				#3 rolls split the universe into 27
				#p2 rolls 3 in 1 universe
				pafter = (pj + 2)%10 + 1
				safter = min(21,sj + pafter)
				scores[(pi,pafter,si,safter)] += n
				#p2 rolls 4 in 3 universes
				pafter = (pj + 3)%10 + 1
				safter = min(21,sj + pafter)
				scores[(pi,pafter,si,safter)] += n*3
				#p2 rolls 5 in 6 universes
				pafter = (pj + 4)%10 + 1
				safter = min(21,sj + pafter)
				scores[(pi,pafter,si,safter)] += n*6
				#p2 rolls 6 in 7 universes
				pafter = (pj + 5)%10 + 1
				safter = min(21,sj + pafter)
				scores[(pi,pafter,si,safter)] += n*7
				#p2 rolls 7 in 6 universes
				pafter = (pj + 6)%10 + 1
				safter = min(21,sj + pafter)
				scores[(pi,pafter,si,safter)] += n*6
				#p2 rolls 8 in 3 universes
				pafter = (pj + 7)%10 + 1
				safter = min(21,sj + pafter)
				scores[(pi,pafter,si,safter)] += n*3
				#p2 rolls 9 in 1 universe
				pafter = (pj + 8)%10 + 1
				safter = min(21,sj + pafter)
				scores[(pi,pafter,si,safter)] += n
	w1 = 0
	w2 = 0
	for pi,pj,si,sj in scores:
		if si == 21:
			w1 += scores[(pi,pj,si,sj)]
		elif sj == 21:
			w2 += scores[(pi,pj,si,sj)]
	print(w1)
	print(w2)

# p1 = 4; p2 = 8
p1 = 5; p2 = 9

print(day21_part1(p1,p2))
day21_part2(p1,p2)