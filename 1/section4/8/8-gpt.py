# Todo: N, M // w(N개) 입력 받기
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

weights = list(map(int, input().split()))
weights.sort()

# Todo: 구명보트 개수 극소화 필요
# M/2 될 때까지 무거운 사람 먼저 태우고, 남은 사람들 찡겨앉게 하기

lt, rt = 0, N-1
ans = 0

while lt <= rt:
    ans += 1
    if weights[lt] + weights[rt] <= M:
        lt += 1
    rt -= 1

print(ans)