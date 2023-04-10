def solve(n,arr):
    arr.sort()
    l, r = 0 , len(arr)-1
    area = [arr[r]*arr[l]]
    count = 0
    while l+1<=r-1:
        temp = 0
        if arr[r] == arr[r-1] and arr[l] == arr[l+1]:
            temp = arr[r] * arr[l]
        if area[-1] == temp:
            count += 1
        if count == n:
            return "YES"
        l += 2
        r -= 2
    return "NO"
query = int(input())
for _ in range(query):
    n = int(input())
    arr = list(map(int,input().split()))
    print(solve(n,arr))