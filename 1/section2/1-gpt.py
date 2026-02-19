# 개선 1: sys.stdin.readline으로 속도 높이기
import sys

n, k = map(int, sys.stdin.readline().split())

fact = []
i = 1

# 개선 2: n**(1/2)까지만 루프문 돌리기
while i*i <= n:
    if n%i==0:
        fact.append(i)
    i = i + 1

for j in range (len(fact)):
    a = n//fact[-1+j]
    if a in fact:
        continue
    else:
        fact.append(n//fact[-1+j])

if k<=len(fact):
    print(fact[k-1])
else:
    print(-1)