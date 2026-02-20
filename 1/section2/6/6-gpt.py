import sys
input = sys.stdin.readline

# 수정 1: digit_sum(x)를 빼먹음
def digit_sum(x):
    total = 0
    while x > 0:
        total += x % 10
        x //= 10
    return total

# 수정 2: 정수 입력
N = int(input())
data = list(map(int, input().split()))

max_value = 0
max_num = 0

for num in data:
    s = digit_sum(num)
    if s > max_value:
        max_value = s
        max_num = num

print(max_num)