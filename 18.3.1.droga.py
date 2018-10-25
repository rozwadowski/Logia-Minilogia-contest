# http://logia.oeiizk.waw.pl/logia/pliki/L183zad.pdf


def droga(tab):
    # szkuanie drogi od A
    drogaA = ['A']
    for i in range(26):
        for info in tab:
            if info[0] == drogaA[-1] and not info[1] in drogaA:
                drogaA.append(info[1])
                break
    # szukanie drogi od Z
    drogaZ = ['Z']
    for i in range(26):
        for info in tab:
            if info[0] == drogaZ[-1] and not info[1] in drogaZ:
                drogaZ.append(info[1])
                break
    # znalezienie miejsca wspolnego
    spotkania = []
    for z in range(len(drogaZ)):
        for a in range(len(drogaA)):
            if drogaA[a] == drogaZ[z]:
                spotkania.append(a+z)
    if len(spotkania) > 0:
        return min(spotkania)
    else:
        return -1


print(droga([['Z', 'D'], ['A', 'B'], ['F', 'B'], ['B', 'C'],
            ['C', 'D'], ['D', 'F']]))
print(droga([['A', 'B'], ['G', 'H'], ['B', 'C'], ['Z', 'C']]))
print(droga([['A', 'B'], ['Z', 'D']]))
