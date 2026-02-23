import sys
input = sys.stdin.readline

data = [list(map(int, input().split())) for _ in range(7)]

cnt = 0
# 수정 1: 가로 (로직 더 간단히)
for i in range(7):
    for j in range(3):
        temp = data[i][j:j+5]
        if temp == temp[::-1]:
            cnt += 1

# 수정 2: 세로
for i in range(7):
    for j in range(3):
        temp = [data[j + k][i] for k in range(5)]
        if temp == temp[::-1]:
            cnt += 1

print(cnt)