import sys
input = sys.stdin.readline

# Todo: N 입력받기
N = int(input())

# Todo: 소수 찾기
# 방법: 2~N for문 (i에 대해 for문 돌려서 약수 개수 세기 -> 2면 cnt += 1)
cnt = 0
for i in range(2, N+1):
    prime = 0
    for j in range(2, i):
        if i % j == 0:
            prime += 1
    if prime == 0:
        cnt += 1

# Todo: 소수 개수 출력
print(cnt)