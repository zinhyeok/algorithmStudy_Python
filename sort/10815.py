def ans():
    N = int(input())
    N_card = set(list(map(int, input().split())))
    M = int(input())
    M_card = list(map(int, input().split()))

    for i in range(M):
        if M_card[i] in N_card:
            M_card[i] = 1
        else:
            M_card[i] = 0
    for i in range(M):
        print(M_card[i], end=" ")

ans()