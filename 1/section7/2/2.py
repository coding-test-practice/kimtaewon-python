# 전위 순회
def DFS1(n):
    if n > 7:
        return
    else:
        print(n, end=' ')
        DFS1(2*n)
        DFS1(2*n+1)

DFS1(1)
print()

# 중위 순회
def DFS2(n):
    if n > 7:
        return
    else:
        DFS2(2*n)
        print(n, end=' ')
        DFS2(2*n+1)

DFS2(1)
print()

# 후위 순회
def DFS3(n):
    if n > 7:
        return
    else:
        DFS3(2*n)
        DFS3(2*n+1)
        print(n, end=' ')

DFS3(1)