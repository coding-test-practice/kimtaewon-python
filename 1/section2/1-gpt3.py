import sys
input = sys.stdin.readline
n, k = map(int, input().split())

forward = []
backward = []

i = 1
while i * i <= n: # 마이너 개선: 띄어쓰기 맞추기
    if n % i == 0:
        forward.append(i)
        if n // i != i:
            backward.append(n//i)
    i += 1 # 마이너 개선: i = i + 1 대신 이렇게 쓸 수 있음

answer = forward + backward[::-1]

# 개선 1: print 함수 내 if문 활용
print(answer[k-1] if k <= len(answer) else -1)