# this is the function that converts 1D list to 2D
def to_matrix(oneDim, n):
    return [oneDim[i:i + n] for i in range(0, len(oneDim), n)]


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

        if chars[int(get_valid_coordinates.x) - 1][int(get_valid_coordinates.y) - 1] != " ":
            print("This cell is occupied! Choose another one!")
            continue

        else:
            break
    return get_valid_coordinates.x, get_valid_coordinates.y


def print_winner(winner):
    print(winner + " wins")


def print_draw():
    print("Draw")


def check_winner():
    if (chars[0][0] == chars[0][1] == chars[0][2]
        or chars[0][0] == chars[1][0] == chars[2][0]
        or chars[0][0] == chars[1][1] == chars[2][2]) \
            and chars[0][0] != " ":
        print_winner(chars[0][0])
        return True

    elif (chars[0][1] == chars[1][1] == chars[2][1]
          or chars[1][0] == chars[1][1] == chars[1][2]) and chars[1][1] != " ":

        print_winner(chars[1][1])
        return True
    elif (chars[0][2] == chars[1][1] == chars[2][0]
          or chars[0][2] == chars[1][2] == chars[2][2]) and chars[0][2] != " ":
        print_winner(chars[0][2])
        return True

    elif chars[2][0] == chars[2][1] == chars[2][2] != " ":
        print_winner(chars[2][0])
        return True
    elif chars[0][0] != " " and chars[0][1] != " " and chars[0][2] != " " \
            and chars[1][0] != " " and chars[1][1] != " " and chars[1][2] != " "\
            and chars[2][0] != " " and chars[2][1] != " " and chars[2][2] != " ":
        print_draw()
        return True
    else:
        return False


game_finished = False
# fill the list with empty symbols for string format
chars = to_matrix([" "] * 9, 3)

string = f""" \
---------
| {chars[0][0]} {chars[0][1]} {chars[0][2]} |
| {chars[1][0]} {chars[1][1]} {chars[1][2]} |
| {chars[2][0]} {chars[2][1]} {chars[2][2]} |
--------- \
"""

print(string)
plays = ["X", "O", "X", "O", "X", "O", "X", "O", "X"]
index = 0
while not game_finished:

    get_valid_coordinates("Enter the coordinates: ")
    chars[(int(get_valid_coordinates.x)) - 1][(int(get_valid_coordinates.y)) - 1] = plays[index]
    string = f""" \
    ---------
    | {chars[0][0]} {chars[0][1]} {chars[0][2]} |
    | {chars[1][0]} {chars[1][1]} {chars[1][2]} |
    | {chars[2][0]} {chars[2][1]} {chars[2][2]} |
    --------- \
    """
    print(string)
    index += 1

    if check_winner():
        game_finished = True
        break
    else:
        continue
