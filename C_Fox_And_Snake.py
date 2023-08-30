n, m = map(int, input().split())
for i in range(n):
    if i % 4 == 0:
        print("#" * m)
    elif i % 2 == 1:
        if (i // 2) % 2 == 0:
            print("." * (m - 1) + "#")
            print("#" * m)
        else:
            print("#" + "." * (m - 1))
