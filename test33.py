N = int(input())
X = []
for i in range(N):
    x, l = map(int, input().split())
    s, e = x-l, x+l
    X.append((s, e))
X.sort(key=lambda x: x[1])
#print(X)
c1 = 1
n1 = X[0][1]
for i in range(1,N):
    if X[i][0] >= n1:
        c1 += 1
        n1 = X[i][1]
c2 = 0
n2 = X[0][0]
for i in range(1,N):
    if X[i][0] >= n2:
        c2 += 1
        n2 = X[i][1]
print(max(c1, c2))


