kell_praegu = input().split(" ")
kell_praegu = 60*int(kell_praegu[0]) + int(kell_praegu[1])

ajavarud = {}

for i in range(int(input())):
    peatus_tund, peatus_minut, peatus_kaugus = [int(x) for x in input().split(" ")]
    peatus_aeg = peatus_tund*60 + peatus_minut
    jouab_kohale = kell_praegu + peatus_kaugus

    ajavaru = peatus_aeg - jouab_kohale

    ajavarud[i+1] = ajavaru

ajavarud = {k: v for k, v in sorted(ajavarud.items(), key=lambda item: item[1], reverse=True)}

maks_varu = next(iter(ajavarud))

print("JAH" if ajavarud[maks_varu] >= 0 else "EI")
print(maks_varu)
