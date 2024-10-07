n = int(input())
magnets = sorted(list(input().strip().replace("0", "")))

n = len(magnets)

if n == 0:
    print("0")
elif n == 1:
    print(magnets[0])
else:
    first_num = []
    second_num = []
    for i in range(n):
        (first_num if i % 2 == 0 else second_num).append(magnets[i])

    print(int("".join(first_num)) + int("".join(second_num)))
