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
