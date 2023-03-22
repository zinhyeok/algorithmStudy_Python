import sys
def ans():
    N = int(input())
    lst = []
    for i in range(N):
        lst.append(int(sys.stdin.readline().strip()))
    lst.sort()

    for i in range(len(lst)):
        print(lst[i])

ans()