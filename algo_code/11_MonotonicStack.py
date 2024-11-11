class Solution_1:
    @classmethod
    def daily_temperature(cls, nums1):
        result = [0] * len(nums1)
        stack = [0]
        for i in range(1, len(nums1)):
            while len(stack) != 0 and nums1[i] > nums1[stack[-1]]:
                result[stack[-1]] = i - stack[-1]
                stack.pop()
            stack.append(i)
        return result


print(Solution_1.daily_temperature([73, 74, 75, 71, 69, 72, 76, 73]))
