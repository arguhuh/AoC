infile = open("input/in21_real.txt","r")
# infile = open("input/in21_test.txt","r")
L = [(ingredients.split(), allergens.split(', ')) for ingredients, allergens in [line.strip('\n)').split(' (contains ') for line in infile]]

A = []
I = []
for ingredients, allergens in L:
	for allergen in allergens:
		A.append(allergen)
	for ingredient in ingredients:
		I.append(ingredient)
I = list(set(I))
Idict = {ingredient:i for i,ingredient in enumerate(I)}
Adict = {allergen:list(range(len(I))) for allergen in A}

for ingredients, allergens in L:
	ing_ind = [Idict[ingredient] for ingredient in ingredients]
	for allergen in allergens:
		to_remove = []
		for i in Adict[allergen]:
			if i not in ing_ind:
				to_remove.append(i)
		for i in to_remove:
			Adict[allergen].remove(i)

allergenic = set(i for s in Adict.values() for i in s)
allergen_free = [I[i] for i in range(len(I)) if i not in allergenic]

Nfree = 0
for ingredients, _ in L:
	for ingredient in ingredients:
		if ingredient in allergen_free:
			Nfree += 1

print(Nfree)

solved = []
while True:
	for allergen, ingredients in Adict.items():
		if len(ingredients) == 1:
			break
	else: #nobreak
		break
	ingredient = ingredients[0]
	solved.append((allergen, I[ingredient]))
	for allergen, ingredients in Adict.items():
		if ingredient in ingredients:
			Adict[allergen].remove(ingredient)

print(','.join(ingredient for allergen, ingredient in sorted(solved, key = lambda p: p[0])))
	