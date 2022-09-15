'''
    Date : 2022년 9월 15일
    Author : 이푸름
    Description: 이것이 코딩 테스트다 음료수 얼려 먹기 예제
'''

n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int,input())))

# DFS로 특정 노드 방문한 뒤에 연결된 모든 노드들도 방문
def dfs(x, y):
    # 범위 벗어나는 경우
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    # 현재 노드 방문하지 않았다면
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False


# 모든 노드에 대하여 음료수 채우기
result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1

print(result)
