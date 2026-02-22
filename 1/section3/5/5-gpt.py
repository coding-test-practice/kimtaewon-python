import sys
input = sys.stdin.readline

N, M = map(int, input().split())
data = list(map(int, input().split()))

# 수정 1: 슬라이딩 윈도우 방식
# lt rt 주고 왼쪽 줄이기 or 오른쪽 늘리기
# 고정 길이 슬라이딩 윈도우
# 가변 길이 슬라이딩 윈도우 (투포인터) => 지금 문제

cnt = 0
cur = 0
lt = 0
for rt in range(N):
    cur += data[rt]

    while cur > M:
        cur -= data[lt]
        lt += 1

    if cur == M:
        cnt += 1
        cur -= data[lt]
        lt += 1

# Todo: 결과 출력
print(cnt)