# http://logia.oeiizk.waw.pl/logia/page.php?sr=logia11/2etap
import numpy as np


def pionek(w, p, c):
    tab = np.array([int(i) for i in p]).reshape((w, int(len(p) // w)))
    pairs = [(i, j) for i in range(w)
             for j in range(int(len(p) // w)) if tab[i][j] == c]
    distances = [abs(a[0]-b[0]) + abs(a[1]-b[1]) for a in pairs
                 for b in pairs if a != b]
    return min(distances)


print(pionek(2, "444474744474", 7))
print(pionek(1, "444474744474", 7))
print(pionek(3, "532378832375", 5))
