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


# 四、216.组合总和III
class Solution_4:
    @classmethod
    def combination_sum3(cls, n, k):
        path = []
        result = []
        cls.backtracking(n, k, 0, 1, path, result)
        return result

    @classmethod
    def backtracking(cls, n, k, current_sum, start_index, path: list, result: list):
        if current_sum > n:
            return
        if len(path) == k:
            if current_sum == n:
                result.append(path[:])
            return

        for i in range(start_index, 10):
            current_sum += i
            path.append(i)
            cls.backtracking(n, k, current_sum, i, path, result)
            current_sum -= i
            path.pop()


print(Solution_4.combination_sum3(7, 3))
