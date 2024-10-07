from itertools import combinations

n = int(input())

andmed = [input() for i in range(n)]
data = []

def intersects(esimene, teine):
    return not (esimene[2] < teine[0]
                or esimene[0] > teine[2]
                or esimene[3] < teine[1]
                or esimene[1] > teine[3])
if n == 1:
    print("EI")
    exit()

for rida in andmed:
    data.append([int(x) for x in rida.split(" ")])


for (i, j) in combinations(data, 2):
    if intersects(i, j):
        print("JAH")
        exit()

print("EI")



