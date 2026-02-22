# Todo: N, 배열 입력받기
import sys
input = sys.stdin.readline

N = int(input())
data = []
for _ in range(N):
    data.append(list(map(int, input().split())))

# Todo: M 입력받기
M = int(input())
# Todo: for문 돌리기 (M)
for i in range(M):
    # Todo: 회전명령 정보 입력받기
    rowNum, direction, move = map(int, input().split())
    # Todo: 정보만큼 이동하기
    if direction == 0:
        data[rowNum-1] = data[rowNum-1][move:] + data[rowNum-1][:move]
    else:
        data[rowNum-1] = data[rowNum-1][:move] + data[rowNum-1][move:]

# Todo: 감 개수 합산
lt = 0
rt = N-1
result = 0
for i in range(N):
    result = sum(data[i][lt:rt+1])
    if i < N//2:
        lt += 1
        rt -= 1
    else:
        lt -= 1
        rt +=1

# Todo: 결과 출력
print(result)