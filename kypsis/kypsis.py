# Küpsise mängu minimax
inimese_kaik = True
stats = []

def kaik(koht, seis, mangija):
    print("Algne",seis)
    mod = koht % 3
    for i in range(len(seis)):
        if seis[i] != ".":
            if i % 3 == mod and i <= koht:
                seis[i] = "."
                for j in range(2-mod):
                    seis[i+j+1] = "."

    if "K" not in seis:
        print("Inimene kaotas" if mangija else "Robot kaotas")
        stats.append("R" if mangija else "I")
        return

    mangija2 = not mangija
    for i in range(len(seis)):
        if seis[i] != ".":
            kaik(i, seis, mangija2)
    
for i in range(9):
    kaik(i, list("MMMMMMMMM"), inimese_kaik)


print("Inimene võidab", str(stats.count("I")/len(stats)*100)+"% kordadest")