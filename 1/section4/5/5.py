# Todo: n, 2차원 배열 입력받기
import sys
input = sys.stdin.readline

n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]
data.sort()
print(data)

# Todo: 시간 안 겹치면서 최대한 회의 우겨넣기 => 그리디
# 극대화하고 싶은 값: 개최된 회의 수 mt
# 문제 정의: mt가 d개를 넘을 수 있다?
start = data[0][0]
end = data[n-1][1]
ans = 0
curr = start

while curr <= end:
    continue


# Todo: 결과 출력
print(f"start={start} end={end} ans={ans}")