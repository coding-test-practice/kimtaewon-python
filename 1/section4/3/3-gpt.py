import sys
input = sys.stdin.readline

N, M = map(int, input().split())
songList = list(map(int, input().split()))

# 수정 1: 그리디 알고리즘 (최대한 우겨넣기)
def needed_dvds(cap):
    dvd_count = 1
    current = 0
    for t in songList:
        if current + t <= cap:
            current += t
        else:
            dvd_count += 1
            current = t
    return dvd_count

lt = max(songList)
rt = sum(songList)
ans = rt

# 수정 2: 이분 탐색
while lt < rt:
    mid = (lt + rt) // 2
    if needed_dvds(mid) <= M:
        ans = mid
        rt = mid - 1
    else:
        lt = mid + 1



# Todo: 결과 출력
print(ans)