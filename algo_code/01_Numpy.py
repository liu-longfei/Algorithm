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


class Solution_4:
    @classmethod
    def sortSquares(cls, nums: list[int]) -> list[int]:
        left = 0
        right = len(nums) - 1
        index = len(nums) - 1
        results = [0] * len(nums)
        while left <= right:
            if nums[left] ** 2 > nums[right] ** 2:
                results[index] = nums[left] ** 2
                left += 1
            else:
                results[index] = nums[right] ** 2
                right -= 1
            index -= 1
        return results


list_1 = [-10, -2, 0, 4, 100]
print(Solution_4.sortSquares(list_1))


# 209.长度最小的子数组
class Solution_5:
    @classmethod
    def min_subarray_length(cls, s: int, nums: list):
        min_len = float('inf')
        idx = 0
        sum = 0

        for i in range(len(nums)):
            sum += nums[i]
            while sum >= s:
                len_ = i - idx + 1
                min_len = min_len if min_len < len_ else len_
                sum -= nums[idx]
                idx += 1

        return 0 if min_len == float('inf') else min_len


print(Solution_5.min_subarray_length(7, [2, 3, 1, 2, 4, 3]))


# 59.螺旋矩阵II
class Solution_6:
    @classmethod
    def generate_matrix(cls, n: int):
        nums = [[0] * n for _ in range(n)]
        startx, starty = 0, 0
        loop = n // 2
        mid = n // 2
        count = 1

        for offset in range(1, loop + 1):

            for i in range(starty, n - offset):
                nums[startx][i] = count
                count += 1

            for i in range(startx, n - offset):
                nums[i][n - offset] = count
                count += 1

            for i in range(n - offset, starty, -1):
                nums[n - offset][i] = count
                count += 1

            for i in range(n - offset, startx, -1):
                nums[i][starty] = count
                count += 1

            startx += 1
            starty += 1

        if n % 2:
            nums[mid][mid] = count
        return nums


for i in Solution_6.generate_matrix(7):
    print(i)
