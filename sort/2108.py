import sys
from collections import Counter

def ans():
    N = int(input())
    lst = []
    for _ in range(N):
        lst.append(int(sys.stdin.readline().strip()))
    lst.sort()
    avg = round(sum(lst)/N)
    # int() round()차이란?
    mid = lst[(N//2)]
    common_lst = Counter(lst).most_common(2)
    common = common_lst[0][0]
    try:
        if common_lst[0][1] == common_lst[1][1]:
            common = common_lst[1][0]
    except():
        pass
    range_lst = lst[-1]-lst[0]
    print(avg)
    print(mid)
    print(common)
    print(range_lst)

ans()