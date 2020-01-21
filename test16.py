T1, T2 = map(int, input().split())
A1, A2 = map(int, input().split())
B1, B2 = map(int, input().split())
firsttaka = T1 * A1
firstao = T1 * B1
sumtaka = T1 * A1 + T2 * A2
sumao = T1 * B1 + T2 * B2
if sumtaka == sumao:
    print('infinity')
elif firsttaka > firstao and sumtaka > sumao:
    print(0)
elif firsttaka < firstao and sumtaka < sumao:
    print(0)
else:
    sumabs = abs(sumtaka - sumao)
    firstabs = abs(firsttaka - firstao)
    ans = (firstabs // sumabs) * 2
    amari = firstabs % sumabs
    if amari > 0:
        ans += 1
    print(ans)