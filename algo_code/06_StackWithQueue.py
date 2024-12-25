# 四、20. 有效的括号
class Solution_4:
    @staticmethod
    def is_valid(s: str):
        if len(s) % 2 != 0:
            return False
        stack = []
        for item in s:
            if item == '(':
                stack.append(')')
            elif item == '{':
                stack.append('}')
            elif item == '[':
                stack.append(']')
            elif not stack or item != stack[-1]:
                return False
            else:
                stack.pop()
        return True


print(Solution_4.is_valid("()[]{}"))
print(Solution_4.is_valid("([{}])))"))


# 1047. 删除字符串中的所有相邻重复项
class Solution_5:
    @classmethod
    def remove_duplicates(cls, S: str):
        result = list()
        for s in S:
            if result and result[-1] == s:
                result.pop()
            else:
                result.append(s)
        return ''.join(result)


print(Solution_5.remove_duplicates('abbaca'))
