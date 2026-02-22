import sys
input = sys.stdin.readline

N = int(input())
data = []
for _ in range(N):
    data.append(list(map(int, input().split())))

sum_data = []
for i in range(N):
    sum_data.append(sum(data[i]))

# 수정 1: 인덱스 오류 (원래 [i][j]로 되어 있었음)
for i in range(N):
    temp = 0
    for j in range(N):
        temp += data[j][i]
    sum_data.append(temp)

# 수정 2: 인덱스 오류 (원래 [-1-i][-1]로 되어 있었음)
d1 = 0
d2 = 0
for i in range(N):
    d1 += data[i][i]
    d2 += data[N-1-i][i]

sum_data.append(d1)
sum_data.append(d2)

# Todo: 결과 출력
print(max(sum_data))