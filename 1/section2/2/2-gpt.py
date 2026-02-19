import sys
input = sys.stdin.readline

# 개선 1: 리스트보다는 케이스별로 다 출력
T = int(input())

for i in range(T):
    N, s, e, k = map(int, input().split())
    arr = list(map(int, input().split()))
    # 수정 1: 슬라이싱 때 범위 다시 생각하기
    arr = sorted(arr[s-1:e])
    print(f"#{i+1} {arr[k-1]}")