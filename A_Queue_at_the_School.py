l, t = map(int,input().split())
seq = list(input())
for i in range(t):
    j = 0
    while j < len(seq) - 1:
        if seq[j] == "B" and seq[j+1] == "G":
            temp = seq[j]
            seq[j] = seq[j+1]
            seq[j+1] = temp
            j += 2
        else:
            j += 1
print("".join(seq))
"""
BBGBG
BGBGB
GBGBB
"""