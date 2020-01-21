N = int(input())
S = input()
keta = 10
count = 0
for i in range(keta):
    for j in range(keta):
        for k in range(keta):
            nnn = str(i) + str(j) + str(k)
            now = 0
            nownnn = nnn[now]
            flag = False
            for l in range(N):
                if S[l] == nownnn:
                    if now == 2:
                        flag = True
                        break
                    else:
                        now += 1
                        nownnn = nnn[now]
            if flag:
                count += 1
print(count)