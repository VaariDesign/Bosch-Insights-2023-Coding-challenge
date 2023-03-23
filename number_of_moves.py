from queue import Queue

# Class for storing a Point's data
class Point:
    def __init__(self, x, y, dis):
        self.x = x
        self.y = y
        self.dis = dis

# Utility method returns true if (x, y) lies inside Board
def isInside(x, y, N):
    return 0 <= x < N and 0 <= y < N

def minMoves(n, startRow, startCol, endRow, endCol):
    dx = [-2, -1, 1, 2, -2, -1, 1, 2]
    dy = [-1, -2, -2, -1, 1, 2, 2, 1]
    minDistance = float('inf')
    queue = Queue()
    queue.put(Point(startRow, startCol, 0))

    visit = [[False] * n for _ in range(n)]
    visit[startRow][startCol] = True

    while not queue.empty():
        t = queue.get()

        if t.x == endRow and t.y == endCol:
            minDistance = t.dis
            break

        for i in range(8):
            x = t.x + dx[i]
            y = t.y + dy[i]

            # If reachable state is not yet visited and inside board, push that state into queue
            if isInside(x, y, n) and not visit[x][y]:
                visit[x][y] = True
                queue.put(Point(x, y, t.dis + 1))

    return minDistance if minDistance < float('inf') else -1