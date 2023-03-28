import sys

def ans():
    N = int(input())
    lst = list(map(int, sys.stdin.readline().strip().split()))
    sort_lst = sorted(set(lst))
    # 2 4 -10 4 -9 -> -2 2 3 4 7
    # compress_lst = [sort_lst.index(i) for i in lst]
    compress_lst = {sort_lst[i]: i for i in range(len(sort_lst))}
    print(compress_lst)
    for i in lst:
        print(compress_lst.get(i), end=" ")


ans()