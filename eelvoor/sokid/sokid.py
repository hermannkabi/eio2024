n = int(input())
data = {}
counter = 0

odd = []

for i in range(n):
    sokk = input()
    if sokk in data:
        data[sokk] = data[sokk] + 1
    else:
        data[sokk] = 1

if n % 2 == 1:
    print("-1")
    exit()

for sokk in data:
    if data[sokk] % 2 != 0:
        odd.append(sokk)
        for sokk2 in odd:
            if sokk != sokk2 and data[sokk2] % 2 == 1:
                counter += 1
                data[sokk] = 0
                data[sokk2] = 0
                odd.remove(sokk)
                odd.remove(sokk2)
                break

print(counter)