x, y, n = int(input())/100, int(input())/100, int(input())

first_part_time = 4
second_part_time = 5

max_possible = first_part_time*x + second_part_time*y

if x<y:
    t1 = first_part_time
    t2 = min(5, (n-x*first_part_time)/y)
    print(int(t1+t2) if t1+t2 == int(t1+t2) else t1+t2)
else:
    t1 = second_part_time
    t2 = min(4, (n-y*second_part_time)/x)
    print(int(t1+t2) if t1+t2 == int(t1+t2) else t1+t2)