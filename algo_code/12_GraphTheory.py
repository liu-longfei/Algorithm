# 98. 所有可达路径
class Solution_3:
    @classmethod
    def dfs(cls, graph, x, n, path, result):
        if x == n:
            result.append(path.copy())
            return
        for i in range(1, n + 1):
            if graph[x][i] == 1:
                path.append(i)
                cls.dfs(graph, i, n, path, result)
                path.pop()


def main_3():
    n, m = map(int, input().split())
    # print(n, m)

    graph = [[0] * (n + 1) for _ in range(n + 1)]

    for _ in range(m):
        s, t = map(int, input().split())
        graph[s][t] = 1

    result = []
    Solution_3.dfs(graph, 1, n, [1], result)

    if len(result) == 0:
        print(-1)
    else:
        for i in result:
            print(' '.join(map(str, i)))


# 99. 岛屿数量, 深搜版
class Solution_5:
    direction = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    @classmethod
    def dfs(cls, grid, visited, x, y):
        for i, j in cls.direction:
            next_x = x + i
            next_y = y + j
            if next_x < 0 or next_x >= len(grid) or next_y < 0 or next_y >= len(grid[0]):
                continue
            if not visited[next_x][next_y] and grid[next_x][next_y]:
                visited[next_x][next_y] = True
                cls.dfs(grid, visited, next_x, next_y)

    @classmethod
    def main(cls):
        '''
4 5
1 1 0 0 0
1 1 0 0 0
0 0 1 0 0
0 0 0 1 1
        '''
        n, m = map(int, input().split())

        grid = []
        for i in range(n):
            grid.append(list(map(int, input().split())))

        visited = [[False] * m for _ in range(n)]

        res = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] and not visited[i][j]:
                    visited[i][j] = True
                    res += 1
                    cls.dfs(grid, visited, i, j)
        return res



# main_3()
# print(Solution_5.main())


# 六、99. 岛屿数量，广搜版
class Solution_6:
    directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    @classmethod
    def bfs(cls, grid, visited, i, j):
        from collections import deque
        que = deque([])
        que.append([i, j])
        while que:
            cur_x, cur_y = que.popleft()
            for x, y in cls.directions:
                next_x = cur_x + x
                next_y = cur_y + y
                if next_y < 0 or next_x < 0 or next_x >= len(grid) or next_y >= len(grid[0]):
                    continue
                if grid[next_x][next_y] and not visited[next_x][next_y]:
                    visited[next_x][next_y] = True
                    que.append([next_x, next_y])

    @classmethod
    def main(cls):
        '''
4 5
1 1 0 0 0
1 1 0 0 0
0 0 1 0 0
0 0 0 1 1
        '''
        n, m = map(int, input().split())

        grid = []
        for i in range(n):
            grid.append(list(map(int, input().split())))
        visited = [[False] * m for _ in range(n)]
        res = 0
        for i in range(n):
            for j in range(m):
                if not visited[i][j] and grid[i][j]:
                    res += 1
                    cls.bfs(grid, visited, i, j)
        print(res)


Solution_6.main()
