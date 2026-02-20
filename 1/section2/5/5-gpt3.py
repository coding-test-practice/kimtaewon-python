import sys
input = sys.stdin.readline

N, M = map(int, input().split())

cnt = {}
for i in range(1, N+1):
    for j in range(1, M+1):
        s = i+j
        if s in cnt:
            cnt[s] += 1
        else:
            cnt[s] = 1

max_cnt = max(cnt.values())

# 수정 1: 리스트로 모아서 출력
# *list: 대괄호 풀고 내용물만 공백으로 출력하겠다는 뜻
result = [key for key in sorted(cnt) if cnt[key] == max_cnt]
print(*result)