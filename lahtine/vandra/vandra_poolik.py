def ristkulikud_kattuvad(ristkulik_1, ristkulik_2):
    x1, y1, x2, y2 = ristkulik_1
    x3, y3, x4, y4 = ristkulik_2
    return not (x2 <= x3 or x4 <= x1 or y2 <= y3 or y4 <= y1)

n = int(input())

ristkulikud = []
for i in range(n):
    x1, y1, x2, y2 = [int(x) for x in input().split()]
    ristkulikud.append((x1, y1, x2, y2))

for i in range(n):
    for j in range(i + 1, n):
        if ristkulikud_kattuvad(ristkulikud[i], ristkulikud[j]):
            print("JAH")
            exit()
print("EI")