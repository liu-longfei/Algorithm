class Solution_2:
    def isAnagram(self, s: str, t: str):
        record = [0] * 26
        for i in s:
            record[ord(i) - ord('a')] += 1
        for j in t:
            record[ord(j) - ord('a')] -= 1
        for k in record:
            if k != 0:
                return False
        return True


if __name__ == '__main__':
    # 力扣题目链接：https://leetcode.cn/problems/valid-anagram/
    solution_2 = Solution_2()
    s = 'abcdz'
    t = 'bacdz'
    print(solution_2.isAnagram(s, t))
