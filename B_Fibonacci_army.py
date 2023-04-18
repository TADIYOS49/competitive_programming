n = int(input())
def solve(n):
    if n == 1:
        return 1
    if n == 0:
        return 1
    return solve(n-1)+solve(n-2)
print(solve(n))