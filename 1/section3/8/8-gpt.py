# Todo: N, 배열 입력받기
import sys
input = sys.stdin.readline

N = int(input())
# 개선 1: 2차원 배열 입력받기 한 줄로
data = [list(map(int, input().split())) for _ in range(N)]

M = int(input())
for i in range(M):
    rowNum, direction, move = map(int, input().split())
    # 수정 1: 슬라이싱 범위 처리
    move %= N
    if move == 0:
        continue

    # 수정 2: right 부분 데이터 수정
    if direction == 0:
        # 12 39 30 23 11 => 2만큼 이동
        # 30 23 11 // 12 39
        # move: + :move
        data[rowNum-1] = data[rowNum-1][move:] + data[rowNum-1][:move]
    else:
        # 12 39 30 23 11 => 2만큼 이동
        # 23 11 // 12 39 30
        # -move: + :-move
        data[rowNum-1] = data[rowNum-1][-move:] + data[rowNum-1][:-move]

lt = 0
rt = N-1
result = 0
for i in range(N):
    # 수정 3: +=가 아니라 = 로 되어 있었음
    result += sum(data[i][lt:rt+1])
    if i < N//2:
        lt += 1
        rt -= 1
    else:
        lt -= 1
        rt +=1

print(result)