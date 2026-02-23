import sys
input = sys.stdin.readline

# ==== 전체 컨셉: set 사용 ====

# 개선 1: 데이터 입력 한줄로
data = [list(map(int, input().split())) for _ in range(9)]
need = set(range(1, 10))

# 수정 1: 행 검사
for i in range(9):
    if set(data[i]) != need:
        print("NO")
        sys.exit(0)

# 수정 2: 열 검사
for j in range(9):
    temp = [data[i][j] for i in range(9)]
    if set(temp) != need:
        print("NO")
        sys.exit(0)

# 수정 3: 3x3 검사
for si in range(0, 9, 3):
    for sj in range(0, 9, 3):
        block = []
        for i in range(si, si+3):
            for j in range(sj, sj+3):
                block.append(data[i][j])
        if set(block) != need:
            print("NO")
            sys.exit(0)


print("YES")