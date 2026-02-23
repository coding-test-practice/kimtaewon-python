# Todo: n, 2차원 배열 입력받기
import sys
input = sys.stdin.readline

n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]
data.sort(key=lambda x: (x[1], x[0]))

# Todo: 시간 안 겹치면서 최대한 회의 우겨넣기 => 그리디
ans = 0
last_end = 0

for s, e in data:
    if s >= last_end:
        ans += 1
        last_end = e

# Todo: 결과 출력
print(ans)