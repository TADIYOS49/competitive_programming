a, b = map(int, input().split())
seq = [b]
while b > a:
    if b % 10 == 1:
        b = (b - 1) // 10
    elif b % 2 == 0:
        b //= 2
    else:
        break
    seq.append(b)
if b == a:
    print("YES")
    print(len(seq))
    print(*seq[::-1])
else:
    print("NO")
