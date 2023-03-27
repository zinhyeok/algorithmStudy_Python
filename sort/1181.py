import sys


def ans():
    N = int(input())
    lst = []
    for _ in range(N):
        lst.append(str(sys.stdin.readline().strip()))
    se = set(lst)
    lst = list(se)
    lst.sort(key= lambda x: (len(x), x))
    for i in lst:
        print(i)

ans()