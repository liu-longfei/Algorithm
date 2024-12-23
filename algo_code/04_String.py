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


class Solution_4:
    @classmethod
    def reverseWords_1(cls, s: str):
        s = s.strip()
        s = s[::-1]
        s = " ".join([word[::-1] for word in s.split()])
        return s

    @classmethod
    def reverseWords_2(cls, s: str):
        s = s.strip()
        word_list = s.split()
        l, r = 0, len(word_list) - 1
        while l < r:
            word_list[l], word_list[r] = word_list[r], word_list[l]
            l += 1
            r -= 1
        return " ".join(word_list)


print(Solution_4.reverseWords_1(" hello world! "))
print(Solution_4.reverseWords_2(" hello  world! "))


# # 五、右旋字符串
# k = int(input())
# str_1 = input()
#
# s = str_1[len(str_1) - k: len(str_1)] + str_1[:len(str_1) - k]
# print(s)


# 六、28. 实现 strStr()
class Solution_5:
    # 前缀表（不减一）
    @classmethod
    def get_next_1(cls, next: list[int], s: str) -> None:
        j = 0
        next[0] = 0
        for i in range(1, len(s)):
            while j > 0 and s[i] != s[j]:
                j = next[j - 1]
            if s[i] == s[j]:
                j += 1
            next[i] = j

    @classmethod
    def str_str(cls, haystack: str, needle: str):
        if len(needle) == 0:
            return 0
        next = [0] * len(needle)
        cls.get_next_1(next, needle)
        j = 0
        for i in range(len(haystack)):
            while j > 0 and haystack[i] != needle[j]:
                j = next[j-1]
            if haystack[i] == needle[j]:
                j += 1
            if j == len(needle):
                return i - len(needle) + 1
        return -1


str_1 = 'aabaaf'
list_1 = [0] * len(str_1)
Solution_5.get_next_1(list_1, str_1)
print(list_1)
haystack = 'aabaabaaf'
print(Solution_5.str_str(haystack, str_1))
