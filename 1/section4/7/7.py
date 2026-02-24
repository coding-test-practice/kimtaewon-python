DEBUG = True
def debug(message):
    if DEBUG:
        print("[DEBUG]", message)

'''
10
69  42  68  76  40  87  14  65  76  81
50
'''

# Todo: L, 자연수(L개), M 입력 받기
import sys
input = sys.stdin.readline

L = int(input())
l_list = list(map(int, input().split()))
M = int(input())

debug(f"L={L}, l_list={l_list}, M={M}")

# Todo: 가장 높은 곳 +1, 가장 낮은 곳 -1
# 브루트 포스: 매번 max min 찾아서 조정하기
# 5 3 9 7 2 8 5
#


# Todo:
# Todo: 결과 (최상단 - 최하단) 출력