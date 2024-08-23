# 力扣题目链接：https://leetcode.cn/problems/reverse-string/
class Solution_1:
    def reverseString(self, s: list[str]) -> list[str]:
        left = 0
        right = len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        return s

rs = Solution_1()
s = ['a', 'b', 'c', 'd']
print(rs.reverseString(s))
