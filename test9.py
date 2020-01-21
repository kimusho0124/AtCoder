N = int(input())
graph = [[] for i in range(N)]
basho = {}
for i in range(N-1):
    a, b = map(int, input().split())
    a, b = a-1, b-1
    graph[a].append(b)
    graph[b].append(a)
    sab = str(a) + '-' + str(b)
    sba = str(b) + '-' + str(a)
    basho[sab] = i
    basho[sba] = i
#print(basho)
#print(graph)
maxi = 0
root = -1
for i in range(N):
    leni = len(graph[i])
    maxi = max(leni, maxi)
    if maxi == leni:
        root = i

K = maxi
visited = [False for i in range(N)]
color = [0 for i in range(N)]
bashocolor = [0 for i in range(N-1)]
def bfs(v):
    Q = []
    visited[v] = True
    Q.append(v)
    while Q:
        v = Q.pop()
        clist = [i for i in range(1, K+1)]
        clist = list(set(clist) - set([color[v]]))
        now = 0
        for u in graph[v]:
            if not visited[u]:
                visited[u] = True
                color[u] = clist[now]
                now += 1
                nnn = str(v) + '-' + str(u)
                bashocolor[basho[nnn]] = color[u]
                Q.append(u)
bfs(root)
print(K)
for i in range(N-1):
    print(bashocolor[i])
