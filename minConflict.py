import random
import time
random.seed(time.process_time())

def probabilistic_return(p):
    if p < 0:
        raise ValueError("p must be between 0 and 1.")

    return random.random() < p

def newArr(N):
    arr = []
    for i in range(N):
        arr.append(0)
    return arr

def build_conflict(queen_row, N):
    numqueen_row = newArr(N)
    numqueen_dia1 = newArr(2*N) #tu trai tren -> phai duoi row - col + N
    numqueen_dia2 = newArr(2*N) #tu phai tren -> trai duoi row + col

    for i in range(N):
        numqueen_row[queen_row[i]] += 1
        numqueen_dia1[queen_row[i] - i + N] += 1
        numqueen_dia2[queen_row[i] + i] += 1
    
    conflict = newArr(N)
    for i in range(N):
        conflict[i] = numqueen_row[queen_row[i]] + numqueen_dia1[queen_row[i] - i + N] + numqueen_dia2[queen_row[i] + i] - 1
    return conflict

def min_row_conflict(pickedCol, queen_row, N, numQueens):
    row_value = newArr(N) #How many queens conflict with this row

    #Add Random-Walk to prevent not go beyond local-minimum
    if (probabilistic_return(0.02) == True):
        return random.randint(0,N-1)

    for i in range(numQueens):
        row_value[queen_row[i]] += 1

        if 0 <= queen_row[i] - i + pickedCol < N: 
            row_value[queen_row[i] - i + pickedCol] += 1
        
        if 0 <= queen_row[i] + i - pickedCol < N:
            row_value[queen_row[i] + i - pickedCol] += 1
    
    return row_value.index(min(row_value))         

def update_conflict(newRow, pickedCol, queen_row, conflict, N):
    oldRow = queen_row[pickedCol]
    conflict[pickedCol] = 0

    for i in range(N):
        if i == pickedCol:
            continue

        if queen_row[i] == oldRow or queen_row[i] - i == oldRow - pickedCol or queen_row[i] + i == oldRow + pickedCol:
            conflict[i] -= 1

        if queen_row[i] == newRow or queen_row[i] - i == newRow - pickedCol or queen_row[i] + i == newRow + pickedCol:
            conflict[i] += 1
            conflict[pickedCol] += 1
    
    queen_row[pickedCol] = newRow

def heuristic_start_state(N):
    queen_row = newArr(N)

    for i in range(N):
        newRow = min_row_conflict(i, queen_row, N, i)
        queen_row[i] = newRow
    return queen_row

def initialize_start_state(N):
    queen_row = newArr(N)

    for i in range(N):
        queen_row[i] = random.randint(0,N-1)
    return queen_row

def minConflict(N, maxStep = 1000000):
    #queen_row = random_start_state(N) #Choose one of two ways to generate first state
    queen_row = heuristic_start_state(N) #Choose one of two ways to generate first state
    conflict = build_conflict(queen_row, N)

    for i in range(maxStep):
        if sum(conflict) == 0: #O(n)
            return queen_row
        
        #Choose random conflict queen
        pickedCol = random.choice([pos for pos in range(N) if conflict[pos] > 0]) #O(n)
        #Choose new row with min conflict
        newRow = min_row_conflict(pickedCol, queen_row, N, N) #O(n)
        #Update conflict list
        update_conflict(newRow, pickedCol, queen_row, conflict, N) #O(n)

print(minConflict(500))
