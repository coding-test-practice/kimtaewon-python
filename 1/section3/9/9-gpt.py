import sys
input = sys.stdin.readline

N = int(input())
data = []

data.append([0] * (N+2))
for _ in range(N):
    data.append([0] + list(map(int, input().split())) + [0])
data.append([0] * (N+2))

# 개선: and보다 dx, dy 활용
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

cnt = 0
for i in range(1, N+1):
    for j in range(1, N+1):
        if all(data[i][j] > data[i+dx[k]][j+dy[k]] for k in range(4)):
            cnt += 1

print(cnt)