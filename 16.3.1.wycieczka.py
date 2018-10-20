
def dziel(m,k,wynik):
	if len(k) > 1:	# jesli da sie podzielic zestaw Karola
		i = k.index(m[0])	# miejsce podzialu tablicy Karola jest tym samym co pierwszy element tablicy Malgosi
		dziel(m[1:i+1], k[:i], wynik)	# lewa strona drzewa
		dziel(m[i+1:], k[i+1:], wynik)	# prawa strona drzewa
		wynik.append(k[i])				# srodek
	elif len(k) == 1:
		wynik.append(k[0])				# na samym dole drzewa

def opis(m,k):
	wynik = []
	dziel(m,k,wynik)
	return wynik



	
print(
opis([1,2,4,5,3,6,7],[4,2,5,1,6,3,7]),	
opis([1,2,4,3],[4,2,1,3]), 
opis([4,2,1,3,5,6],[1,2,3,4,6,5])
)