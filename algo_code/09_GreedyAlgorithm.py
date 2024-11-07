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
