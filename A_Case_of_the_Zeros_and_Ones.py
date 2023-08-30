def minimum_length(n, s):
    stack = []

    for i in range(n):
        if len(stack) > 0 and stack[-1] != s[i]:
            stack.pop()
        else:
            stack.append(s[i])

    return len(stack)

# Read input
n = int(input())
s = input()

# Call the function and print the result
result = minimum_length(n, s)
print(result)
