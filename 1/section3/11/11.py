# Todo: 7*7 입력받기
import sys
input = sys.stdin.readline

data = [list(map(int, input().split())) for _ in range(7)]

# Todo: 7번 * 3번 왔다갔다 하면서 회문수 찾기 (가로)
cnt = 0
for i in range(7):
    for j in range(3):
        temp = data[i][j:j+5]
        if temp[0:2] == temp[3:5][::-1]:
            cnt += 1

# Todo: 3번 * 7번 왔다갔다 하면서 회문수 찾기 (세로)
for i in range(7):
    temp = []
    for j in range(3):
        temp.append(data[j][i])
        if temp[0:2] == temp[3:5][::-1]:
            cnt += 1

# Todo: 개수 출력
print(cnt)