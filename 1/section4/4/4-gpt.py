import sys
input = sys.stdin.readline

# 수정 1: 입력 수정
N, C = map(int, input().split())
xi = [int(input()) for _ in range (N)]
xi.sort()

# 두 말의 최소 거리 d
# 문제 정의: d가 최소 거리가 되나?
# 문제 정의하는 법
# 최대 길이, 최소 용량, 등등 숫자 하나를 극단값으로 만들고 싶어하는 문제 -> 90% 결정 알고리즘
# "가장 가까운 두 말의 거리가 최대" => 말의 최소 거리 d를 극단값으로 만들고 싶어함
# 이 d를 바로 구할 수는 없음.
# 이분탐색을 활용해서, "이 d값이면 문제 요건을 충족하는가?" 를 확인해야 함
# YES -> NO가 한번만 변하도록 잡아야 함 (Y Y Y Y N N N)


# 말 놓는 방식: 그리디.
def can_place(d):
    count = 1
    last = xi[0]

    for i in range(1, N):
        if xi[i] - last >= d:
            count += 1
            last = xi[i]
            if count >= C:
                return True
    return False

lt = 1
rt = xi[-1] - xi[0]
ans = 0

while lt <= rt:
    mid = (lt + rt) // 2
    if can_place(mid):
        ans = mid
        lt = mid + 1
    else:
        rt = mid -1

print(ans)