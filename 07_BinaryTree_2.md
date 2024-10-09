# 十、111.二叉树的最小深度

[力扣题目链接(opens new window)](https://leetcode.cn/problems/minimum-depth-of-binary-tree/)

给定一个二叉树，找出其最小深度。

最小深度是从根节点到最近叶子节点的最短路径上的节点数量。

说明: 叶子节点是指没有子节点的节点。

示例:

给定二叉树 [3,9,20,null,null,15,7],

![111.二叉树的最小深度1](https://code-thinking-1253855093.file.myqcloud.com/pics/2021020315582586.png)

返回它的最小深度 2.

## 算法公开课

**[《代码随想录》算法视频公开课 **(opens new window)**](https://programmercarl.com/other/gongkaike.html)：[看起来好像做过，一写就错！ | LeetCode：111.二叉树的最小深度 **(opens new window)**](https://www.bilibili.com/video/BV1QD4y1B7e2)，相信结合视频再看本篇题解，更有助于大家对本题的理解**。

## 思路

看完了这篇[104.二叉树的最大深度 **(opens new window)**](https://programmercarl.com/0104.%E4%BA%8C%E5%8F%89%E6%A0%91%E7%9A%84%E6%9C%80%E5%A4%A7%E6%B7%B1%E5%BA%A6.html)，再来看看如何求最小深度。

直觉上好像和求最大深度差不多，其实还是差不少的。

本题依然是前序遍历和后序遍历都可以，前序求的是深度，后序求的是高度。

* 二叉树节点的深度：指从根节点到该节点的最长简单路径边的条数或者节点数（取决于深度从0开始还是从1开始）
* 二叉树节点的高度：指从该节点到叶子节点的最长简单路径边的条数后者节点数（取决于高度从0开始还是从1开始）

那么使用后序遍历，其实求的是根节点到叶子节点的最小距离，就是求高度的过程，不过这个最小距离 也同样是最小深度。

以下讲解中遍历顺序上依然采用后序遍历（因为要比较递归返回之后的结果，本文我也给出前序遍历的写法）。

本题还有一个误区，在处理节点的过程中，最大深度很容易理解，最小深度就不那么好理解，如图：

https://code-thinking.cdn.bcebos.com/pics/111.%E4%BA%8C%E5%8F%89%E6%A0%91%E7%9A%84%E6%9C%80%E5%B0%8F%E6%B7%B1%E5%BA%A6.png（图像链接）

这就重新审题了，题目中说的是：**最小深度是从根节点到最近叶子节点的最短路径上的节点数量。**注意是**叶子节点**。

什么是叶子节点，左右孩子都为空的节点才是叶子节点！

### 递归法

来来来，一起递归三部曲：

1. 确定递归函数的参数和返回值

参数为要传入的二叉树根节点，返回的是int类型的深度。

代码如下：

```cpp
int getDepth(TreeNode* node)
```

2. 确定终止条件

终止条件也是遇到空节点返回0，表示当前节点的高度为0。

代码如下：

```cpp
if (node == NULL) return 0;
```

3. 确定单层递归的逻辑

这块和求最大深度可就不一样了，一些同学可能会写如下代码：

```cpp
int leftDepth = getDepth(node->left);
int rightDepth = getDepth(node->right);
int result = 1 + min(leftDepth, rightDepth);
return result;
```

这个代码就犯了此图中的误区：

https://code-thinking.cdn.bcebos.com/pics/111.%E4%BA%8C%E5%8F%89%E6%A0%91%E7%9A%84%E6%9C%80%E5%B0%8F%E6%B7%B1%E5%BA%A6.png（图像链接）

如果这么求的话，没有左孩子的分支会算为最短深度。

所以，如果左子树为空，右子树不为空，说明最小深度是 1 + 右子树的深度。

反之，右子树为空，左子树不为空，最小深度是 1 + 左子树的深度。 最后如果左右子树都不为空，返回左右子树深度最小值 + 1 。

代码如下：

```cpp
int leftDepth = getDepth(node->left);           // 左
int rightDepth = getDepth(node->right);         // 右
                                                // 中
// 当一个左子树为空，右不为空，这时并不是最低点
if (node->left == NULL && node->right != NULL) { 
    return 1 + rightDepth;
}   
// 当一个右子树为空，左不为空，这时并不是最低点
if (node->left != NULL && node->right == NULL) { 
    return 1 + leftDepth;
}
int result = 1 + min(leftDepth, rightDepth);
return result;
```

遍历的顺序为后序（左右中），可以看出：**求二叉树的最小深度和求二叉树的最大深度的差别主要在于处理左右孩子不为空的逻辑。**

整体递归代码如下：

```cpp
class Solution {
public:
    int getDepth(TreeNode* node) {
        if (node == NULL) return 0;
        int leftDepth = getDepth(node->left);           // 左
        int rightDepth = getDepth(node->right);         // 右
                                                        // 中
        // 当一个左子树为空，右不为空，这时并不是最低点
        if (node->left == NULL && node->right != NULL) { 
            return 1 + rightDepth;
        }   
        // 当一个右子树为空，左不为空，这时并不是最低点
        if (node->left != NULL && node->right == NULL) { 
            return 1 + leftDepth;
        }
        int result = 1 + min(leftDepth, rightDepth);
        return result;
    }

    int minDepth(TreeNode* root) {
        return getDepth(root);
    }
};
```

精简之后代码如下：

```cpp
class Solution {
public:
    int minDepth(TreeNode* root) {
        if (root == NULL) return 0;
        if (root->left == NULL && root->right != NULL) {
            return 1 + minDepth(root->right);
        }
        if (root->left != NULL && root->right == NULL) {
            return 1 + minDepth(root->left);
        }
        return 1 + min(minDepth(root->left), minDepth(root->right));
    }
};
```

**精简之后的代码根本看不出是哪种遍历方式，所以依然还要强调一波：如果对二叉树的操作还不熟练，尽量不要直接照着精简代码来学。**

前序遍历的方式：

```cpp
class Solution {
private:
    int result;
    void getdepth(TreeNode* node, int depth) {
        // 函数递归终止条件
        if (node == nullptr) {
            return;
        }
        // 中，处理逻辑：判断是不是叶子结点
        if (node -> left == nullptr && node->right == nullptr) {
            result = min(result, depth);
        }
        if (node->left) { // 左
            getdepth(node->left, depth + 1);
        }
        if (node->right) { // 右
            getdepth(node->right, depth + 1);
        }
        return ;
    }

public:
    int minDepth(TreeNode* root) {
        if (root == nullptr) {
            return 0;
        }
        result = INT_MAX;
        getdepth(root, 1);
        return result;
    }
};
```

### 迭代法

相对于[104.二叉树的最大深度 **(opens new window)**](https://programmercarl.com/0104.%E4%BA%8C%E5%8F%89%E6%A0%91%E7%9A%84%E6%9C%80%E5%A4%A7%E6%B7%B1%E5%BA%A6.html)，本题还可以使用层序遍历的方式来解决，思路是一样的。

如果对层序遍历还不清楚的话，可以看这篇：[二叉树：层序遍历登场！(opens new window)](https://programmercarl.com/0102.%E4%BA%8C%E5%8F%89%E6%A0%91%E7%9A%84%E5%B1%82%E5%BA%8F%E9%81%8D%E5%8E%86.html)

**需要注意的是，只有当左右孩子都为空的时候，才说明遍历到最低点了。如果其中一个孩子不为空则不是最低点**

代码如下：（详细注释）

```cpp
class Solution {
public:

    int minDepth(TreeNode* root) {
        if (root == NULL) return 0;
        int depth = 0;
        queue<TreeNode*> que;
        que.push(root);
        while(!que.empty()) {
            int size = que.size();
            depth++; // 记录最小深度
            for (int i = 0; i < size; i++) {
                TreeNode* node = que.front();
                que.pop();
                if (node->left) que.push(node->left);
                if (node->right) que.push(node->right);
                if (!node->left && !node->right) { // 当左右孩子都为空的时候，说明是最低点的一层了，退出
                    return depth;
                }
            }
        }
        return depth;
    }
};
```

## 其他语言版本

### Python :

递归法（版本一）

```python
class Solution:
    def getDepth(self, node):
        if node is None:
            return 0
        leftDepth = self.getDepth(node.left)  # 左
        rightDepth = self.getDepth(node.right)  # 右
      
        # 当一个左子树为空，右不为空，这时并不是最低点
        if node.left is None and node.right is not None:
            return 1 + rightDepth
      
        # 当一个右子树为空，左不为空，这时并不是最低点
        if node.left is not None and node.right is None:
            return 1 + leftDepth
      
        result = 1 + min(leftDepth, rightDepth)
        return result

    def minDepth(self, root):
        return self.getDepth(root)

```

递归法（版本二）

```python
class Solution:
    def minDepth(self, root):
        if root is None:
            return 0
        if root.left is None and root.right is not None:
            return 1 + self.minDepth(root.right)
        if root.left is not None and root.right is None:
            return 1 + self.minDepth(root.left)
        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))


```

递归法（版本三）前序

```python
class Solution:
    def __init__(self):
        self.result = float('inf')

    def getDepth(self, node, depth):
        if node is None:
            return
        if node.left is None and node.right is None:
            self.result = min(self.result, depth)
        if node.left:
            self.getDepth(node.left, depth + 1)
        if node.right:
            self.getDepth(node.right, depth + 1)

    def minDepth(self, root):
        if root is None:
            return 0
        self.getDepth(root, 1)
        return self.result


```

迭代法

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        depth = 0
        queue = collections.deque([root])
      
        while queue:
            depth += 1 
            for _ in range(len(queue)):
                node = queue.popleft()
              
                if not node.left and not node.right:
                    return depth
          
                if node.left:
                    queue.append(node.left)
                  
                if node.right:
                    queue.append(node.right)

        return depth
```
# 十一、222.完全二叉树的节点个数

[力扣题目链接(opens new window)](https://leetcode.cn/problems/count-complete-tree-nodes/)

给出一个完全二叉树，求出该树的节点个数。

示例 1：

* 输入：root = [1,2,3,4,5,6]
* 输出：6

示例 2：

* 输入：root = []
* 输出：0

示例 3：

* 输入：root = [1]
* 输出：1

提示：

* 树中节点的数目范围是[0, 5 \* 10^4]
* 0 <= Node.val <= 5 \* 10^4
* 题目数据保证输入的树是 完全二叉树

## 算法公开课

**[《代码随想录》算法视频公开课 **(opens new window)**](https://programmercarl.com/other/gongkaike.html)：[要理解普通二叉树和完全二叉树的区别！ | LeetCode：222.完全二叉树节点的数量 **(opens new window)**](https://www.bilibili.com/video/BV1eW4y1B7pD)，相信结合视频再看本篇题解，更有助于大家对本题的理解**。

## 思路

本篇给出按照普通二叉树的求法以及利用完全二叉树性质的求法。

### 普通二叉树

首先按照普通二叉树的逻辑来求。

这道题目的递归法和求二叉树的深度写法类似， 而迭代法，[二叉树：层序遍历登场！ **(opens new window)**](https://programmercarl.com/0102.%E4%BA%8C%E5%8F%89%E6%A0%91%E7%9A%84%E5%B1%82%E5%BA%8F%E9%81%8D%E5%8E%86.html)遍历模板稍稍修改一下，记录遍历的节点数量就可以了。

递归遍历的顺序依然是后序（左右中）。

#### 递归

如果对求二叉树深度还不熟悉的话，看这篇：[二叉树：看看这些树的最大深度 **(opens new window)**](https://programmercarl.com/0104.%E4%BA%8C%E5%8F%89%E6%A0%91%E7%9A%84%E6%9C%80%E5%A4%A7%E6%B7%B1%E5%BA%A6.html)。

1. 确定递归函数的参数和返回值：参数就是传入树的根节点，返回就返回以该节点为根节点二叉树的节点数量，所以返回值为int类型。

代码如下：

```cpp
int getNodesNum(TreeNode* cur) {
```

2. 确定终止条件：如果为空节点的话，就返回0，表示节点数为0。

代码如下：

```cpp
if (cur == NULL) return 0;
```

3. 确定单层递归的逻辑：先求它的左子树的节点数量，再求右子树的节点数量，最后取总和再加一 （加1是因为算上当前中间节点）就是目前节点为根节点的节点数量。

代码如下：

```cpp
int leftNum = getNodesNum(cur->left);      // 左
int rightNum = getNodesNum(cur->right);    // 右
int treeNum = leftNum + rightNum + 1;      // 中
return treeNum;
```

所以整体C++代码如下：

```cpp
// 版本一
class Solution {
private:
    int getNodesNum(TreeNode* cur) {
        if (cur == NULL) return 0;
        int leftNum = getNodesNum(cur->left);      // 左
        int rightNum = getNodesNum(cur->right);    // 右
        int treeNum = leftNum + rightNum + 1;      // 中
        return treeNum;
    }
public:
    int countNodes(TreeNode* root) {
        return getNodesNum(root);
    }
};
```

代码精简之后C++代码如下：

```cpp
// 版本二
class Solution {
public:
    int countNodes(TreeNode* root) {
        if (root == NULL) return 0;
        return 1 + countNodes(root->left) + countNodes(root->right);
    }
};
```

* 时间复杂度：O(n)
* 空间复杂度：O(log n)，算上了递归系统栈占用的空间

**网上基本都是这个精简的代码版本，其实不建议大家照着这个来写，代码确实精简，但隐藏了一些内容，连遍历的顺序都看不出来，所以初学者建议学习版本一的代码，稳稳的打基础**。

#### 迭代

如果对求二叉树层序遍历还不熟悉的话，看这篇：[二叉树：层序遍历登场！ **(opens new window)**](https://programmercarl.com/0102.%E4%BA%8C%E5%8F%89%E6%A0%91%E7%9A%84%E5%B1%82%E5%BA%8F%E9%81%8D%E5%8E%86.html)。

那么只要模板少做改动，加一个变量result，统计节点数量就可以了

```cpp
class Solution {
public:
    int countNodes(TreeNode* root) {
        queue<TreeNode*> que;
        if (root != NULL) que.push(root);
        int result = 0;
        while (!que.empty()) {
            int size = que.size();
            for (int i = 0; i < size; i++) {
                TreeNode* node = que.front();
                que.pop();
                result++;   // 记录节点数量
                if (node->left) que.push(node->left);
                if (node->right) que.push(node->right);
            }
        }
        return result;
    }
};
```

* 时间复杂度：O(n)
* 空间复杂度：O(n)

### 完全二叉树

以上方法都是按照普通二叉树来做的，对于完全二叉树特性不了解的同学可以看这篇 [关于二叉树，你该了解这些！ **(opens new window)**](https://programmercarl.com/%E4%BA%8C%E5%8F%89%E6%A0%91%E7%90%86%E8%AE%BA%E5%9F%BA%E7%A1%80.html)，这篇详细介绍了各种二叉树的特性。

在完全二叉树中，除了最底层节点可能没填满外，其余每层节点数都达到最大值，并且最下面一层的节点都集中在该层最左边的若干位置。若最底层为第 h 层，则该层包含 1\~ 2^(h-1)  个节点。

**大家要自己看完全二叉树的定义，很多同学对完全二叉树其实不是真正的懂了。**

我来举一个典型的例子如题：

https://code-thinking-1253855093.file.myqcloud.com/pics/20200920221638903-20230310123444151.png（图像链接）

完全二叉树只有两种情况，情况一：就是满二叉树，情况二：最后一层叶子节点没有满。

对于情况一，可以直接用 2^树深度 - 1 来计算，注意这里根节点深度为1。

对于情况二，分别递归左孩子，和右孩子，递归到某一深度一定会有左孩子或者右孩子为满二叉树，然后依然可以按照情况1来计算。

完全二叉树（一）如图：

https://code-thinking-1253855093.file.myqcloud.com/pics/20201124092543662.png（图像链接）

完全二叉树（二）如图：

https://code-thinking-1253855093.file.myqcloud.com/pics/20201124092634138.png（图像链接）

可以看出如果整个树不是满二叉树，就递归其左右孩子，直到遇到满二叉树为止，用公式计算这个子树（满二叉树）的节点数量。

这里关键在于如何去判断一个左子树或者右子树是不是满二叉树呢？

在完全二叉树中，如果递归向左遍历的深度等于递归向右遍历的深度，那说明就是满二叉树。如图：

https://code-thinking-1253855093.file.myqcloud.com/pics/20220829163554.png（图像链接）

在完全二叉树中，如果递归向左遍历的深度不等于递归向右遍历的深度，则说明不是满二叉树，如图：

https://code-thinking-1253855093.file.myqcloud.com/pics/20220829163709.png（图像链接）

那有录友说了，这种情况，递归向左遍历的深度等于递归向右遍历的深度，但也不是满二叉树，如题：

https://code-thinking-1253855093.file.myqcloud.com/pics/20220829163811.png（图像链接）

如果这么想，大家就是对 完全二叉树理解有误区了，**以上这棵二叉树，它根本就不是一个完全二叉树**！

判断其子树是不是满二叉树，如果是则利用公式计算这个子树（满二叉树）的节点数量，如果不是则继续递归，那么 在递归三部曲中，第二部：终止条件的写法应该是这样的：

```cpp
if (root == nullptr) return 0; 
// 开始根据左深度和右深度是否相同来判断该子树是不是满二叉树
TreeNode* left = root->left;
TreeNode* right = root->right;
int leftDepth = 0, rightDepth = 0; // 这里初始为0是有目的的，为了下面求指数方便
while (left) {  // 求左子树深度
    left = left->left;
    leftDepth++;
}
while (right) { // 求右子树深度
    right = right->right;
    rightDepth++;
}
if (leftDepth == rightDepth) {
    return (2 << leftDepth) - 1; // 注意(2<<1) 相当于2^2，返回满足满二叉树的子树节点数量
}
```

递归三部曲，第三部，单层递归的逻辑：（可以看出使用后序遍历）

```cpp
int leftTreeNum = countNodes(root->left);       // 左
int rightTreeNum = countNodes(root->right);     // 右
int result = leftTreeNum + rightTreeNum + 1;    // 中
return result;
```

该部分精简之后代码为：

```cpp
return countNodes(root->left) + countNodes(root->right) + 1; 
```

最后整体C++代码如下：

```cpp
class Solution {
public:
    int countNodes(TreeNode* root) {
        if (root == nullptr) return 0;
        TreeNode* left = root->left;
        TreeNode* right = root->right;
        int leftDepth = 0, rightDepth = 0; // 这里初始为0是有目的的，为了下面求指数方便
        while (left) {  // 求左子树深度
            left = left->left;
            leftDepth++;
        }
        while (right) { // 求右子树深度
            right = right->right;
            rightDepth++;
        }
        if (leftDepth == rightDepth) {
            return (2 << leftDepth) - 1; // 注意(2<<1) 相当于2^2，所以leftDepth初始为0
        }
        return countNodes(root->left) + countNodes(root->right) + 1;
    }
};
```

* 时间复杂度：O(log n × log n)
* 空间复杂度：O(log n)

## 其他语言版本

### Python:

递归法：

```python
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        return self.getNodesNum(root)
      
    def getNodesNum(self, cur):
        if not cur:
            return 0
        leftNum = self.getNodesNum(cur.left) #左
        rightNum = self.getNodesNum(cur.right) #右
        treeNum = leftNum + rightNum + 1 #中
        return treeNum
```

递归法：精简版

```python
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
```

迭代法：

```python
import collections
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        queue = collections.deque()
        if root:
            queue.append(root)
        result = 0
        while queue:
            size = len(queue)
            for i in range(size):
                node = queue.popleft()
                result += 1 #记录节点数量
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return result
```

完全二叉树

```python
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        left = root.left
        right = root.right
        leftDepth = 0 #这里初始为0是有目的的，为了下面求指数方便
        rightDepth = 0
        while left: #求左子树深度
            left = left.left
            leftDepth += 1
        while right: #求右子树深度
            right = right.right
            rightDepth += 1
        if leftDepth == rightDepth:
            return (2 << leftDepth) - 1 #注意(2<<1) 相当于2^2，所以leftDepth初始为0
        return self.countNodes(root.left) + self.countNodes(root.right) + 1
```

完全二叉树写法2

```python
class Solution: # 利用完全二叉树特性
    def countNodes(self, root: TreeNode) -> int:
        if not root: return 0
        count = 1
        left = root.left; right = root.right
        while left and right:
            count+=1
            left = left.left; right = right.right
        if not left and not right: # 如果同时到底说明是满二叉树，反之则不是
            return 2**count-1
        return 1+self.countNodes(root.left)+self.countNodes(root.right)  
```

完全二叉树写法3

```python
class Solution: # 利用完全二叉树特性
    def countNodes(self, root: TreeNode) -> int:
        if not root: return 0
        count = 0
        left = root.left; right = root.right
        while left and right:
            count+=1
            left = left.left; right = right.right
        if not left and not right: # 如果同时到底说明是满二叉树，反之则不是
            return (2<<count)-1
        return 1+self.countNodes(root.left)+self.countNodes(root.right)  
```
