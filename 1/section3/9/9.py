# Todo: N, 봉우리 데이터 입력받기 (패딩 포함)
import sys
input = sys.stdin.readline

N = int(input())
data = []

data.append([0] * (N+2))
for _ in range(N):
    data.append([0] + list(map(int, input().split())) + [0])
data.append([0] * (N+2))

# Todo: 봉우리 개수 찾기
cnt = 0
for i in range(1, N+1):
    for j in range(1, N+1):
        if data[i][j] > data[i-1][j] and data[i][j] > data[i+1][j] and data[i][j] > data[i][j-1] and data[i][j] > data[i][j+1]:
            cnt += 1

# Todo: 결과 출력
print(cnt)