H, W = map(int, input().split())
S = [0 for j in range(H)]
for i in range(H):
    S[i] = list(str(input()))
TF = [[False for i in range(W)] for j in range(H)]
first = [0,0]
for j in range(H):
    for i in range(W):
        if S[j][i] == '#':
            TF[j][i] = True
        else:
            first = [j,i]
distance = [[0 for i in range(W)] for j in range(H)]
def bfs(s):
    Q = []
    TF[s[0]][s[1]] = True
    Q.append(s)
    while Q:
        v = Q.pop(0)
        next = [[v[0], v[1]+1], [v[0], v[1]-1],[v[0]+1, v[1]], [v[0]-1,v[1]]]
        for u in next:
            if u[0] >= 0 and u[0] <= H-1 and u[1] >= 0 and u[1] <= W-1:
                if TF[u[0]][u[1]] == False:
                    distance[u[0]][u[1]] = distance[v[0]][v[1]] + 1
                    TF[u[0]][u[1]] = True
                    Q.append(u)

maxd = 0
for k in range(H):
    for l in range(W):
        if S[k][l] == '.':
            first = [k,l]
            TF = [[False for i in range(W)] for j in range(H)]
            for j in range(H):
                for i in range(W):
                    if S[j][i] == '#':
                        TF[j][i] = True
            distance = [[0 for i in range(W)] for j in range(H)]
            bfs(first)
            #print(first)
            #print(distance)
            for j in range(H):
                for i in range(W):
                    maxd = max(maxd,distance[j][i])

print(maxd)
