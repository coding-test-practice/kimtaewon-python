# Todo: N, 2차원 배열 입력받기
import sys
input = sys.stdin.readline

N = int(input())
data = []
for _ in range(N):
    data.append(list(map(int, input().split())))

# Todo: 행 합 계산
sum_data = []
for i in range(N):
    sum_data.append(sum(data[i]))

# Todo: 열 합 계산
for i in range(N):
    temp = 0
    for j in range(N):
        temp += data[j][i]
    sum_data.append(temp)

# Todo: 대각선 합 계산
d1 = 0
d2 = 0
for i in range(N):
    d1 += data[i][i]
    d2 += data[-1-i][-1-i]

sum_data.append(d1)
sum_data.append(d2)

# Todo: 결과 출력
print(max(sum_data))