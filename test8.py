A, B, X = map(int, input().split())
lenx = len(str(X))
ans = 0
minx = min(lenx, 10)
for i in range(1, minx+1):
    if i != 10:
        nokori = X - B * i
        if nokori >=0:
            nnn = min(nokori // A, 10 ** i -1)
            #print(nnn)
            lennnn = len(str(nnn))
            if lennnn == i and nnn <= X and nnn <= 10 ** 9:
                ans = nnn
    elif i == 10:
        if A * 10 ** 9 + B * 10 <= X:
            ans = 10 ** 9
print(ans)
