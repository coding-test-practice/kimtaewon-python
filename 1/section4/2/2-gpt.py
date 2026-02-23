import sys
input = sys.stdin.readline

K, N = map(int, input().split())

lan_list = [int(input()) for _ in range (K)]

# ==== 개념: 결정 알고리즘 ====
# 어떤 값 X의 가능 여부만 빠르게 판정 후, 이분 탐색으로 좁혀서 정답 찾음
# 정답 형태: 최댓값/최솟값
# X, 결정 문제 정의 => 이분 탐색

# 길이: L
# 문제 정의: 길이 L로 잘라서 N개 이상 만들 수 있는가?

lt = 1
rt = max(lan_list)
ans = 0

while lt <= rt:
    mid = (lt + rt) // 2
    cnt = 0
    for lan in lan_list:
        cnt += lan // mid
    if cnt >= N:
        ans = mid
        lt = mid + 1
    elif cnt < N:
        rt = mid - 1

print(ans)

