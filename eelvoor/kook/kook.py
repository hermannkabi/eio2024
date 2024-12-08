n = int(input())
pakapikud = [int(x) for x in input().split(" ")]
koogid = [int(x) for x in input().split(" ")]

tegurid = []
saab_teha = False
oige_tegur = 0

jarjekord = []
voetud = []

if n == 2:
    for kook in koogid:
        koogi_tegurid = []
        for pakapikk in pakapikud:
            tegur = kook/pakapikk
            if tegur not in koogi_tegurid:
                koogi_tegurid.append(tegur)
                tegurid.append(tegur)
    for i in set(tegurid):
        if tegurid.count(i) >= n:
            saab_teha = True
            oige_tegur = i
    print("JAH" if saab_teha else "EI")
    
else:
    for i in range(n):
        tegur = koogid[i]/pakapikud[i]
        if oige_tegur == 0:
            oige_tegur = tegur
        if tegur != oige_tegur:
            print("EI")
            exit()
    print("JAH")
    print(" ".join([str(i+1) for i in range(n)]))
    exit()

if saab_teha:
    for kook in koogid:
        vastav_pakapikk = round(kook/oige_tegur)
        if pakapikud.count(vastav_pakapikk) == 1:
            jarjekord.append(str(pakapikud.index(vastav_pakapikk) + 1))
        else:
            for i in range(len(pakapikud)):
                if pakapikud[i] == vastav_pakapikk and i not in voetud:
                    voetud.append(i)
                    jarjekord.append(str(i+1))

    print(" ".join(jarjekord))