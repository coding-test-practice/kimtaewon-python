import sys
input = sys.stdin.readline

N = int(input())
data = []
for _ in range(N):
    data.append(list(map(int, input().split())))

# 수정: 리스트 없는 버전

max_sum = -1
d1 = 0
d2 = 0

for i in range(N):
    row_sum = 0
    col_sum = 0
    for j in range(N):
        row_sum += data[i][j]
        col_sum += data[j][i]

    max_sum = max(max_sum, row_sum, col_sum)

    d1 += data[i][i]
    d2 += data[i][N-1-i]

print(max(max_sum, d1, d2))