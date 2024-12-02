# 二、509. 斐波那契数
class Solution_2:
    # 使用动态规划
    @classmethod
    def fib(cls, n):
        if n == 0 or n == 1:
            return n
        dp = [0] * (n + 1)
        dp[1] = 1
        for i in range(2, n + 1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]

    # 使用递归
    @classmethod
    def fib_2(cls, n):
        if n == 0 or n == 1:
            return n
        return cls.fib_2(n - 1) + cls.fib_2(n - 2)


print(Solution_2.fib(10))
print(Solution_2.fib_2(10))


# 三、70. 爬楼梯
class Solution_3:
    @classmethod
    def climb_stair(cls, n: int):
        if n <= 2:
            return n
        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n + 1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]


print(Solution_3.climb_stair(3))
