import math
N = int(input())
x = [0 for i in range(N)]
y = [0 for j in range(N)]
for i in range(N):
    x[i], y[i] = map(int, input().split())
for i in range(N):
    for j in range(i+1,N):
        x1, y1 = x[i], y[i]
        x2, y2 = x[j], y[j]
        xc, yc = (x1 + x2) /2, (y1+y2)/2
        r2 = ((x1-x2)**2 + (y1-y2)**2) / 4
        print(i,j,r2)
        flag = True

        for k in range(N):
            xk, yk = x[k], y[k]
            now = (xk-xc) ** 2 + (yk - yc) ** 2
            if now > r2:
                flag = False
                break
        if flag:
            print(math.sqrt(r2))
            break
    else:
        continue
    break
