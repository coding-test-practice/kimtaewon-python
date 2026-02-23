import sys
input = sys.stdin.readline

N = int(input())
ox = list(map(int, input().split()))

def calc(data):
    score = 0
    cnt = 0
    # 개선 1: 조건 더 간단하게 (combo는 필요없음)
    for d in data:
        if d == 1:
            cnt += 1
            score += cnt
        else:
            cnt = 0
    return score

print(calc(ox))