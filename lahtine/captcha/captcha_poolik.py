oiged = [input() for i in range(5)]
n = int(input())
venna_valikud = [input() for i in range(n)]

#Kaks muutujat, et hallata numbreid ja järjekorda eraldi
praegused_numbrid = {} 
praegune_jarjestus = []

for vajutus in venna_valikud:
    if vajutus in praegused_numbrid:
        del praegused_numbrid[vajutus]
        praegune_jarjestus.remove(vajutus)
    else:
        praegused_numbrid[vajutus] = len(praegune_jarjestus) + 1
        praegune_jarjestus.append(vajutus)

tulemus = []
for i, oige_valik in enumerate(oiged):
    if i < len(praegune_jarjestus) and praegune_jarjestus[i] == oige_valik:
        continue
    else:
        if oige_valik in praegused_numbrid:
            tulemus.append(oige_valik)
            praegune_jarjestus.remove(oige_valik)
            del praegused_numbrid[oige_valik]
        
        tulemus.append(oige_valik)
        praegused_numbrid[oige_valik] = len(praegune_jarjestus) + 1
        praegune_jarjestus.append(oige_valik)

print(len(tulemus))
for vajutus in tulemus:
    print(vajutus)