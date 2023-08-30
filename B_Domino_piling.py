def max_dominoes(M, N):
    # Calculate the area of the board and a single domino
    board_area = M * N
    domino_area = 2 * 1

    # Calculate the maximum number of dominoes that can be placed
    max_dominoes_count = board_area // domino_area

    return max_dominoes_count

# Read input values
M, N = map(int, input().split())

# Call the function and print the result
print(max_dominoes(M, N))
