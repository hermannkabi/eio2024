soned = [input() for x in range(5)]
n = int(input())
juku_klopsud = [input() for x in range(n)]

numbrid = {}
clicks = 0

for sone in juku_klopsud:
    numbrid[sone] = max(numbrid.values() or [0]) + 1

numbrid = dict(sorted(numbrid.items(), key=lambda item: item[1]))

for voti in numbrid.keys():
    if (soned.index(voti) + 1) != int(numbrid[voti]):
        clicks += 1
        #Click this one
        numbrid[voti] = False
        n
