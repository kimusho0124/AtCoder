N = int(input())
A = list(map(int, input().split()))
try:
    flag = False
    now = A[0]
    for i in range(N):
        if A[i] != now:
            flag = True
            break
    if flag:
        B = [1 for i in range(N)]
        amari = [i for i in range(2, N + 1)]
        for i in range(N-1):
            k = B[i]
            if A[k-1] == amari[0]:
                now = amari.pop(1)
            else:
                now = amari.pop(0)
            B[i+1] = now
        print(*B)
    else:
        B = [now for i in range(N)]
        amari = [i for i in range(1, N + 1) if i != now ]
        for i in range(N - 1):
            k = B[i]
            if A[k - 1] == amari[0]:
                now = amari.pop(1)
            else:
                now = amari.pop(0)
            B[i + 1] = now
        print(*B)

except:
    print(-1)
