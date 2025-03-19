# 查找缺省的最小正整数
def find_smallest_missing_positive(nums: list):
    positive_nums = [i for i in nums if i > 0]
    # positive_nums = list(set(positive_nums))
    positive_nums.sort()

    smallest_num = 1
    for num in positive_nums:
        if num == smallest_num:
            smallest_num += 1
        elif num > smallest_num:
            break
    return smallest_num


# 测试示例
nums = [3, 4, -1, 1, 2, 2]
print(find_smallest_missing_positive(nums))
