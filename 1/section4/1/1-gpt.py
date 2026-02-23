import sys
input = sys.stdin.readline

N, M = map(int, input().split())
data = list(map(int, input().split()))

data.sort()

# 개념: 이분 검색
# 중간값 찾기
# 내가 찾는 값 M이 더 크면 오른쪽, 더 작으면 왼쪽

lt = 0
rt = N-1
ans = -1

while lt <= rt:
    mid = (lt + rt) // 2
    if data[mid] == M:
        ans = mid + 1
        break
    elif data[mid] < M:
        lt = mid + 1
    else:
        rt = mid - 1

# Todo: 결과 출력
print(ans)