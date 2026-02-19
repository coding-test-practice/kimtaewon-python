n, k = map(int, input().split())

fact = []
for i in range (1, n+1):
    if n%i==0:
        fact.append(i)

if k<=len(fact):
    print(fact[k-1])
else:
    print(-1)