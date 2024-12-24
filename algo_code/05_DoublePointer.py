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


class Solution_3:
    @classmethod
    def change(cls, s):
        list_1 = list(s)
        for i in range(len(list_1)):
            if list_1[i].isdigit():
                list_1[i] = 'number'
        return ''.join(list_1)


print(Solution_3.change('a1b2c3'))


# 四、151.翻转字符串里的单词
class Solution_4:
    @classmethod
    def reverse_words_1(cls, s: str):
        s = s.strip()
        s = s[::-1]
        s = ' '.join([word[::-1] for word in s.split()])
        return s

    @classmethod
    def reverse_words_2(cls, s: str):
        s = s.strip()
        words_list = s.split()
        l = 0
        r = len(words_list) - 1
        while l < r:
            words_list[l], words_list[r] = words_list[r], words_list[l]
            l += 1
            r -= 1
        return ' '.join(words_list)


print(Solution_4.reverse_words_1('hello world'))
print(Solution_4.reverse_words_2('hello world'))


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 五、206.反转链表
class Solution_5:
    @classmethod
    def reverse_list(cls, head: ListNode):
        cur = head
        pre = None
        while cur:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        return pre


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

res = Solution_5.reverse_list(head)


while res:
    print(res.val, end=" -> ")
    res = res.next
