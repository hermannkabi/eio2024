x_max, y_max, x1, y1, x2, y2 = [int(x) for x in input().split(" ")]

paper_area = x_max*y_max

#parall y-telg
if x1 == x2:
    area = y_max*x1
    area2 = paper_area - area
    print(max(area, area2))


#parall x-telg
if y1 == y2:
    area = x_max*y1
    area2 = paper_area - area
    print(max(area, area2))

# 45-kraadine nurk
tipud = [(0,0), (0, y_max), (x_max, 0), (x_max, y_max)]

punkt1 = (x1, y1)
punkt2 = (x2, y2)

oige_tipp = tipud[0]

for tipp in tipud:
    if (punkt1[0] == tipp[0] and punkt2[1] == tipp[1]) or (punkt1[1] == tipp[1] and punkt2[0] == tipp[0]):
        oige_tipp = tipp
        haar1 = abs(punkt1[0] - oige_tipp[0] if punkt1[0] != oige_tipp[0] else punkt1[1] - oige_tipp[1])
        haar2 = abs(punkt2[0] - oige_tipp[0] if punkt2[0] != oige_tipp[0] else punkt2[1] - oige_tipp[1])

        area = haar1*haar2/2
        area2 = paper_area - area
        print(max(area, area2))
