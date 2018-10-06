# http://logia.oeiizk.waw.pl/logia/pliki/L183zad.pdf


def perm(tab,k):
    results = []
    if k==0:
        results.append(tab.copy())
    else:
        for i in range(k):
            tab[i],tab[k-1]=tab[k-1],tab[i]
            results.extend( perm(tab, k-1) )
            tab[i],tab[k-1]=tab[k-1],tab[i]
    return results

def strony(n,tab):
	alph = "abcdefgh"
	counter = 0
	alph = alph[0:n]
	alph = [i for i in alph]
	for p in perm(alph,len(alph)):
		ok = True
		for inf in tab:
			if p.index(inf[0]) > p.index(inf[1]):
				ok = False
		if ok:
			counter += 1
	return counter
print( strony(4,["ab","ac","ad","db"]) )
print( strony(2,["ba"]) )