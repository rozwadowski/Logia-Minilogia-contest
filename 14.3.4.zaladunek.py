# http://logia.oeiizk.waw.pl/logia/page.php?sr=logia14/3etap

def ilesam(packs,trucks):
	i = 0
	while len(packs)>0:
		if packs[0][0] > 0:
			if packs[0][1] <= trucks[i]:
				trucks[i] -= packs[0][1]
				packs[0][0] -= 1
			else:
				i += 1
		else:
			packs.pop(0)

	return i+1
	
print( ilesam([[4, 5], [2, 2], [1, 20]], [17, 25, 25, 17, 25]) )
print( ilesam([[20, 1],[2, 5],[1, 3],[2, 7]], [25, 10, 10, 10, 10, 10]) )