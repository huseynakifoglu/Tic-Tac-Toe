money = int(input())

# animal_list = [["chicken", "23"], ["goat", "678"], ["pig", "1296"], ["cow", "3848"], ["sheep", "6769"]]
animal_list = [["chicken", "chickens", 23], ["goat", "goat", 678], ["pig", "pigs", 1296], ["cow", "cows", 3848],
               ["sheep", "sheep", 6769]]


def find_min(operation):
    my_minn = operation
    if operation < my_minn:
        my_minn = operation
        return my_minn


for x in animal_list:
    if money // x[2] < 1:
        print("None")
        break
    elif money // x[2] == 1:
        print("1 " + x[0])
        break
    else:
        find_min(money - x[2])
        print(str(money // x[2]) + " " + x[1])
        break