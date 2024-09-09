kogus = int(input())
kohad = {"X":0, "Y":1, "Z":2}

avatud = {}

for nr in range(kogus):
    rida = input.split()

    algus = [int(rida[0]), int(rida[1]), int(rida[2])]
    ots = algus[:]

    koht = kohad[rida[3][0]]

    if rida[3][1] == "+":
        ots[koht] += 1
    else: 
        ots[koht] -= 1

    algus = tuple(algus)
    ots = tuple(ots)

    if algus not in avatud:
        avatud[algus] = set()
    avatud[algus].add(ots)

    print(algus, ots)

algkoht = input().split()

seotud = {}

for koht in avatud:
    seotud[koht] = set()

    for koht2 in avatud[koht]:
        if koht in avatud[koht2]:
            seotud[koht].add(koht2)

print(avatud)
print(seotud)
