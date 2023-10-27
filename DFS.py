import time

def init_nQueen_Board(queens_board, Number_of_nQueen):
    for i in range(Number_of_nQueen):
        queens_board.append(0)
def is_Safe_to_Place(queens_board, row, current):
    for i in range(current):
        if (queens_board[i] == row) or (abs(queens_board[i]-row) == abs(current-i)):
            return False
    return True
def DFS_nQueens_Game(queens_board, Number_of_nQueen, current):
    if current == Number_of_nQueen:
        return True
    else:
        for i in range (Number_of_nQueen):
            if is_Safe_to_Place(queens_board, i, current):
                queens_board[current] = i       #Place queen at row #i
                if DFS_nQueens_Game(queens_board, Number_of_nQueen, current + 1):
                    return True
    return False
def Play_nQueen(Number_of_nQueen):
    queens_board = []
    start_time = time.time()
    init_nQueen_Board(queens_board, Number_of_nQueen)
    if DFS_nQueens_Game(queens_board, Number_of_nQueen, 0):
        print (queens_board)
    else:
        print ("No result found!!!")
    end_time = time.time()
    time_elapsed = end_time - start_time
    print(f"Time: {time_elapsed:.5f} second")
Play_nQueen(3)
        
    


    




    


