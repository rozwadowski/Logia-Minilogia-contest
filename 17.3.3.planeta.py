def odleglosc(x1,y1,x2,y2,n):
	x = min( n-abs(x2-x1), abs(x2-x1) )
	y = min( n-abs(y2-y1), abs(y2-y1) )

	return x+y	


def planeta(n,tab):
	nr = [ 0 for i in range(len(tab)) ]	

	for dom1 in tab:
		for dom2 in tab:
			if dom1 != dom2:
				if odleglosc(dom1[0], dom1[1], dom2[0], dom2[1], n) <= 5 :
					if nr[tab.index(dom1)] == 0 and nr[tab.index(dom2)] == 0:
						nr[tab.index(dom1)] = max(nr) + 1
						nr[tab.index(dom2)] = max(nr) + 1
					elif nr[tab.index(dom1)] == 0:
						nr[tab.index(dom1)] = nr[tab.index(dom2)]
					else:
						nr[tab.index(dom2)] = nr[tab.index(dom1)]
	
	for i in range(len(nr)):
		if nr[i] == 0:
			nr[i] = max(nr) + 1
	
	maks = nr.count(nr[0])
	for i in range(1,max(nr)):
		if maks < nr.count(i):
			maks = nr.count(i)
			
	return(maks)
	
	
print(planeta(100,[[6,6],[6,11],[11,6],[11,11],[80,80]]))
print(planeta(12,[[3,1],[1,1],[1,3],[2,12],[9,5],[8,6]]))



					