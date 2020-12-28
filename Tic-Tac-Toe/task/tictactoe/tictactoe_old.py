# this is the function that converts 1D list to 2D
def to_matrix(chars, n):
    return [chars[i:i + n] for i in range(0, len(chars), n)]


# this is the function that controls the asking coordination
def get_valid_coordinates(prompt):
    while True:
        try:
            get_valid_coordinates.x, get_valid_coordinates.y = input(prompt).split()
        except ValueError:
            print("You should enter numbers!")
            continue

        if not get_valid_coordinates.x.isdigit() or not get_valid_coordinates.y.isdigit():
            print("You should enter numbers!")
            continue

        if int(get_valid_coordinates.x) < 1 or int(get_valid_coordinates.x) > 3 or int(
                get_valid_coordinates.y) < 1 or int(get_valid_coordinates.y) > 3:
            print("Coordinates should be from 1 to 3!")
            continue

        if chars[int(get_valid_coordinates.x) - 1][int(get_valid_coordinates.y) - 1] != "_":
            print("This cell is occupied! Choose another one!")
            continue

        else:
            break
    return get_valid_coordinates.x, get_valid_coordinates.y


# fill the list with empty symbols for string format
chars = to_matrix([" "] * 9)

string = f""" \
---------
| {chars[0][0]} {chars[0][1]} {chars[0][2]} |
| {chars[1][0]} {chars[1][1]} {chars[1][2]} |
| {chars[2][0]} {chars[2][1]} {chars[2][2]} |
--------- \
"""
a = chars[0][0]
b = chars[0][1]
c = chars[0][2]
d = chars[1][0]
e = chars[1][1]
f = chars[1][2]
g = chars[2][0]
h = chars[2][1]
j = chars[2][2]

print(string)


def print_winner(winner):
    print(winner + " wins")


def print_draw(condition):
    if condition:
        print("Draw")


def print_game_not_finished(condition):
    if condition:
        print("Game not finished")


def print_impossible(condition):
    if condition:
        print("Impossible")


def is_someone_wins():
    if (a == d == g == "X" and b == e == h == "O") or (a == d == g == "X" and c == f == j == "O"):
        print_impossible(True)
    elif (b == e == h == "X" and a == d == g == "O") or (b == e == h == "X" and c == f == j == "O"):
        print_impossible()
    elif (c == f == j == "X" and a == d == g == "O") or (c == f == j == "X" and b == e == h == "O"):
        print_impossible()
    elif (abs(chars.count("X") - chars.count("O"))) >= 2:
        print_impossible(True)
    elif a == b == c or a == d == g or a == e == j:
        return True, print_winner(a)
    elif b == e == f or d == e == f:
        return True, print_winner(b)
    elif c == e == g or c == f == j:
        return True, print_winner(c)
    elif g == h == j:
        return True, print_winner(g)
    elif " " in chars:
        print_game_not_finished(True)
    else:
        print_draw(True)


game_finished = False

# x, y = input("Enter the coordinates: ").split()
# print("x coordinate: ", x)
# print("y coordinate: ", y)
get_valid_coordinates("Enter the coordinates: ")
chars[(int(get_valid_coordinates.x)) - 1][(int(get_valid_coordinates.y)) - 1] = "X"
print(chars[(int(get_valid_coordinates.x)) - 1][(int(get_valid_coordinates.y)) - 1])

string = f""" \
---------
| {chars[0][0]} {chars[0][1]} {chars[0][2]} |
| {chars[1][0]} {chars[1][1]} {chars[1][2]} |
| {chars[2][0]} {chars[2][1]} {chars[2][2]} |
--------- \
"""

print(string)
# print(string.format(a=a, b=b, c=c, d=d, e=e, f=f, g=g, h=h, j=j))
