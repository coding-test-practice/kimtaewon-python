import sys
input = sys.stdin.readline

N = int(input())
a = list(map(int, input().split()))

lt, rt = 0, N - 1
last = 0
res = []

while lt <= rt:
    candidates = []
    if a[lt] > last:
        candidates.append((a[lt], 'L'))
    if a[rt] > last:
        candidates.append((a[rt], 'R'))

    if not candidates:
        break

    # 후보가 2개면 더 작은 값을 고르는 게 유리
    candidates.sort()  # (값, 방향) 기준 정렬
    if len(candidates) == 1:
        val, dirc = candidates[0]
    else:
        # 값이 같으면 "미래에 몇 개 더 뽑을 수 있는지" 비교
        if candidates[0][0] == candidates[1][0]:
            ltmp, rtmp = lt, rt
            cur = last

            cntL = 0
            while ltmp <= rt and a[ltmp] > cur:
                cur = a[ltmp]
                cntL += 1
                ltmp += 1

            cur = last
            cntR = 0
            while lt <= rtmp and a[rtmp] > cur:
                cur = a[rtmp]
                cntR += 1
                rtmp -= 1

            if cntL >= cntR:
                val, dirc = candidates[0][0], 'L'
            else:
                val, dirc = candidates[0][0], 'R'
        else:
            val, dirc = candidates[0]  # 더 작은 값 선택

    res.append(dirc)
    last = val
    if dirc == 'L':
        lt += 1
    else:
        rt -= 1

print(len(res))
print(''.join(res))
