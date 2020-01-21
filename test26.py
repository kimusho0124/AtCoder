N = int(input())
s = ['' for i in range(N)]
t = [0 for i in range(N)]

for i in range(N):
    ss, tt = input().split()
    s[i] = ss
    t[i] = int(tt)
X = input()
flag = False
ans = 0
for i in range(N):
    if flag:
        ans += t[i]
    else:
        if X == s[i]:
            flag = True
print(ans)
