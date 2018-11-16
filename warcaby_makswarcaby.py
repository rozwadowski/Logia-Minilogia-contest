

def bij(tab, n, i, j, wyniki, gl):
    if i >= 2 and j >= 2:
        if tab[i-1][j-1] == 2 and tab[i-2][j-2] == 0:
            newtab = tab.copy()
            newtab[i-1][j-1] = 1
            newtab[i-2][j-2] = 1
            bij(newtab, n, i-2, j-2, wyniki, gl+1)
    if i >= 2 and j <= n - 3:
        if tab[i-1][j+1] == 2 and tab[i-2][j+2] == 0:
            newtab = tab.copy()
            newtab[i-1][j+1] = 1
            newtab[i-2][j+2] = 1
            bij(newtab, n, i-2, j+2, wyniki, gl+1)
    if i <= n - 3 and j <= n - 3:
        if tab[i+1][j+1] == 2 and tab[i+2][j+2] == 0:
            newtab = tab.copy()
            newtab[i+1][j+1] = 1
            newtab[i+2][j+2] = 1
            bij(newtab, n, i+2, j+2, wyniki, gl+1)
    if i <= n - 3 and j >= 2:
        if tab[i+1][j-1] == 2 and tab[i+2][j-2] == 0:
            newtab = tab.copy()
            newtab[i+1][j-1] = 1
            newtab[i+2][j-2] = 1
            bij(newtab, n, i+2, j-2, wyniki, gl+1)
    wyniki.append(gl)


def makswarcaby(n, tab1, tab2):
    tab = [[0 for i in range(n)] for j in range(n)]

    for nr in tab1:
        i = int((nr-1)/n)
        j = nr-i*n-1
        tab[i][j] = 1
    for nr in tab2:
        i = int((nr-1)/n)
        j = nr-i*n-1
        tab[i][j] = 2

    [[print(tab[j][i], end="\t") for i in range(n)]
     and print() for j in range(n)]

    wyniki = []
    for i in range(n):
        for j in range(n):
            if tab[i][j] == 1:
                bij(tab, n, i, j, wyniki, 0)
    print(wyniki)
    return max(wyniki)


print(makswarcaby(6, [31, 33], [9, 14, 26, 28]))
print(makswarcaby(6, [1], [8]))
