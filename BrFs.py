from collections import deque 
import time

def BFS_Solution(n):
    queue = deque()
    for i in range (n):
        queue.append([i])

    queen = 1
    while(queen != n):
        qlen = len(queue)
        for i in range (qlen):
            state = queue.popleft()
            forbidden = set()

            for j, pos in enumerate(state):
                forbidden.add(pos)
                forbidden.add(pos + (queen - j))
                forbidden.add(pos - (queen - j))
            for k in range (n):
                if k not in forbidden:
                    temp = state[:]
                    temp.append(k)
                    if len(temp) == n:
                        return temp
                    queue.append(temp)
        queen += 1
    return "No result!"

def BFS(n):
    start_time = time.time()
    print(BFS_Solution(n))
    end_time = time.time()
    runtime = end_time - start_time
    return runtime

n = int(input())
print("Time: ",BFS(n))

            