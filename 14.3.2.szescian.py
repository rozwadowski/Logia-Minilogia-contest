# http://logia.oeiizk.waw.pl/logia/page.php?sr=logia14/3etap

def obok(n,p):
	tab= [[[ 1+i+j*n+k*n**2 for k in range(n)]for j in range(n)] for i in range(n)]
	cell = [ (i,j,k) for k in range(n)for j in range(n) for i in range(n) if tab[i][j][k]==p ][0]
		
	wyniki=[]
	if cell[0] < n-1:
		wyniki.append(tab[cell[0]+1][cell[1]][cell[2]])
	if cell[0] > 0:
		wyniki.append(tab[cell[0]-1][cell[1]][cell[2]])
	if cell[1] < n-1:
		wyniki.append(tab[cell[0]][cell[1]+1][cell[2]])
	if cell[1] > 0:
		wyniki.append(tab[cell[0]][cell[1]-1][cell[2]])
	if cell[2] < n-1:
		wyniki.append(tab[cell[0]][cell[1]][cell[2]+1])
	if cell[2] > 0:
		wyniki.append(tab[cell[0]][cell[1]][cell[2]-1])		

	wyniki.sort()
	return wyniki

print(obok(3,11))
print(obok(7,1))
print(obok(10,1000))


