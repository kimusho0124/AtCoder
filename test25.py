N = int(input())
C = list(map(int, input().split()))
C.sort(reverse = True)
#print(C)
sosu = 10 ** 9 + 7
K = dict()
K[-1] = 1
K[0] = 1
for i in range(1, N+1):
    a = K[i-1] * 2 % sosu
    K[i] = a
ans = 0
for i in range(N):
    #for j in range(1,circle):##j番目に大きい
    #    kkk = c(i, j-1) * 2 ** (N-i-1)###i+1番目に大きいものがj番目に大きくなるような選び方
    #    ans += C[i] * kake * j * kkk
    ans += (C[i] * K[N] * (K[i] + i * K[i-1]) * K[N-i-1]) % sosu
    ans %= sosu
print(int(ans))





