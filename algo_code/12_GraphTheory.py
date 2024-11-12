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


if __name__ == '__main__':
    main_3()
