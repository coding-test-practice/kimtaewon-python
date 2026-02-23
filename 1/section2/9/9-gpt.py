import sys
input = sys.stdin.readline

N = int(input())

# 개선 1: 정렬 후 계산
def calc(data):
    data.sort()
    a, b, c = data
    print(a, b, c)
    if a == c:
        return 10000 + a*1000
    elif a == b or b == c:
        return 1000 + b*100
    else:
        return c*100

# 개선 2: max_price 기본값 -1
max_price = -1
for i in range(N):
    price = calc(list(map(int, input().split())))
    if price > max_price:
        max_price = price


# Todo: 정답 출력
print(max_price)