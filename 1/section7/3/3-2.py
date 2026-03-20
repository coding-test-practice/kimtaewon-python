N = int(input())

def DFS(v, temp):
    global N
    if v > N:
        print(*temp)
        return
    else:
        temp.append(v)
        DFS(v+1, temp)
        temp.pop()
        DFS(v+1, temp)

DFS(1, [])
