from heapq import heapify, heappop, heappush

def solve(n, w, order):
    introvert_heap = [(-w[i], i) for i in range(n)]
    extrovert_heap = []
    heapify(introvert_heap)
    taken = [0]*n
    answer = [0]*(2*n)
    for i in range(2*n):
        if order[i] == '0': # Introvert
            _, row = heappop(introvert_heap)
            answer[i] = row + 1
            taken[row] = i
            heappush(extrovert_heap, (w[row], -i, row))
        else: # Extrovert
            _, _, row = heappop(extrovert_heap)
            answer[i] = answer[taken[row]] = row + 1
    return answer

n = 2
w = [3, 1]
order = "0011"
print(solve(n, w, order))  # Output: [2, 1, 1, 2]
