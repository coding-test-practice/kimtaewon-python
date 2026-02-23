# Todo: N, M // songList 입력 받기
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
songList = list(map(int, input().split()))

# Todo: 결정 알고리즘
#  ans = 최소 용량 크기
#  문제: ans의 용량을 가진 M개의 DVD에 N개의 곡이 다 들어가는가?
#  알고리즘: N개의 곡이 M개 이하일 때 다 들어가면 됨
#   1. 합이 ans 이하가 되도록 그룹핑
#   2. 그룹 개수가 N개 이하 -> 용량 충분. 용량 줄이기
#   3. 그룹 개수가 N개 초과 -> 용량 부족. 용량 늘리기
ans = max(songList)
start = 0
end = 0
cnt = 0

# ans = 10
while True:
    while end < N: # end < 9
        temp = sum(songList[start:end+1])# 1+2+3+4 = 10
        print(f"[before] temp: {temp} ans: {ans} cnt: {cnt} start: {start} end: {end}")
        if temp < ans:
            end += 1
        else:
            cnt += 1
            start = end
            if end == N - 1:
                break
    if cnt <= M:
        ans += 1
    else:
        ans -= 1




# Todo: 결과 출력
print(ans)