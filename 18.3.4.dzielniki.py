# http://logia.oeiizk.waw.pl/logia/pliki/L183zad.pdf


def dzielniki(a, b):
    tab = [i for i in range(a, b+1) if int(i**0.5)**2 == i]
    counter = 0
    for num in tab:
        divisor = 1
        for i in range(1, num//2+1):
            if num % i == 0:
                divisor += 1
        if divisor == 3:
            counter += 1
    return counter


print(dzielniki(2, 6))
print(dzielniki(80000, 90000))
print(dzielniki(1, 1000000))
