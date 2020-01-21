X = int(input())
if X >= 100:
    first = int(str(X)[:-2])

    last = int(str(X)[-2:])
    p = [0 for i in range(6)]
    for i in range(5,0,-1):
        p[i] = last // i
        last = last - p[i] * i
    sump = sum(p)
    if first >= sump:
        print(1)
    else:
        print(0)
else:
    print(0)