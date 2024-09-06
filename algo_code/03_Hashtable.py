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
