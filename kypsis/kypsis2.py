import random

on_inimese_kaik = True
mang_labi = False

ruudustik = [
    ["O", "O", "O"],
    ["O", "O", "O"],
    ["X", "O", "O"],
]

def tee_kaik(rida, tulp):
    uus_ruudustik = ruudustik.copy()
    rea_nr = rida
    while rea_nr >= 0:
        uus_ruudustik[rea_nr][tulp:] = ["-"]*(len(ruudustik[rea_nr]) - tulp)
        rea_nr -= 1

    for x in uus_ruudustik:
        print(" ".join(x))
    print()

    kogu_list = [e for x in uus_ruudustik for e in x]

    if "X" not in kogu_list:
        return False
    
    return uus_ruudustik

def koht_tuhi(rida, tulp):
    return ruudustik[rida][tulp] == "-"

def saa_inimese_valik():
    rida, tulp = int(input("Sisesta käigu rida: ")), int(input("Sisesta käigu tulp: "))
    if koht_tuhi(rida, tulp):
        print("Sellel kohal pole küpsist")
        saa_inimese_valik()
    return rida, tulp

def saa_arvuti_valik():
    valikud = [e for x in ruudustik for e in x]
    valikud_paarid = []
    for e in valikud:
        if e != "-":
            idx = valikud.index(e)
            valikud_paarid.append([idx // 3, idx % 3])

    valitud_paar = random.choice(valikud_paarid)
        
    print("Arvuti käib", valitud_paar[0], valitud_paar[1])
    print()
    return valitud_paar[0], valitud_paar[1]

def inimese_kaik():
    global ruudustik, mang_labi, on_inimese_kaik

    rida, tulp = saa_inimese_valik()
    tulemus = tee_kaik(rida, tulp)

    if tulemus:
        ruudustik = tulemus
        on_inimese_kaik = not on_inimese_kaik
    else:
        mang_labi = True

def arvuti_kaik():
    global ruudustik, mang_labi, on_inimese_kaik
    rida, tulp = saa_arvuti_valik()
    tulemus = tee_kaik(rida, tulp)

    if tulemus:
        ruudustik = tulemus
        on_inimese_kaik = not on_inimese_kaik
    else:
        mang_labi = True
    


while not mang_labi:
    if on_inimese_kaik:
        inimese_kaik()
    else:
        arvuti_kaik()

print("Arvuti võit" if on_inimese_kaik else "Inimese võit")