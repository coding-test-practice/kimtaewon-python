# Todo: N, 채점 결과 * N 입력 받기
import sys
input = sys.stdin.readline

N = int(input())
ox = list(map(int, input().split()))

# Todo: 점수 계산 함수
def calc(data):
    score = 0
    # Todo: 연속 콤보 있음
    combo = False
    cnt = 0
    for d in data:
        if d == 1:
            if combo:
                score += 1 + cnt
            else:
                score += 1
            combo = True
            cnt += 1
        else:
            combo = False
            cnt = 0
    return score

# Todo: 총 점수 출력
print(calc(ox))