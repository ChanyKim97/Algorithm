M, N = map(int, input().split())

board = []
for i in range(M):
    board.append(input())

list_ = []
for i in range(M-7):
    for j in range(N-7):
        cnt1 =0
        cnt2 =0
        for k in range(i, i+8):
            for l in range(j, j+8):
                if (k+l)%2 == 0:
                    if board[k][l] != 'W':
                        cnt1 += 1
                    if board[k][l] != 'B':
                        cnt2 += 1
                else:
                    if board[k][l] != 'B':
                        cnt1 += 1
                    if board[k][l] != 'W':
                        cnt2 += 1

        list_.append(min(cnt1, cnt2))

print(min(list_))