class Solution_2:
    @classmethod
    def combine(cls, n, k):
        result = []
        cls.backtracking(n, k, 1, [], result)
        return result

    @classmethod
    def backtracking(cls, n, k, start_index, path, result):
        if len(path) == k:
            result.append(path[:])
            return
        for i in range(start_index, n + 1):
            path.append(i)
            cls.backtracking(n, k, i+1, path, result)
            path.pop()


print(Solution_2.combine(5, 3))


# 三、77.组合优化
class Solution_3:
    @classmethod
    def combine(cls, n, k):
        result = []
        cls.backtracking(n, k, 1, [], result)
        return result

    @classmethod
    def backtracking(cls, n, k, start_index, path, result):
        if len(path) == k:
            result.append(path[:])

        for i in range(start_index, n - (k - len(path)) + 2):
            path.append(i)
            cls.backtracking(n, k, i, path, result)
            path.pop()


print(Solution_2.combine(5, 3))
