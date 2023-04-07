import sys
from itertools import combinations

dwarf_lst = []
sum_dwarf_height = 100

for _ in range(9):
    dwarf_lst.append(int(sys.stdin.readline().strip()))

possible_seven_lst = list(combinations(dwarf_lst, 7))

for seven_dwarf in possible_seven_lst:
    if sum(seven_dwarf) == sum_dwarf_height:
        for dwarf in sorted(seven_dwarf):
            print(dwarf)
        break


# 조합 만들기 함수
def combination(lst, r):
    wanted = []
    if r == 1:
        for i in lst:
            wanted.append([i])
    else:
        for i in range(len(lst)-r+1):
            for j in combination(lst[i+1:], r-1):
                wanted.append([lst[i]]+j)
    return wanted