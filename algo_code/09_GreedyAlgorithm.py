class Solution_2:
    # 大饼干优先胃口大的
    @classmethod
    def find_content_children_1(cls, g: list, size: list):
        g.sort()
        size.sort()
        index = len(size) - 1
        result = 0
        for i in range(len(g) - 1, -1, -1):
            if index >= 0 and size[index] >= g[i]:
                result += 1
                index -= 1
        return result

    # 小饼干优先胃口小的
    @classmethod
    def find_content_children_2(cls, g: list, size: list):
        g.sort()
        size.sort()
        index = 0
        result = 0
        for i in range(len(size)):
            if index < len(g) and size[index] >= g[i]:
                index += 1
                result += 1
        return result


print(Solution_2.find_content_children_1([1, 2, 3], [1, 1]))
print(Solution_2.find_content_children_2([1, 2, 3], [1, 1]))

print(Solution_2.find_content_children_1([1, 2], [1, 2, 3]))
print(Solution_2.find_content_children_2([1, 2], [1, 2, 3]))


# 三、376. 摆动序列
class Solution_3:
    @classmethod
    def wiggle_max_length_greedy(cls, nums):
        if len(nums) <= 1:
            return len(nums)

        pre_diff = 0
        cur_diff = 0
        result = 1
        for i in range(len(nums) - 1):
            cur_diff = nums[i+1] - nums[i]
            if (pre_diff >= 0 and cur_diff < 0) or (pre_diff <= 0 and cur_diff > 0):
                result += 1
                pre_diff = cur_diff
        return result

    @classmethod
    def wiggle_max_lenth_dynamic(cls, nums):
        if len(nums) <= 1:
            return len(nums)

        dynamic_nums = [[0, 0] for _ in range(len(nums))]
        for i in range(len(nums)):
            dynamic_nums[i][0], dynamic_nums[i][1] = 1, 1
            for j in range(i):
                if dynamic_nums[i][0] > nums[j]:
                    dynamic_nums[i][0] = max(dynamic_nums[i][0], dynamic_nums[j][1] + 1)
                if dynamic_nums[i][1] < nums[j]:
                    dynamic_nums[i][1] = max(dynamic_nums[i][1], dynamic_nums[i][0] + 1)
        return max(dynamic_nums[-1][0], dynamic_nums[-1][1])


result_1 = Solution_3.wiggle_max_length_greedy([1, 2, 2, 2, 3, 4])
result_2 = Solution_3.wiggle_max_lenth_dynamic([1, 2, 2, 2, 3, 4])
print(result_1, result_2)

