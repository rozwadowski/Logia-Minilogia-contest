

def szyfrujweza(n, napis):
    i = 0
    while i*n < len(napis):
        if i % 2 == 1:
            napis = napis[:i*n] + napis[i*n:(i+1)*n][::-1] + napis[(i+1)*n:]
        i += 1
    # print(napis)
    wynik = ""
    for i in range(n):
        j = i
        while j < len(napis):
            wynik += napis[j]
            j += n

    return wynik


print(szyfrujweza(4, "abcdefghij"))
print(szyfrujweza(2, "abcdefghij"))
print(szyfrujweza(1, "abcdefghij"))
