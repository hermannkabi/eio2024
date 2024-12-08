m, n = [int(x) for x in input().split(" ")]

longest = []

def yhisosa_algusest(sone1, sone2):
    lyhem = min(sone1, sone2)
    pikem = sone1 if lyhem == sone2 else sone2
    for i in range(len(pikem)):
        if len(lyhem) <= i:
            return lyhem
        if sone1[i] != sone2[i]:
            return lyhem[0:i] if i > 0 else ""

for i in range(n):
    soovid = input().split(" ")
    longest_empty = len(longest) == 0
    for soov in soovid:
        if longest_empty:
            longest.append(soov)
        else:
            for long in longest:
                print(yhisosa_algusest(soov, long))
                if len(yhisosa_algusest(soov, long)) == 0:
                    longest.remove(long)
        
    
print(longest)
