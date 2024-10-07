soned = [input() for x in range(5)]
n = int(input())
juku_klopsud = [input() for x in range(n)]

numbrid = {}

for sone in juku_klopsud:
    if sone not in numbrid:
        numbrid[sone] = max(numbrid.values() or [0]) + 1
    else:
        numbrid[sone] = (max(numbrid.values() or [0]) + 1) if numbrid[sone] == False else False
        for i in range(len(list(numbrid.keys())[(soned.index(sone)+1):])):

            muuda_sone = list(numbrid.keys())[(soned.index(sone)+1):][i]
            numbrid[muuda_sone] = (numbrid[muuda_sone] or 0) - 1

            print(muuda_sone)
            print(numbrid)
print(numbrid)