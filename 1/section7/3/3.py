N = int(input())
traversal = []

# 1~N 부분집합 출력 프로그램
# 전위순회 출력

def DFS(v):
    global N
    if v > N:
        return
    else:
        traversal.append(v)
        DFS(2*v)
        DFS(2*v+1)

DFS(1)


answer = []

def DFS2(list):
    if not list:
        return
    else:
        # 본연의 일: 출력
        answer.append(list)
        # 원소 하나씩 빼고 재귀 호출
        for x in list:
            temp = list.copy()
            temp.remove(x)
            DFS2(temp)

DFS2(traversal)

answer2 = []
for x in answer:
    if x not in answer2:
        answer2.append(x)

for x in answer2:
    print(*x)