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


# 541. 反转字符串II
class Solution_2:
    @classmethod
    def reverseStr(cls, s: str, k: int):
        def reverse(text):
            left, right = 0, len(text) - 1
            while left < right:
                text[left], text[right] = text[right], text[left]
                left += 1
                right -= 1
            return text

        list_s = list(s)
        for i in range(0, len(list_s), 2 * k):
            list_s[i: i+k] = reverse(list_s[i:i+k])
        s = ''.join(list_s)
        return s

s = 'abcde'
print(Solution_2.reverseStr(s, 3))


# 替换数字
class Solution_3:
    @classmethod
    def changeDigit(cls, s):
        list_s = list(s)
        for i in range(len(list_s)):
            if list_s[i].isdigit():
                list_s[i] = 'number'
        return ''.join(list_s)


print(Solution_3.changeDigit('abc1dce'))
