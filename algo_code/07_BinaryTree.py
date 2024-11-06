import collections
from typing import Optional


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 二叉树递归的前中后序遍历
class Solution_2:
    @classmethod
    def preorderTraversal(cls, root: TreeNode):
        res = []
        def dfs(node):
            if node is None:
                return
            res.append(node.val)
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return res

    @classmethod
    def inorderTraversal(cls, root):
        res = []
        def dfs(node):
            if node is None:
                return
            dfs(root.left)
            res.append(node.val)
            dfs(root.right)
        dfs(root)
        return res

    @classmethod
    def postorderTraversal(cls, root):
        res = []
        def dfs(node):
            if node is None:
                return
            dfs(root.left)
            dfs(root.right)
            res.append(root.val)
        dfs(root)
        return res


# 层序遍历
class Solution_5:
    @classmethod
    def levelOrder(cls, root: Optional[TreeNode]):
        if not root:
            return []
        queue = collections.deque([root])
        result = []
        while queue:
            level_res = []
            for _ in range(len(queue)):
                cur = queue.popleft()
                level_res.append(cur.val)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            result.append(level_res)
        return result

# 构建测试数据
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

print(Solution_5.levelOrder(root))


# 翻转二叉树，递归
class Solution_6:
    @classmethod
    def invertTree(cls, root: TreeNode):
        if not root:
            return None
        root.left, root.right = root.right, root.left
        cls.invertTree(root.left)
        cls.invertTree(root.right)
        return root


# 构建测试数据
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(9)

print(Solution_5.levelOrder(root))
print(Solution_5.levelOrder(Solution_6.invertTree(root)))
