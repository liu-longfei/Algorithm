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


class Solution_2:
    @classmethod
    def reverseStr(cls, s: list[str]):
        l, r = 0, len(s) - 1
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
        return s


list_1 = ['a', 'b', 'c', 'd']
print(Solution_2.reverseStr(list_1))
