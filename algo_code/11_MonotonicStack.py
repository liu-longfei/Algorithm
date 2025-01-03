# 一、739. 每日温度
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


# 二、496.下一个更大元素 I
class Solution_2:
    @classmethod
    def next_great_element(cls, nums1, nums2):
        result = [-1] * len(nums1)
        stack = [0]
        for i in range(1, len(nums2)):
            if nums2[i] <= nums2[stack[-1]]:
                stack.append(i)
            else:
                while len(stack) != 0 and nums2[i] > nums2[stack[-1]]:
                    if nums2[stack[-1]] in nums1:
                        index = nums1.index(nums2[stack[-1]])
                        result[index] = nums2[i]
                    stack.append(i)
        return result


print(Solution_2.next_great_element([4, 1, 2], [1, 3, 4, 2]))
print(Solution_2.next_great_element([2, 4], [1, 2, 3, 4]))


# 三、503.下一个更大元素II
class Solution_3:
    @classmethod
    def next_greate_elements(cls, nums: list):
        result = [-1] * len(nums)
        if len(nums) == 0:
            return result
        stack = [0]
        for i in range(1, len(nums) * 2):
            if len(stack) != 0 and nums[i % len(nums)] <= nums[stack[-1]]:
                stack.append(i % len(nums))
            else:
                while len(stack) != 0 and nums[i % len(nums)] > nums[stack[-1]]:
                    result[stack[-1]] = nums[i % len(nums)]
                    stack.pop()
                stack.append(i % len(nums))
        return result


print(Solution_3.next_greate_elements([1, 2, 1]))
print(Solution_3.next_greate_elements([2, -1, 2]))
