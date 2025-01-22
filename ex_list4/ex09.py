def print_board(board: list):
    for line in board:
        print(f"{line[0]} {line[1]} {line[2]}")


def check_win(board: list):
    for line in board:
        if line[0] == line[1] == line[2]:
            if line[0] == "X":
                return 1
            elif line[0] == "O":
                return 2
    
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i]:
            if board[0][i] == "X":
                return 1
            elif board[0][i] == "O":
                return 2
            
    if board[0][0] == board[1][1] == board[2][2]:
        if board[0][0] == "X":
            return 1
        elif board[0][0] == "O":
            return 2
        
    if board[0][2] == board[1][1] == board[2][0]:
        if board[0][2] == "X":
            return 1
        elif board[0][2] == "O":
            return 2
        
    return 0


def play(board: list):
    for i in range(1, 10):
        print_board(board)

        if i % 2 == 0:
            player = "O"
        else:
            player = "X"

        while True:
            line = int(input("\nLinha: ")) - 1
            collumn = int(input("Coluna: ")) - 1
            print()

            if board[line][collumn] == "_":
                board[line][collumn] = player
                break
            else:
                print("Jogada inválida!\n")

        if check_win(board) == 1:
            print_board(board)
            print("\nJogador 1 ganhou!")
            break
        elif check_win(board) == 2:
            print_board(board)
            print("\nJogador 2 ganhou!")
            break
        elif i == 9 and check_win(board) == 0:
            print_board(board)
            print("\nVelha!")
        

board = [["_", "_", "_"],["_", "_", "_"],["_", "_", "_"]]
play(board)