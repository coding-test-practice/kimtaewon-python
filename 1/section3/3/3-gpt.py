import sys
input = sys.stdin.readline

# 개선 1: 배열 더 간단히 세팅
cards = list(range(21))

for _ in range(10):
    a, b = map(int, input().split())

    # 개선 2: 리스트 만드는 수 줄이기
    cards[a:b+1] = cards[a:b+1][::-1]

# Todo: 결과값 출력
print(*cards[1:])