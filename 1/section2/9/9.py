# Todo: N 입력받기
import sys
input = sys.stdin.readline

N = int(input())

# Todo: 규칙 계산 함수 작성
def calc(data):
    if data[0] == data[1] == data[2]:
        return 10000 + data[0]*1000
    elif data[0] != data[1] and data[1] != data[2] and data[2] != data[0]:
        return max(data)*100
    else:
        if data[0] == data[1]:
            return 1000 + data[0]*100
        elif data[1] == data[2]:
            return 1000 + data[1]*100
        else:
            return 1000 + data[2]*100

# Todo: (주사위 눈 3개) * N 입력받기 -> 최댓값 여부 확인
max_price = 0
for i in range(N):
    price = calc(list(map(int, input().split())))
    if price > max_price:
        max_price = price


# Todo: 정답 출력
print(max_price)