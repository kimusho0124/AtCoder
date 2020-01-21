N, K = map(int, input().split())
R, S, P = map(int, input().split())
T = input()
janken = ['' for i in range(K)]
for i in range(N):
    amari = i % K
    janken[amari] = janken[amari] + T[i]
#print(janken)
count = 0
for i in range(K):
    lenN = len(janken[i])
    now = 1
    jan = janken[i][0]
    for j in range(1,lenN):
        if janken[i][j-1] == janken[i][j]:
            now += 1
        elif janken[i][j-1] != janken[i][j]:
            sho = (now + 1) // 2
            if jan == 'r':
                count += sho * P
            elif jan == 's':
                count += sho * R
            elif jan == 'p':
                count += sho * S
            now = 1
            jan = janken[i][j]
    sho = (now + 1) // 2
    if jan == 'r':
        count += sho * P
    elif jan == 's':
        count += sho * R
    elif jan == 'p':
        count += sho * S
print(count)