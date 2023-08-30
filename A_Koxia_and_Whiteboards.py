import heapq
t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    j = 0
    heapq.heapify(a)
    while j < m:
        heapq.heappop(a)
        heapq.heappush(a,b[j])
        j += 1
    print(sum(a))
