# Todo: 스토쿠 입력받기
import sys
input = sys.stdin.readline

data= []
for _ in range(9):
    data.append(list(map(int, input().split())))

# Todo: 행 확인
ans = [1, 2, 3, 4, 5, 6, 7, 8, 9]
row_val = True
for i in range(9):
    temp = data[i]
    temp.sort()
    if temp != ans:
        row_val = False
        break

# Todo: 열 확인
col_val = True
for i in range(9):
    temp = [data[i][k] for k in range(9)]
    temp.sort()
    if temp != ans:
        col_val = False
        break

# Todo: 3x3 확인
sq_val = True
for i in range(9):
    temp = data[0][0:3] + data[1][0:3] + data[2][0:3]
    for i in range(3):
        for j in range(3):
            temp.append(data[i][j])

temp = data[0][0:3] + data[1][0:3] + data[2][0:3]
print(temp)
if temp != ans:
    sq_val = False

# Todo: 결과 출력
if all([row_val, col_val, sq_val]):
    print("YES")
else:
    print("NO")