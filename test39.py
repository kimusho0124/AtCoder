N = int(input())
cnt = 0
lenn = len(str(N))
for i in range(1, N+1):
    num = str(i)
    s = int(num[-1])
    e = int(num[0])
    if s != 0:
        if lenn == 1:
            cnt += 1
        elif lenn == 2:
            if s == e:
                cnt += 1
            if s * 10 + e <= N:
                cnt += 1
        else:
            if s == e:
                cnt += 1
            for k in range(2, lenn + 1):
                if k == lenn:
                    if s < int(str(N)[0]):
                        cnt += 10 ** (k-2)
                    elif s == int(str(N)[0]) and e <= int(str(N)[-1]):
                        cnt += int(str(N)[1:lenn-1]) + 1
                    elif s == int(str(N)[0]) and e > int(str(N)[-1]):
                        if int(str(N)[1:lenn-1]) >= 0:
                            cnt += int(str(N)[1:lenn-1])
                else:
                    cnt += 10 ** (k-2)
print(cnt)
