# http://logia.oeiizk.waw.pl/logia/page.php?sr=logia11/2etap

def ilep(s):
	counter = 0
	for a in [s[i:j+1] for i in range(len(s)) for j in range(i,len(s))]:
		if a == a[::-1]:
			counter += 1
	return counter

print( ilep("kajak") )
print( ilep("mama") )
