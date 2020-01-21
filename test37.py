a, b = map(int, input().split())
if a <= b:
    s = str(a) * b
else:
    s = str(b) * a
print(s)