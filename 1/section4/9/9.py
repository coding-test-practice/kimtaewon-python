import sys
input = sys.stdin.readline

N = int(input())
n_list = list(map(int, input().split()))

message = ''
lt, rt = (0, N-1)
last = 0
while lt <= rt:
    if lt == 0 and rt == N - 1:
        if n_list[lt] < n_list[rt]:
            last = n_list[0]
            lt += 1
            message += 'L'
        elif n_list[lt] >= n_list[rt]:
            last = n_list[N-1]
            rt -= 1
            message += 'R'
    if n_list[lt] > n_list[rt]:
        if n_list[lt] > last:
            last = n_list[lt]
            lt += 1
            message += 'L'
        else:
            break
    elif n_list[lt] <= n_list[rt]:
        if n_list[rt] > last:
            last = n_list[rt]
            rt -= 1
            message += 'R'
        else:
            break

print(f"{len(message)}\n{message}")