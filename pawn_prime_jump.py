import math

def p_cells(n):
    cells = []
    is_prime = [True] * n
    is_prime[0] = False
    for i in range(2, n):
        if is_prime[i]:
            if (i % 10) == 3:
                cells.append(i)
            for j in range(i*i, n, i):
                is_prime[j] = False
    return (cells)


def maxGameScore(cell):

    n = len(cell)
    max_scores = [-math.inf] * n
    max_scores[0]= cell[0]
    possible_moves = p_cells(n)

    for i in range(1,n):
  #      print(i)
        if max_scores[i] < cell[i] + max_scores[i-1]:
            max_scores[i] = cell[i] + max_scores[i-1]
 #           print(max_scores)
        if possible_moves:
            for move in possible_moves:
                if move <= (n-i):
                    if max_scores[i-1+move] < cell[i-1+move] + max_scores[i-1]:
                        max_scores[i-1+move] = cell[i-1+move] + max_scores[i-1]
        #print(max_scores)

    return max_scores[-1]

# Example usage:
cells = [0, 1, 2, 3]
result = maxGameScore(cells)
print(result)  # output: 40