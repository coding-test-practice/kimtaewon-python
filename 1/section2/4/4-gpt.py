import sys
input = sys.stdin.readline

N = int(input())
scores = list(map(int, input().split()))

# 수정 1: 사사오입
avg = int(sum(scores)/N+0.5)

best = -1
temp = 1000000

# 수정 2: enumerate 사용; 인덱스, 값 동시에 꺼내기
for i, score in enumerate(scores):
    if abs(avg - score) < temp:
        temp = abs(avg - score)
        print("yes")
        best = i

print(avg, best)