def isprime(x):
    d = 2
    while d * d <= x:
       if x % d == 0:
           return False
       d += 1
    return True
t = int(input())
for _ in range(t):
    n = int(input())
    m = 2
    while isprime(n + m):
        m += 1
    print(m)