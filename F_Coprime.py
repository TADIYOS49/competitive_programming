def gcd(a,b):
    if b == 0:
        return a
    return gcd(b,a % b)
t = int(input())
for _ in range(t):
    leng = int(input())
    arr = list(map(int,input().split()))
    i = len(arr) - 1
    while i >= 1:
        a,b = 0,0
        if arr[i] >= arr[i-1]:
            a = arr[i-1]
            b = arr[i]
        else:
            a = arr[i]
            b = arr[i-1]
        if gcd(a,b) == 1:
            print(i+i-1)
            break
        i -= 1
    