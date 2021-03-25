from random import randrange

board = [[1, 2, 3], [4, "X", 6], [7, 8, 9]]
b2 = board[:]

# pos = {1: board[0][0], 2: board[0][1], 3: board[0][2], 4: board[1][0], 5: board[1][1], 6: board[1][2], 7: board[2][0], 8: board[2][1], 9: board[2][2]}


def display_board(board):
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|   {}   |   {}   |   {}   |".format(board[0][0], board[0][1], board[0][2]))
    print("|       |       |       |")
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|   {}   |   {}   |   {}   |".format(board[1][0], board[1][1], board[1][2]))
    print("|       |       |       |")
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|   {}   |   {}   |   {}   |".format(board[2][0], board[2][1], board[2][2]))
    print("|       |       |       |")
    print("+-------+-------+-------+")


def enter_move(board):
    user_move = "O"
    swapped = False

    def recur(taken = False):
        if taken:
            print("Already taken, try again!")
            enter_move(board)
        else:
            print("Wrong move! Let's try again.")
            enter_move(board)

    user_play = int(input("Enter your next play (1-9 only): "))

    if type(user_play) != int or user_play not in range(1,10):
        recur()
    else:
        for coord in make_list_of_free_fields(board):
            if board[coord[0]][coord[1]] == user_play:
                swapped = True
                board[coord[0]][coord[1]] = user_move

    if swapped:
        display_board(board)
    else:
        display_board(board)
        recur(True)

    if victory_for(board, user_move):
        print("Congratulations! You've won!")
    else:
        if len(make_list_of_free_fields(board)) < 1:
            print("It's a draw!")
        else:
            draw_move(board)


def make_list_of_free_fields(board):
    fields = []
    for i in range(3):
        for j in range(3):
            if type(board[i][j]) == int:
                fields.append((i, j))

    return fields


def victory_for(board, sign):
    pos = {1: board[0][0], 2: board[0][1], 3: board[0][2], 4: board[1][0], 5: board[1][1], 6: board[1][2],
           7: board[2][0], 8: board[2][1], 9: board[2][2]}

    if len(make_list_of_free_fields(board)) < 5:
        if pos[1] == pos[2] == pos[3] == sign or pos[1] == pos[4] == pos[7] == sign \
                or pos[1] == pos[5] == pos[9] == sign or pos[2] == pos[5] == pos[8] == sign \
                or pos[3] == pos[6] == pos[9] == sign or pos[3] == pos[5] == pos[7] == sign \
                or pos[4] == pos[5] == pos[6] == sign or pos[7] == pos[8] == pos[9] == sign:
            return True

    return False


def draw_move(board):
    comp_val = "X"
    sel = make_list_of_free_fields(board)
    move = sel[randrange(len(sel))]

    board[move[0]][move[1]] = comp_val
    display_board(board)

    if victory_for(board, comp_val):
        print("I won!")
    else:
        if len(make_list_of_free_fields(board)) < 1:
            print("It's a tie!")
        else:
            enter_move(board)

display_board(b2)
enter_move(b2)