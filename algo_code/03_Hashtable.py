# 242.有效的字母异位词
class Solution_2:
    @classmethod
    def isAnagram(cls, s: str, t: str):
        record = [0] * 26
        for i in s:
            record[ord(i) - ord('a')] += 1
        for j in t:
            record[ord(j) - ord('a')] -= 1
        for k in record:
            if k != 0:
                return False
        return True


s = 'abcdz'
t = 'bacdz'
print(Solution_2().isAnagram(s, t))


# 349. 两个数组的交集
class Solution_3:
    @classmethod
    def intersection(cls, nums1: list[int], nums2: list[int]):
        nums1_dict = {}
        for i in nums1:
            nums1_dict[i] = nums1_dict.get(i, 0) + 1
        result_set = set()
        for j in nums2:
            if j in nums1_dict:
                result_set.add(j)
                del nums1_dict[j]
        return list(result_set)


nums1 = [1, 2, 3, 4]
nums2 = [2, 4, 6, 7]
print(Solution_3.intersection(nums1, nums2))


# 四、第202题. 快乐数
class Solution_4:
    def get_sum(self, n):
        new_sum = 0
        while n:
            n, r = divmod(n, 10)
            new_sum += r * r
        return new_sum

    @classmethod
    def isHappy(cls, n):
        record = set()
        while True:
            new_sum = cls.get_sum(cls, n)
            # print(new_sum)
            if new_sum == 1:
                return True
            elif new_sum in record:
                return False
            else:
                record.add(new_sum)
                n = new_sum

print(Solution_4.isHappy(129))


# 1. 两数之和
class Solution_5:
    @classmethod
    def twoSum(cls, nums: list[int], target: int):
        records = dict()
        for idx, val in enumerate(nums):
            if target - val in records:
                return [records[target - val], idx]
            records[val] = idx
        return []

print(Solution_5.twoSum([0, 1, 2, 3, 4, 5, 100], 105))


# 第454题.四数相加II
class Solution_6:
    @classmethod
    def for_sum_count(cls, a, b, c, d):
        dict_1 = {}
        for i in a:
            for j in b:
                dict_1[i + j] = dict_1.get(i + j, 0) + 1
        count = 0
        for m in c:
            for n in d:
                key = -m - n
                if key in dict_1:
                    count += dict_1[key]
        return count


print(Solution_6.for_sum_count([1, 2], [-2, -1], [-1, 2], [0, 2]))


# 七、383. 赎金信
class Solution_7:
    @classmethod
    def can_construct(cls, ransom: str, magazine: str):
        count_dict = {}
        for i in magazine:
            count_dict[i] = count_dict.get(i, 0) + 1
        for j in ransom:
            if j not in count_dict or count_dict.get(j) == 0:
                return False
            count_dict[j] -= 1
        return True


print(Solution_7.can_construct('aa', 'aab'))
