# Todo: N, 원소 * N, M, 원소 * M 각 줄에 입력받기
import sys
input = sys.stdin.readline

N = int(input())
n_list = list(map(int, input().split()))

M = int(input())
m_list = list(map(int, input().split()))

# Todo: 오름차순 합치기 -> 결과 출력
result = n_list + m_list
result.sort()
print(*result)
