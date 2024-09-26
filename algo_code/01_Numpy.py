# 二分查找
class Solution_2:
    # 左闭右闭区间
    @classmethod
    def search(cls, nums: list[int], target: int):
        left, right = 0, len(nums) - 1
        while left <= right:
            middle = (left + right) // 2
            if nums[middle] > target:
                right = middle - 1
            elif nums[middle] < target:
                left = middle + 1
            else:
                return middle
        return -1

    # 左闭右开区间
    @classmethod
    def search_1(cls, nums: list[int], target: int):
        left, right = 0, len(nums) - 1
        while left < right:
            middle = (left + right) // 2
            if nums[middle] > target:
                right = middle - 1
            elif nums[middle] < target:
                left = middle + 1
            else:
                return middle
        return -1


list_1 = [-1, 2, 4, 8]
print(Solution_2.search(list_1, 3))


# 移除元素，快慢指针
class Solution_3:
    @classmethod
    def removeElement(cls, nums: list, val: int):
        slow = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[slow] = nums[i]
                slow += 1
        return slow


list_1 = [0, 1, 2, 3, 4, 2, 2, 2, 7]
print(Solution_3.removeElement(list_1, 2))
