# Todo: 입력 세팅
import sys
input = sys.stdin.readline

# Todo: 배열 세팅
cards = []
for i in range(21):
    cards.append(i)

# Todo: for문 10번 돌리기
for i in range(10):
    a, b = map(int, input().split())

    # Todo: 역순 배열
    cards = cards[:a] + cards[a:b+1][::-1] + cards[b+1:]

    print(f"sort: {cards}")

# Todo: 결과값 출력
print(*cards[1:])