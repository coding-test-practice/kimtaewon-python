import sys
input = sys.stdin.readline

N, M = map(int, input().split())

arr = []
for i in range(1, N+1):
    for j in range(1, M+1):
        arr.append(i + j)

# 수정 1: 딕셔너리 사용
# dict[x] = @ 하면 키 자동 등록됨. 값도 업데이트 가능.
# 어렵게 생각 X
cnt = {}
for x in arr:
    if x in cnt:
        cnt[x] += 1
    else:
        cnt[x] = 1


