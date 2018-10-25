

def good(napis):
    for i in range(len(napis)):
        if (napis[i] == "c" or napis[i] == "z") and "n" in napis[i+1:]:
            return False
        if napis[i] == "z" and "c" in napis[i+1:]:
            return False
    return True


def check(napis, wynik, n):
    if n != 0:
        if good(napis):
            wynik.append(napis)
        else:
            for i in range(len(napis)):
                check(napis[:i] + napis[i+1:], wynik, n - 1)


def abc(napis):
    wynik = []
    i = 1
    while len(wynik) == 0:
        check(napis, wynik, i)
        i += 1
    return len(napis) - len(wynik[0])


print(abc('nncnnbffbbbccczzzcz'))
print(abc('zzzznnnnz'))
