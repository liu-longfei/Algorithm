class Solution_1:
    @classmethod
    def removeElement(cls, nums: list, val: int):
        slowIndex = 0
        for fastIndex in range(len(nums)):
            if nums[fastIndex] != val:
                nums[slowIndex] = nums[fastIndex]
                slowIndex += 1
        return slowIndex


list_1 = [1, 2, 2, 3, 3, 4, 5]
print(Solution_1.removeElement(list_1, 1))
