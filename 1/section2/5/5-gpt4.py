import sys
input = sys.stdin.readline

N, M = map(int, input().split())

cnt = {}
for i in range(1, N+1):
    for j in range(1, M+1):
        s = i+j
        cnt[s] = cnt.get(s, 0) + 1 # 개선 1: 카운트 부분을 더 간단히 하기
        # cnt.get(s): s의 value 반환
        # cnt.get(s, 0): s의 value 반환, 단 s라는 key가 존재하지 않으면 0 반환

max_cnt = max(cnt.values())

# 수정 1: 리스트로 모아서 출력
# *list: 대괄호 풀고 내용물만 공백으로 출력하겠다는 뜻
result = [key for key in sorted(cnt) if cnt[key] == max_cnt]
print(*result)