import heapq
t = int(input())
for _ in range(t):
    n = int(input())
    arr = map(int,input().split())
    heapq.heapify(arr)
    while 