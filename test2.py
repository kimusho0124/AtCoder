N = int(input())
S = input()
amari = N % 2
sho = N // 2
flag = False
if amari == 0:
    if S[:sho] == S[sho:]:
        flag = True
if flag:
    print('Yes')
else:
    print('No')