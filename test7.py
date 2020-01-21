N = int(input())
S = input()
alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lens = len(S)
ans = ''
for i in range(lens):
    ind = alpha.index(S[i])
    next = ind + N
    if next >= 26:
        next -= 26
    ans += alpha[next]
print(ans)
