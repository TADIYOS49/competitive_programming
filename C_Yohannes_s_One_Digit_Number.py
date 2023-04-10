import sys, threading

input = lambda: sys.stdin.readline().strip()

def solve(n,count):
    if len(n) == 1:
        return count
    temp = 0
    for i in n:
        temp += int(i)
    count += 1
    return solve(str(temp),count)
def main():
    num = input()
    ans = solve(str(num),0)
    print(ans)


if __name__ == '__main__':
    
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()