#u = int(input())

#open_doors = []

#for i in range(u):
#    open_doors.append(input().split(" "))

#leaking_module = input().split(" ")

open_doors = [['2', '1', '1', 'X-'], ['1', '1', '1', 'X+'], ['1', '1', '1', 'Z+'], ['3', '1', '1', 'X-'], ['1', '1', '2', 'Z-']]
leaking_module = ["1", "1", "1"]

modules_leaking = []

translate = {"X":0, "Y":1, "Z":2}

# Returns modules next to module
def next_to(module):
    module = [int(x) for x in module[0:3]]
    next_to = [[module[0]-1, module[1], module[2]], [module[0]+1, module[1], module[2]], [module[0], module[1]-1, module[2]], [module[0], module[1]+1, module[2]], [module[0], module[1], module[2]-1], [module[0], module[1], module[2]+1]]

    for pot in next_to:
        if -1 in pot or 0 in pot:
            next_to.remove(pot)

    return next_to

# What doors are open that are next to the module
def doors_open(module):
    open_doors_for_module = [x for x in open_doors if x[0] == module[0] and x[1] == module[1] and x[2] == module[2]]
    

    return open_doors_for_module

print(doors_open(leaking_module))