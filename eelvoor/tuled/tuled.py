x, y, n = int(input())/100, int(input())/100, int(input())

first_part_time = 4
second_part_time = 5

max_possible = first_part_time*x + second_part_time*y

if n>max_possible:
    print("9")
    exit()

if x<y:
    t1 = n/x if first_part_time*x > n else first_part_time
    t2 = min(5, (n-x*t1)/y)
    print(int(t1+t2) if t1+t2 == int(t1+t2) else t1+t2)
else:
    t1 = n/y if second_part_time*y > n else second_part_time
    t2 = min(4, (n-y*t1)/x)
    print(int(t1+t2) if t1+t2 == int(t1+t2) else t1+t2)