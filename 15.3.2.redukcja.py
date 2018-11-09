
def lewo(tab, n):
    return [[tab[n-j-1][i] for j in range(n)] for i in range(n)]


def spadanie(tab, n):
    for i in range(n):
        for k in range(n):
            for j in range(n-1):
                if tab[i][j] != 0 and tab[i][j+1] == 0:
                    tab[i][j], tab[i][j+1] = tab[i][j+1], tab[i][j]
    return tab


def redukuj(tab, n):
    for i in range(n):
        for k in range(n):
            for j in range(n-1):
                if tab[i][j] == tab[i][j+1]:
                    tab[i][j] = (tab[i][j]+tab[i][j+1]) % 10
                    tab[i][j+1] = 0
                    spadanie(tab, n)
    return tab


def redukcja(tab, nap):
    n = len(tab)
    tab = [[tab[i][j] for i in range(n)] for j in range(n)]
    # [[print(tab[i][j], end = " ")
    # for i in range(n)] and print() for j in range(n)]
    # print()
    for lit in nap:
        if lit == "l":
            tab = lewo(tab, n)
        elif lit == "p":
            tab = lewo(tab, n)
            tab = lewo(tab, n)
            tab = lewo(tab, n)
        elif lit == "g":
            tab = lewo(tab, n)
            tab = lewo(tab, n)

        tab = spadanie(tab, n)
        tab = redukuj(tab, n)

        if lit == "l":
            tab = lewo(tab, n)
            tab = lewo(tab, n)
            tab = lewo(tab, n)
        elif lit == "p":
            tab = lewo(tab, n)
        elif lit == "g":
            tab = lewo(tab, n)
            tab = lewo(tab, n)

        # [[print(tab[i][j],end = " ")
        # for i in range(n)] and print() for j in range(n)]
        # print()
    return tab


print(redukcja([[0, 2, 4], [4, 4, 8], [4, 0, 8]], 'dldld'))
print(redukcja([[1, 1, 1, 1], [1, 1, 1, 1],
                [1, 1, 1, 1], [1, 1, 1, 1]], 'lpdg'))
