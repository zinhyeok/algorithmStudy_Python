from itertools import permutations

N = int(input())
oneToNine = [1,2,3,4,5,6,7,8,9]
ans_lst = list(permutations(oneToNine, 3))
#strike인 경우 123 1 -> 198 921 893 등등
def strike(num_lst, n):
    num_lst = [i in list(num_lst)]
    permutations(oneToNine.remove(), 3-n)

for i in range(N):

