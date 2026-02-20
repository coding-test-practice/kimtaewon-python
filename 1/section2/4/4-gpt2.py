import sys
input = sys.stdin.readline

N = int(input())
scores = list(map(int, input().split()))

avg = int(sum(scores)/N + 0.5)

best = 1
best_score = scores[0] # 수정 2: best_score 도입하기
temp = abs(avg-scores[0])

# 수정 1: 1부터 시작하기
for i, score in enumerate(scores, start=1):
    diff = abs(avg - score) # 개선 1: 반복 변수 단독으로 빼내기
    if diff < temp or (diff == temp and score > best_score):
        temp = diff
        best_score = score
        best = i

print(avg, best)