from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution_2:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # 创建虚拟头部节点以简化删除过程
        dummy_head = ListNode(next=head)

        # 遍历列表并删除值为val的节点
        current = dummy_head
        while current.next:
            if current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next

        return dummy_head.next


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(6)
head.next.next.next = ListNode(3)
head.next.next.next.next = ListNode(4)
head.next.next.next.next.next = ListNode(5)
head.next.next.next.next.next.next = ListNode(6)

obj = Solution_2()
# 移除值为 6 的节点
new_head = obj.removeElements(head, 6)

# 打印移除后的链表
curr = new_head
while curr:
    print(curr.val, end=" -> ")
    curr = curr.next


# 设计链表
class Solution_3:
    pass


class Solution_4:
    @classmethod
    def reverseList(cls, head: ListNode):
        pre = None
        cur = head
        while cur:
            tmp = cur.next
            cur.next = pre
            
            pre = cur
            cur = tmp
        return pre
