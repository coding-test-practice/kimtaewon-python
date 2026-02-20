import sys
input = sys.stdin.readline

N, M = map(int, input().split())

# 수정 1: arr 사용하지 말고 바로 합산
cnt = {}
for i in range(1, N+1):
    for j in range(1, M+1):
        s = i+j
        if s in cnt:
            cnt[s] += 1
        else:
            cnt[s] = 1

# Todo: 최댓값 찾기
max_cnt = max(cnt.values())

# Todo: 최댓값 가진 key들 출력
for key in sorted(cnt):
    if cnt[key] == max_cnt:
        print(key, sep=' ')