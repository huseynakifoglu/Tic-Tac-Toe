number = int(input())
mylist = []
for _i in range(number):
    mylist.append([a_list for a_list in input().split()])

print([gamer[0] for gamer in mylist if gamer[1] == "win"])
print(len([gamer[0] for gamer in mylist if gamer[1] == "win"]))
