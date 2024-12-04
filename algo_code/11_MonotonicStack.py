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
