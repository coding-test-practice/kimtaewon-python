DEBUG = False
def debug(message: str):
    if DEBUG:
        print("[DEBUG]", message)

'''
5
172  67
183  65
180  70
170  72
181  60
'''

# Todo: N, 키+몸무게 정보 입력 받기
import sys
input = sys.stdin.readline

N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]
data.sort(reverse=True)

# Todo: 완벽한 상위호환이 있으면 안됨.
# 그냥 제일 무거운 사람 뽑으면 됨

cnt = 1
standard = data[0][1]

for i in range(1, N):
    if data[i][1] > standard:
        debug(f"{data[i]} selected")
        cnt += 1
        standard = data[i][1]


# Todo: 결과(최대 인원) 출력
print(cnt)
