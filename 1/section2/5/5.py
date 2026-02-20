import sys
input = sys.stdin.readline

N, M = map(int, input().split())

# 1. 이중 for문으로 나올 수 있는 정수의 합을 전부 기록.
arr = []
for i in range(1, N+1):
    for j in range(1, M+1):
        arr.append(i + j)

# 2. 개수 세서 제일 많은 것들을 정답으로 출력.
cnt = {}
for x in arr:
    if x in cnt.keys():
        continue
        #Todo: x가 있으면 value에 더하고 x가 없으면 key로 새로 등록하고 싶은데 방법을 모르겠음
