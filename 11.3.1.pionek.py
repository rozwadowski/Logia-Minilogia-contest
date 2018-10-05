# http://logia.oeiizk.waw.pl/logia/page.php?sr=logia11/3etap

def pionek(s):
	tab = [ [i,j,k] for i in range(3) for j in range(3) for k in range(3) if s[i+3*j+9*k] == "c" ]
	return abs(tab[0][0]-tab[1][0])+abs(tab[0][1]-tab[1][1])+abs(tab[0][2]-tab[1][2])

print( pionek("cbbbbbbbbbbbbbbbbbbbbbbbbbc") )
print( pionek("bbbbbbbbbbbbbbbbbbbcbbbbbbc") )