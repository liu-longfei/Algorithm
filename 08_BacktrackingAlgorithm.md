# 一、回溯算法理论基础

## 题目分类

https://code-thinking-1253855093.file.myqcloud.com/pics/20210219192050666.png（图像链接）

## 算法公开课

**[《代码随想录》算法视频公开课 **(opens new window)**](https://programmercarl.com/other/gongkaike.html)：[带你学透回溯算法（理论篇） **(opens new window)**](https://www.bilibili.com/video/BV1cy4y167mM/)，相信结合视频再看本篇题解，更有助于大家对本题的理解。**

## 理论基础

### 什么是回溯法

回溯法也可以叫做回溯搜索法，它是一种搜索的方式。

在二叉树系列中，我们已经不止一次，提到了回溯，例如[二叉树：以为使用了递归，其实还隐藏着回溯 **(opens new window)**](https://programmercarl.com/%E4%BA%8C%E5%8F%89%E6%A0%91%E4%B8%AD%E9%80%92%E5%BD%92%E5%B8%A6%E7%9D%80%E5%9B%9E%E6%BA%AF.html)。

回溯是递归的副产品，只要有递归就会有回溯。

**所以以下讲解中，回溯函数也就是递归函数，指的都是一个函数**。

### 回溯法的效率

回溯法的性能如何呢，这里要和大家说清楚了，**虽然回溯法很难，很不好理解，但是回溯法并不是什么高效的算法**。

**因为回溯的本质是穷举，穷举所有可能，然后选出我们想要的答案**，如果想让回溯法高效一些，可以加一些剪枝的操作，但也改不了回溯法就是穷举的本质。

那么既然回溯法并不高效为什么还要用它呢？

因为没得选，一些问题能暴力搜出来就不错了，撑死了再剪枝一下，还没有更高效的解法。

此时大家应该好奇了，都什么问题，这么牛逼，只能暴力搜索。

### 回溯法解决的问题

回溯法，一般可以解决如下几种问题：

* 组合问题：N个数里面按一定规则找出k个数的集合
* 切割问题：一个字符串按一定规则有几种切割方式
* 子集问题：一个N个数的集合里有多少符合条件的子集
* 排列问题：N个数按一定规则全排列，有几种排列方式
* 棋盘问题：N皇后，解数独等等

**相信大家看着这些之后会发现，每个问题，都不简单！**

另外，会有一些同学可能分不清什么是组合，什么是排列？

**组合是不强调元素顺序的，排列是强调元素顺序**。

例如：{1, 2} 和 {2, 1} 在组合上，就是一个集合，因为不强调顺序，而要是排列的话，{1, 2} 和 {2, 1} 就是两个集合了。

记住组合无序，排列有序，就可以了。

### 如何理解回溯法

**回溯法解决的问题都可以抽象为树形结构**，是的，我指的是所有回溯法的问题都可以抽象为树形结构！

因为回溯法解决的都是在集合中递归查找子集，**集合的大小就构成了树的宽度，递归的深度就构成了树的深度**。

递归就要有终止条件，所以必然是一棵高度有限的树（N叉树）。

这块可能初学者还不太理解，后面的回溯算法解决的所有题目中，我都会强调这一点并画图举相应的例子，现在有一个印象就行。

### 回溯法模板

这里给出Carl总结的回溯算法模板。

在讲[二叉树的递归 **(opens new window)**](https://programmercarl.com/%E4%BA%8C%E5%8F%89%E6%A0%91%E7%9A%84%E9%80%92%E5%BD%92%E9%81%8D%E5%8E%86.html)中我们说了递归三部曲，这里我再给大家列出回溯三部曲。

* 回溯函数模板返回值以及参数

在回溯算法中，我的习惯是函数起名字为backtracking，这个起名大家随意。

回溯算法中函数返回值一般为void。

再来看一下参数，因为回溯算法需要的参数可不像二叉树递归的时候那么容易一次性确定下来，所以一般是先写逻辑，然后需要什么参数，就填什么参数。

但后面的回溯题目的讲解中，为了方便大家理解，我在一开始就帮大家把参数确定下来。

回溯函数伪代码如下：

```text
void backtracking(参数)
```

* 回溯函数终止条件

既然是树形结构，那么我们在讲解[二叉树的递归 **(opens new window)**](https://programmercarl.com/%E4%BA%8C%E5%8F%89%E6%A0%91%E7%9A%84%E9%80%92%E5%BD%92%E9%81%8D%E5%8E%86.html)的时候，就知道遍历树形结构一定要有终止条件。

所以回溯也要有终止条件。

什么时候达到了终止条件，树中就可以看出，一般来说搜到叶子节点了，也就找到了满足条件的一条答案，把这个答案存放起来，并结束本层递归。

所以回溯函数终止条件伪代码如下：

```text
if (终止条件) {
    存放结果;
    return;
}
```

* 回溯搜索的遍历过程

在上面我们提到了，回溯法一般是在集合中递归搜索，集合的大小构成了树的宽度，递归的深度构成的树的深度。

如图：

https://code-thinking-1253855093.file.myqcloud.com/pics/20210130173631174.png（图像链接）

注意图中，我特意举例集合大小和孩子的数量是相等的！

回溯函数遍历过程伪代码如下：

```text
for (选择：本层集合中元素（树中节点孩子的数量就是集合的大小）) {
    处理节点;
    backtracking(路径，选择列表); // 递归
    回溯，撤销处理结果
}
```

for循环就是遍历集合区间，可以理解一个节点有多少个孩子，这个for循环就执行多少次。

backtracking这里自己调用自己，实现递归。

大家可以从图中看出**for循环可以理解是横向遍历，backtracking（递归）就是纵向遍历**，这样就把这棵树全遍历完了，一般来说，搜索叶子节点就是找的其中一个结果了。

分析完过程，回溯算法模板框架如下：

```text
void backtracking(参数) {
    if (终止条件) {
        存放结果;
        return;
    }

    for (选择：本层集合中元素（树中节点孩子的数量就是集合的大小）) {
        处理节点;
        backtracking(路径，选择列表); // 递归
        回溯，撤销处理结果
    }
}

```

**这份模板很重要，后面做回溯法的题目都靠它了！**

如果从来没有学过回溯算法的录友们，看到这里会有点懵，后面开始讲解具体题目的时候就会好一些了，已经做过回溯法题目的录友，看到这里应该会感同身受了。

## 总结

本篇我们讲解了，什么是回溯算法，知道了回溯和递归是相辅相成的。

接着提到了回溯法的效率，回溯法其实就是暴力查找，并不是什么高效的算法。

然后列出了回溯法可以解决几类问题，可以看出每一类问题都不简单。

最后我们讲到回溯法解决的问题都可以抽象为树形结构（N叉树），并给出了回溯法的模板。

今天是回溯算法的第一天，按照惯例Carl都是先概述一波，然后在开始讲解具体题目，没有接触过回溯法的同学刚学起来有点看不懂很正常，后面和具体题目结合起来会好一些。

# 二、第77题. 组合

[力扣题目链接(opens new window)](https://leetcode.cn/problems/combinations/)

给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。

示例: 输入: n = 4, k = 2 输出: [ [2,4], [3,4], [2,3], [1,2], [1,3], [1,4], ]

## 算法公开课

[《代码随想录》算法视频公开课 **(opens new window)**](https://programmercarl.com/other/gongkaike.html)：[带你学透回溯算法-组合问题（对应力扣题目：77.组合） **(opens new window)**](https://www.bilibili.com/video/BV1ti4y1L7cv)，[组合问题的剪枝操作 **(opens new window)**](https://www.bilibili.com/video/BV1wi4y157er)，**相信结合视频在看本篇题解，更有助于大家对本题的理解**。

## 思路

本题是回溯法的经典题目。

直接的解法当然是使用for循环，例如示例中k为2，很容易想到 用两个for循环，这样就可以输出 和示例中一样的结果。

代码如下：

```cpp
int n = 4;
for (int i = 1; i <= n; i++) {
    for (int j = i + 1; j <= n; j++) {
        cout << i << " " << j << endl;
    }
}
```

输入：n = 100, k = 3 那么就三层for循环，代码如下：

```cpp
int n = 100;
for (int i = 1; i <= n; i++) {
    for (int j = i + 1; j <= n; j++) {
        for (int u = j + 1; u <= n; n++) {
            cout << i << " " << j << " " << u << endl;
        }
    }
}
```

**如果n为100，k为50呢，那就50层for循环，是不是开始窒息**。

**此时就会发现虽然想暴力搜索，但是用for循环嵌套连暴力都写不出来！**

咋整？

回溯搜索法来了，虽然回溯法也是暴力，但至少能写出来，不像for循环嵌套k层让人绝望。

那么回溯法怎么暴力搜呢？

上面我们说了**要解决 n为100，k为50的情况，暴力写法需要嵌套50层for循环，那么回溯法就用递归来解决嵌套层数的问题**。

递归来做层叠嵌套（可以理解是开k层for循环），**每一次的递归中嵌套一个for循环，那么递归就可以用于解决多层嵌套循环的问题了**。

此时递归的层数大家应该知道了，例如：n为100，k为50的情况下，就是递归50层。

一些同学本来对递归就懵，回溯法中递归还要嵌套for循环，可能就直接晕倒了！

如果脑洞模拟回溯搜索的过程，绝对可以让人窒息，所以需要抽象图形结构来进一步理解。

**我们在[关于回溯算法，你该了解这些！ **(opens new window)**](https://programmercarl.com/%E5%9B%9E%E6%BA%AF%E7%AE%97%E6%B3%95%E7%90%86%E8%AE%BA%E5%9F%BA%E7%A1%80.html)中说到回溯法解决的问题都可以抽象为树形结构（N叉树），用树形结构来理解回溯就容易多了**。

那么我把组合问题抽象为如下树形结构：

https://code-thinking-1253855093.file.myqcloud.com/pics/20201123195223940.png（图像链接）

可以看出这棵树，一开始集合是 1，2，3，4， 从左向右取数，取过的数，不再重复取。

第一次取1，集合变为2，3，4 ，因为k为2，我们只需要再取一个数就可以了，分别取2，3，4，得到集合[1,2] [1,3] [1,4]，以此类推。

**每次从集合中选取元素，可选择的范围随着选择的进行而收缩，调整可选择的范围**。

**图中可以发现n相当于树的宽度，k相当于树的深度**。

那么如何在这个树上遍历，然后收集到我们要的结果集呢？

**图中每次搜索到了叶子节点，我们就找到了一个结果**。

相当于只需要把达到叶子节点的结果收集起来，就可以求得 n个数中k个数的组合集合。

在[关于回溯算法，你该了解这些！ **(opens new window)**](https://programmercarl.com/%E5%9B%9E%E6%BA%AF%E7%AE%97%E6%B3%95%E7%90%86%E8%AE%BA%E5%9F%BA%E7%A1%80.html)中我们提到了回溯法三部曲，那么我们按照回溯法三部曲开始正式讲解代码了。

### 回溯法三部曲

* 递归函数的返回值以及参数

在这里要定义两个全局变量，一个用来存放符合条件单一结果，一个用来存放符合条件结果的集合。

代码如下：

```cpp
vector<vector<int>> result; // 存放符合条件结果的集合
vector<int> path; // 用来存放符合条件结果
```

其实不定义这两个全局变量也是可以的，把这两个变量放进递归函数的参数里，但函数里参数太多影响可读性，所以我定义全局变量了。

函数里一定有两个参数，既然是集合n里面取k个数，那么n和k是两个int型的参数。

然后还需要一个参数，为int型变量startIndex，这个参数用来记录本层递归的中，集合从哪里开始遍历（集合就是[1,...,n] ）。

为什么要有这个startIndex呢？

**建议在[77.组合视频讲解 **(opens new window)**](https://www.bilibili.com/video/BV1ti4y1L7cv)中，07:36的时候开始听，startIndex 就是防止出现重复的组合**。

从下图中红线部分可以看出，在集合[1,2,3,4]取1之后，下一层递归，就要在[2,3,4]中取数了，那么下一层递归如何知道从[2,3,4]中取数呢，靠的就是startIndex。

https://code-thinking-1253855093.file.myqcloud.com/pics/20201123195328976.png（图像链接）

所以需要startIndex来记录下一层递归，搜索的起始位置。

那么整体代码如下：

```cpp
vector<vector<int>> result; // 存放符合条件结果的集合
vector<int> path; // 用来存放符合条件单一结果
void backtracking(int n, int k, int startIndex)
```

* 回溯函数终止条件

什么时候到达所谓的叶子节点了呢？

path这个数组的大小如果达到k，说明我们找到了一个子集大小为k的组合了，在图中path存的就是根节点到叶子节点的路径。

如图红色部分：

https://code-thinking-1253855093.file.myqcloud.com/pics/20201123195407907.png（图像链接）

此时用result二维数组，把path保存起来，并终止本层递归。

所以终止条件代码如下：

```cpp
if (path.size() == k) {
    result.push_back(path);
    return;
}
```

* 单层搜索的过程

回溯法的搜索过程就是一个树型结构的遍历过程，在如下图中，可以看出for循环用来横向遍历，递归的过程是纵向遍历。

https://code-thinking-1253855093.file.myqcloud.com/pics/20201123195242899.png（图像链接）

如此我们才遍历完图中的这棵树。

for循环每次从startIndex开始遍历，然后用path保存取到的节点i。

代码如下：

```cpp
for (int i = startIndex; i <= n; i++) { // 控制树的横向遍历
    path.push_back(i); // 处理节点
    backtracking(n, k, i + 1); // 递归：控制树的纵向遍历，注意下一层搜索要从i+1开始
    path.pop_back(); // 回溯，撤销处理的节点
}
```

可以看出backtracking（递归函数）通过不断调用自己一直往深处遍历，总会遇到叶子节点，遇到了叶子节点就要返回。

backtracking的下面部分就是回溯的操作了，撤销本次处理的结果。

关键地方都讲完了，组合问题C++完整代码如下：

```cpp
class Solution {
private:
    vector<vector<int>> result; // 存放符合条件结果的集合
    vector<int> path; // 用来存放符合条件结果
    void backtracking(int n, int k, int startIndex) {
        if (path.size() == k) {
            result.push_back(path);
            return;
        }
        for (int i = startIndex; i <= n; i++) {
            path.push_back(i); // 处理节点
            backtracking(n, k, i + 1); // 递归
            path.pop_back(); // 回溯，撤销处理的节点
        }
    }
public:
    vector<vector<int>> combine(int n, int k) {
        result.clear(); // 可以不写
        path.clear();   // 可以不写
        backtracking(n, k, 1);
        return result;
    }
};
```

* 时间复杂度: O(n \* 2^n)
* 空间复杂度: O(n)

还记得我们在[关于回溯算法，你该了解这些！ **(opens new window)**](https://programmercarl.com/%E5%9B%9E%E6%BA%AF%E7%AE%97%E6%B3%95%E7%90%86%E8%AE%BA%E5%9F%BA%E7%A1%80.html)中给出的回溯法模板么？

如下：

```text
void backtracking(参数) {
    if (终止条件) {
        存放结果;
        return;
    }

    for (选择：本层集合中元素（树中节点孩子的数量就是集合的大小）) {
        处理节点;
        backtracking(路径，选择列表); // 递归
        回溯，撤销处理结果
    }
}
```

**对比一下本题的代码，是不是发现有点像！** 所以有了这个模板，就有解题的大体方向，不至于毫无头绪。

## 总结

组合问题是回溯法解决的经典问题，我们开始的时候给大家列举一个很形象的例子，就是n为100，k为50的话，直接想法就需要50层for循环。

从而引出了回溯法就是解决这种k层for循环嵌套的问题。

然后进一步把回溯法的搜索过程抽象为树形结构，可以直观的看出搜索的过程。

接着用回溯法三部曲，逐步分析了函数参数、终止条件和单层搜索的过程。

## 剪枝优化

我们说过，回溯法虽然是暴力搜索，但也有时候可以有点剪枝优化一下的。

在遍历的过程中有如下代码：

```cpp
for (int i = startIndex; i <= n; i++) {
    path.push_back(i);
    backtracking(n, k, i + 1);
    path.pop_back();
}
```

这个遍历的范围是可以剪枝优化的，怎么优化呢？

来举一个例子，n = 4，k = 4的话，那么第一层for循环的时候，从元素2开始的遍历都没有意义了。 在第二层for循环，从元素3开始的遍历都没有意义了。

这么说有点抽象，如图所示：

https://code-thinking-1253855093.file.myqcloud.com/pics/20210130194335207-20230310134409532.png（图像链接）

图中每一个节点（图中为矩形），就代表本层的一个for循环，那么每一层的for循环从第二个数开始遍历的话，都没有意义，都是无效遍历。

**所以，可以剪枝的地方就在递归中每一层的for循环所选择的起始位置**。

**如果for循环选择的起始位置之后的元素个数 已经不足 我们需要的元素个数了，那么就没有必要搜索了**。

注意代码中i，就是for循环里选择的起始位置。

```text
for (int i = startIndex; i <= n; i++) {
```

接下来看一下优化过程如下：

1. 已经选择的元素个数：path.size();
2. 还需要的元素个数为: k - path.size();
3. 在集合n中至多要从该起始位置 : n - (k - path.size()) + 1，开始遍历

为什么有个+1呢，因为包括起始位置，我们要是一个左闭的集合。

举个例子，n = 4，k = 3， 目前已经选取的元素为0（path.size为0），n - (k - 0) + 1 即 4 - ( 3 - 0) + 1 = 2。

从2开始搜索都是合理的，可以是组合[2, 3, 4]。

这里大家想不懂的话，建议也举一个例子，就知道是不是要+1了。

所以优化之后的for循环是：

```text
for (int i = startIndex; i <= n - (k - path.size()) + 1; i++) // i为本次搜索的起始位置
```

优化后整体代码如下：

```cpp
class Solution {
private:
    vector<vector<int>> result;
    vector<int> path;
    void backtracking(int n, int k, int startIndex) {
        if (path.size() == k) {
            result.push_back(path);
            return;
        }
        for (int i = startIndex; i <= n - (k - path.size()) + 1; i++) { // 优化的地方
            path.push_back(i); // 处理节点
            backtracking(n, k, i + 1);
            path.pop_back(); // 回溯，撤销处理的节点
        }
    }
public:

    vector<vector<int>> combine(int n, int k) {
        backtracking(n, k, 1);
        return result;
    }
};
```

## 剪枝总结

本篇我们针对求组合问题的回溯法代码做了剪枝优化，这个优化如果不画图的话，其实不好理解，也不好讲清楚。

所以我依然是把整个回溯过程抽象为一棵树形结构，然后可以直观的看出，剪枝究竟是剪的哪里。

## 其他语言版本

### Python

未剪枝优化

```python
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []  # 存放结果集
        self.backtracking(n, k, 1, [], result)
        return result
    def backtracking(self, n, k, startIndex, path, result):
        if len(path) == k:
            result.append(path[:])
            return
        for i in range(startIndex, n + 1):  # 需要优化的地方
            path.append(i)  # 处理节点
            self.backtracking(n, k, i + 1, path, result)
            path.pop()  # 回溯，撤销处理的节点

```

剪枝优化：

```python
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []  # 存放结果集
        self.backtracking(n, k, 1, [], result)
        return result
    def backtracking(self, n, k, startIndex, path, result):
        if len(path) == k:
            result.append(path[:])
            return
        for i in range(startIndex, n - (k - len(path)) + 2):  # 优化的地方
            path.append(i)  # 处理节点
            self.backtracking(n, k, i + 1, path, result)
            path.pop()  # 回溯，撤销处理的节点

```

# 三、77.组合优化

## 算法公开课

**[《代码随想录》算法视频公开课 **(opens new window)**](https://programmercarl.com/other/gongkaike.html)：[组合问题的剪枝操作 **(opens new window)**](https://www.bilibili.com/video/BV1wi4y157er)，相信结合视频在看本篇题解，更有助于大家对本题的理解。**

## 思路

在[回溯算法：求组合问题！ **(opens new window)**](https://programmercarl.com/0077.%E7%BB%84%E5%90%88.html)中，我们通过回溯搜索法，解决了n个数中求k个数的组合问题。

文中的回溯法是可以剪枝优化的，本篇我们继续来看一下题目77. 组合。

链接：https://leetcode.cn/problems/combinations/

**看本篇之前，需要先看**[回溯算法：求组合问题！ **(opens new window)**](https://programmercarl.com/0077.%E7%BB%84%E5%90%88.html)。

大家先回忆一下[77. 组合]给出的回溯法的代码：

```cpp
class Solution {
private:
    vector<vector<int>> result; // 存放符合条件结果的集合
    vector<int> path; // 用来存放符合条件结果
    void backtracking(int n, int k, int startIndex) {
        if (path.size() == k) {
            result.push_back(path);
            return;
        }
        for (int i = startIndex; i <= n; i++) {
            path.push_back(i); // 处理节点
            backtracking(n, k, i + 1); // 递归
            path.pop_back(); // 回溯，撤销处理的节点
        }
    }
public:
    vector<vector<int>> combine(int n, int k) {
        result.clear(); // 可以不写
        path.clear();   // 可以不写
        backtracking(n, k, 1);
        return result;
    }
};
```

## 剪枝优化

我们说过，回溯法虽然是暴力搜索，但也有时候可以有点剪枝优化一下的。

在遍历的过程中有如下代码：

```cpp
for (int i = startIndex; i <= n; i++) {
    path.push_back(i);
    backtracking(n, k, i + 1);
    path.pop_back();
}
```

这个遍历的范围是可以剪枝优化的，怎么优化呢？

来举一个例子，n = 4，k = 4的话，那么第一层for循环的时候，从元素2开始的遍历都没有意义了。 在第二层for循环，从元素3开始的遍历都没有意义了。

这么说有点抽象，如图所示：

https://code-thinking-1253855093.file.myqcloud.com/pics/20210130194335207.png（图像链接）

图中每一个节点（图中为矩形），就代表本层的一个for循环，那么每一层的for循环从第二个数开始遍历的话，都没有意义，都是无效遍历。

**所以，可以剪枝的地方就在递归中每一层的for循环所选择的起始位置**。

**如果for循环选择的起始位置之后的元素个数 已经不足 我们需要的元素个数了，那么就没有必要搜索了**。

注意代码中i，就是for循环里选择的起始位置。

```cpp
for (int i = startIndex; i <= n; i++) {
```

接下来看一下优化过程如下：

1. 已经选择的元素个数：path.size();
2. 所需需要的元素个数为: k - path.size();
3. 列表中剩余元素（n-i） >= 所需需要的元素个数（k - path.size()）
4. 在集合n中至多要从该起始位置 : i <= n - (k - path.size()) + 1，开始遍历

为什么有个+1呢，因为包括起始位置，我们要是一个左闭的集合。

举个例子，n = 4，k = 3， 目前已经选取的元素为0（path.size为0），n - (k - 0) + 1 即 4 - ( 3 - 0) + 1 = 2。

从2开始搜索都是合理的，可以是组合[2, 3, 4]。

这里大家想不懂的话，建议也举一个例子，就知道是不是要+1了。

所以优化之后的for循环是：

```cpp
for (int i = startIndex; i <= n - (k - path.size()) + 1; i++) // i为本次搜索的起始位置
```

优化后整体代码如下：

```cpp
class Solution {
private:
    vector<vector<int>> result;
    vector<int> path;
    void backtracking(int n, int k, int startIndex) {
        if (path.size() == k) {
            result.push_back(path);
            return;
        }
        for (int i = startIndex; i <= n - (k - path.size()) + 1; i++) { // 优化的地方
            path.push_back(i); // 处理节点
            backtracking(n, k, i + 1);
            path.pop_back(); // 回溯，撤销处理的节点
        }
    }
public:

    vector<vector<int>> combine(int n, int k) {
        backtracking(n, k, 1);
        return result;
    }
};
```

* 时间复杂度: O(n \* 2^n)
* 空间复杂度: O(n)

## 总结

本篇我们针对求组合问题的回溯法代码做了剪枝优化，这个优化如果不画图的话，其实不好理解，也不好讲清楚。

所以我依然是把整个回溯过程抽象为一棵树形结构，然后可以直观的看出，剪枝究竟是剪的哪里。

**就酱，学到了就帮Carl转发一下吧，让更多的同学知道这里！**

## 其他语言版本

### Python

```python
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []  # 存放结果集
        self.backtracking(n, k, 1, [], result)
        return result
    def backtracking(self, n, k, startIndex, path, result):
        if len(path) == k:
            result.append(path[:])
            return
        for i in range(startIndex, n - (k - len(path)) + 2):  # 优化的地方
            path.append(i)  # 处理节点
            self.backtracking(n, k, i + 1, path, result)
            path.pop()  # 回溯，撤销处理的节点

```


# 四、216.组合总和III

[力扣题目链接(opens new window)](https://leetcode.cn/problems/combination-sum-iii/)

找出所有相加之和为 n 的 k 个数的组合。组合中只允许含有 1 - 9 的正整数，并且每种组合中不存在重复的数字。

说明：

* 所有数字都是正整数。
* 解集不能包含重复的组合。

示例 1: 输入: k = 3, n = 7 输出: [[1,2,4]]

示例 2: 输入: k = 3, n = 9 输出: [[1,2,6], [1,3,5], [2,3,4]]

## 算法公开课

[《代码随想录》算法视频公开课 **(opens new window)**](https://programmercarl.com/other/gongkaike.html)：[和组合问题有啥区别？回溯算法如何剪枝？| LeetCode：216.组合总和III **(opens new window)**](https://www.bilibili.com/video/BV1wg411873x)，**相信结合视频再看本篇题解，更有助于大家对本题的理解**。

## 思路

本题就是在[1,2,3,4,5,6,7,8,9]这个集合中找到和为n的k个数的组合。

相对于[77. 组合 **(opens new window)**](https://programmercarl.com/0077.%E7%BB%84%E5%90%88.html)，无非就是多了一个限制，本题是要找到和为n的k个数的组合，而整个集合已经是固定的了[1,...,9]。

想到这一点了，做过[77. 组合 **(opens new window)**](https://programmercarl.com/0077.%E7%BB%84%E5%90%88.html)之后，本题是简单一些了。

本题k相当于树的深度，9（因为整个集合就是9个数）就是树的宽度。

例如 k = 2，n = 4的话，就是在集合[1,2,3,4,5,6,7,8,9]中求 k（个数） = 2, n（和） = 4的组合。

选取过程如图：

https://code-thinking-1253855093.file.myqcloud.com/pics/20201123195717975.png（图像链接）

图中，可以看出，只有最后取到集合（1，3）和为4 符合条件。

### 回溯三部曲

* **确定递归函数参数**

和[77. 组合 **(opens new window)**](https://programmercarl.com/0077.%E7%BB%84%E5%90%88.html)一样，依然需要一维数组path来存放符合条件的结果，二维数组result来存放结果集。

这里我依然定义path 和 result为全局变量。

至于为什么取名为path？从上面树形结构中，可以看出，结果其实就是一条根节点到叶子节点的路径。

```cpp
vector<vector<int>> result; // 存放结果集
vector<int> path; // 符合条件的结果
```

接下来还需要如下参数：

* targetSum（int）目标和，也就是题目中的n。
* k（int）就是题目中要求k个数的集合。
* sum（int）为已经收集的元素的总和，也就是path里元素的总和。
* startIndex（int）为下一层for循环搜索的起始位置。

所以代码如下：

```cpp
vector<vector<int>> result;
vector<int> path;
void backtracking(int targetSum, int k, int sum, int startIndex)
```

其实这里sum这个参数也可以省略，每次targetSum减去选取的元素数值，然后判断如果targetSum为0了，说明收集到符合条件的结果了，我这里为了直观便于理解，还是加一个sum参数。

还要强调一下，回溯法中递归函数参数很难一次性确定下来，一般先写逻辑，需要啥参数了，填什么参数。

* 确定终止条件

什么时候终止呢？

在上面已经说了，k其实就已经限制树的深度，因为就取k个元素，树再往下深了没有意义。

所以如果path.size() 和 k相等了，就终止。

如果此时path里收集到的元素和（sum） 和targetSum（就是题目描述的n）相同了，就用result收集当前的结果。

所以 终止代码如下：

```cpp
if (path.size() == k) {
    if (sum == targetSum) result.push_back(path);
    return; // 如果path.size() == k 但sum != targetSum 直接返回
}
```

* **单层搜索过程**

本题和[77. 组合 **(opens new window)**](https://programmercarl.com/0077.%E7%BB%84%E5%90%88.html)区别之一就是集合固定的就是9个数[1,...,9]，所以for循环固定i<=9

如图：

https://code-thinking-1253855093.file.myqcloud.com/pics/20201123195717975-20230310113546003.png（图像链接）

处理过程就是 path收集每次选取的元素，相当于树型结构里的边，sum来统计path里元素的总和。

代码如下：

```cpp
for (int i = startIndex; i <= 9; i++) {
    sum += i;
    path.push_back(i);
    backtracking(targetSum, k, sum, i + 1); // 注意i+1调整startIndex
    sum -= i; // 回溯
    path.pop_back(); // 回溯
}
```

**别忘了处理过程 和 回溯过程是一一对应的，处理有加，回溯就要有减！**

参照[关于回溯算法，你该了解这些！ **(opens new window)**](https://programmercarl.com/%E5%9B%9E%E6%BA%AF%E7%AE%97%E6%B3%95%E7%90%86%E8%AE%BA%E5%9F%BA%E7%A1%80.html)中的模板，不难写出如下C++代码：

```cpp
class Solution {
private:
    vector<vector<int>> result; // 存放结果集
    vector<int> path; // 符合条件的结果
    // targetSum：目标和，也就是题目中的n。
    // k：题目中要求k个数的集合。
    // sum：已经收集的元素的总和，也就是path里元素的总和。
    // startIndex：下一层for循环搜索的起始位置。
    void backtracking(int targetSum, int k, int sum, int startIndex) {
        if (path.size() == k) {
            if (sum == targetSum) result.push_back(path);
            return; // 如果path.size() == k 但sum != targetSum 直接返回
        }
        for (int i = startIndex; i <= 9; i++) {
            sum += i; // 处理
            path.push_back(i); // 处理
            backtracking(targetSum, k, sum, i + 1); // 注意i+1调整startIndex
            sum -= i; // 回溯
            path.pop_back(); // 回溯
        }
    }

public:
    vector<vector<int>> combinationSum3(int k, int n) {
        result.clear(); // 可以不加
        path.clear();   // 可以不加
        backtracking(n, k, 0, 1);
        return result;
    }
};
```

### 剪枝

这道题目，剪枝操作其实是很容易想到了，想必大家看上面的树形图的时候已经想到了。

如图：

https://code-thinking-1253855093.file.myqcloud.com/pics/2020112319580476.png（图像链接）

已选元素总和如果已经大于n（图中数值为4）了，那么往后遍历就没有意义了，直接剪掉。

那么剪枝的地方可以放在递归函数开始的地方，剪枝代码如下：

```cpp
if (sum > targetSum) { // 剪枝操作
    return;
}
```

当然这个剪枝也可以放在 调用递归之前，即放在这里，只不过要记得 要回溯操作给做了。

```cpp
for (int i = startIndex; i <= 9 - (k - path.size()) + 1; i++) { // 剪枝
    sum += i; // 处理
    path.push_back(i); // 处理
    if (sum > targetSum) { // 剪枝操作
        sum -= i; // 剪枝之前先把回溯做了
        path.pop_back(); // 剪枝之前先把回溯做了
        return;
    }
    backtracking(targetSum, k, sum, i + 1); // 注意i+1调整startIndex
    sum -= i; // 回溯
    path.pop_back(); // 回溯
}
```

和[回溯算法：组合问题再剪剪枝 **(opens new window)**](https://programmercarl.com/0077.%E7%BB%84%E5%90%88%E4%BC%98%E5%8C%96.html)一样，for循环的范围也可以剪枝，i <= 9 - (k - path.size()) + 1就可以了。

最后C++代码如下：

```cpp
class Solution {
private:
    vector<vector<int>> result; // 存放结果集
    vector<int> path; // 符合条件的结果
    void backtracking(int targetSum, int k, int sum, int startIndex) {
        if (sum > targetSum) { // 剪枝操作
            return; 
        }
        if (path.size() == k) {
            if (sum == targetSum) result.push_back(path);
            return; // 如果path.size() == k 但sum != targetSum 直接返回
        }
        for (int i = startIndex; i <= 9 - (k - path.size()) + 1; i++) { // 剪枝
            sum += i; // 处理
            path.push_back(i); // 处理
            backtracking(targetSum, k, sum, i + 1); // 注意i+1调整startIndex
            sum -= i; // 回溯
            path.pop_back(); // 回溯
        }
    }

public:
    vector<vector<int>> combinationSum3(int k, int n) {
        result.clear(); // 可以不加
        path.clear();   // 可以不加
        backtracking(n, k, 0, 1);
        return result;
    }
};
```

* 时间复杂度: O(n \* 2^n)
* 空间复杂度: O(n)

## 总结

开篇就介绍了本题与[77.组合 **(opens new window)**](https://programmercarl.com/0077.%E7%BB%84%E5%90%88.html)的区别，相对来说加了元素总和的限制，如果做完[77.组合 **(opens new window)**](https://programmercarl.com/0077.%E7%BB%84%E5%90%88.html)再做本题在合适不过。

分析完区别，依然把问题抽象为树形结构，按照回溯三部曲进行讲解，最后给出剪枝的优化。

相信做完本题，大家对组合问题应该有初步了解了。

## 其他语言版本

### Python

```py
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []  # 存放结果集
        self.backtracking(n, k, 0, 1, [], result)
        return result

    def backtracking(self, targetSum, k, currentSum, startIndex, path, result):
        if currentSum > targetSum:  # 剪枝操作
            return  # 如果path的长度等于k但currentSum不等于targetSum，则直接返回
        if len(path) == k:
            if currentSum == targetSum:
                result.append(path[:])
            return
        for i in range(startIndex, 9 - (k - len(path)) + 2):  # 剪枝
            currentSum += i  # 处理
            path.append(i)  # 处理
            self.backtracking(targetSum, k, currentSum, i + 1, path, result)  # 注意i+1调整startIndex
            currentSum -= i  # 回溯
            path.pop()  # 回溯

```


# 五、17.电话号码的字母组合

[力扣题目链接(opens new window)](https://leetcode.cn/problems/letter-combinations-of-a-phone-number/)

给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。

给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。

https://code-thinking-1253855093.file.myqcloud.com/pics/2020102916424043.png（图像链接）

示例:

* 输入："23"
* 输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

说明：尽管上面的答案是按字典序排列的，但是你可以任意选择答案输出的顺序。

## 算法公开课

[《代码随想录》算法视频公开课 **(opens new window)**](https://programmercarl.com/other/gongkaike.html)：：[还得用回溯算法！| LeetCode：17.电话号码的字母组合 **(opens new window)**](https://www.bilibili.com/video/BV1yV4y1V7Ug)，**相信结合视频再看本篇题解，更有助于大家对本题的理解**。

## 思路

从示例上来说，输入"23"，最直接的想法就是两层for循环遍历了吧，正好把组合的情况都输出了。

如果输入"233"呢，那么就三层for循环，如果"2333"呢，就四层for循环.......

大家应该感觉出和[77.组合 **(opens new window)**](https://programmercarl.com/0077.%E7%BB%84%E5%90%88.html)遇到的一样的问题，就是这for循环的层数如何写出来，此时又是回溯法登场的时候了。

理解本题后，要解决如下三个问题：

1. 数字和字母如何映射
2. 两个字母就两个for循环，三个字符我就三个for循环，以此类推，然后发现代码根本写不出来
3. 输入1 \* #按键等等异常情况

### 数字和字母如何映射

可以使用map或者定义一个二维数组，例如：string letterMap[10]，来做映射，我这里定义一个二维数组，代码如下：

```cpp
const string letterMap[10] = {
    "", // 0
    "", // 1
    "abc", // 2
    "def", // 3
    "ghi", // 4
    "jkl", // 5
    "mno", // 6
    "pqrs", // 7
    "tuv", // 8
    "wxyz", // 9
};
```

### 回溯法来解决n个for循环的问题

对于回溯法还不了解的同学看这篇：[关于回溯算法，你该了解这些！(opens new window)](https://programmercarl.com/%E5%9B%9E%E6%BA%AF%E7%AE%97%E6%B3%95%E7%90%86%E8%AE%BA%E5%9F%BA%E7%A1%80.html)

例如：输入："23"，抽象为树形结构，如图所示：

https://code-thinking-1253855093.file.myqcloud.com/pics/20201123200304469.png（图像链接）

图中可以看出遍历的深度，就是输入"23"的长度，而叶子节点就是我们要收集的结果，输出["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]。

回溯三部曲：

* 确定回溯函数参数

首先需要一个字符串s来收集叶子节点的结果，然后用一个字符串数组result保存起来，这两个变量我依然定义为全局。

再来看参数，参数指定是有题目中给的string digits，然后还要有一个参数就是int型的index。

注意这个index可不是 [77.组合 **(opens new window)**](https://programmercarl.com/0077.%E7%BB%84%E5%90%88.html)和[216.组合总和III **(opens new window)**](https://programmercarl.com/0216.%E7%BB%84%E5%90%88%E6%80%BB%E5%92%8CIII.html)中的startIndex了。

这个index是记录遍历第几个数字了，就是用来遍历digits的（题目中给出数字字符串），同时index也表示树的深度。

代码如下：

```cpp
vector<string> result;
string s;
void backtracking(const string& digits, int index)
```

* 确定终止条件

例如输入用例"23"，两个数字，那么根节点往下递归两层就可以了，叶子节点就是要收集的结果集。

那么终止条件就是如果index 等于 输入的数字个数（digits.size）了（本来index就是用来遍历digits的）。

然后收集结果，结束本层递归。

代码如下：

```cpp
if (index == digits.size()) {
    result.push_back(s);
    return;
}
```

* 确定单层遍历逻辑

首先要取index指向的数字，并找到对应的字符集（手机键盘的字符集）。

然后for循环来处理这个字符集，代码如下：

```cpp
int digit = digits[index] - '0';        // 将index指向的数字转为int
string letters = letterMap[digit];      // 取数字对应的字符集
for (int i = 0; i < letters.size(); i++) {
    s.push_back(letters[i]);            // 处理
    backtracking(digits, index + 1);    // 递归，注意index+1，一下层要处理下一个数字了
    s.pop_back();                       // 回溯
}
```

**注意这里for循环，可不像是在[回溯算法：求组合问题！ **(opens new window)**](https://programmercarl.com/0077.%E7%BB%84%E5%90%88.html)和[回溯算法：求组合总和！ **(opens new window)**](https://programmercarl.com/0216.%E7%BB%84%E5%90%88%E6%80%BB%E5%92%8CIII.html)中从startIndex开始遍历的**。

**因为本题每一个数字代表的是不同集合，也就是求不同集合之间的组合，而[77. 组合 **(opens new window)**](https://programmercarl.com/0077.%E7%BB%84%E5%90%88.html)和[216.组合总和III **(opens new window)**](https://programmercarl.com/0216.%E7%BB%84%E5%90%88%E6%80%BB%E5%92%8CIII.html)都是求同一个集合中的组合！**

注意：输入1 \* #按键等等异常情况

代码中最好考虑这些异常情况，但题目的测试数据中应该没有异常情况的数据，所以我就没有加了。

**但是要知道会有这些异常，如果是现场面试中，一定要考虑到！**

关键地方都讲完了，按照[关于回溯算法，你该了解这些！ **(opens new window)**](https://programmercarl.com/%E5%9B%9E%E6%BA%AF%E7%AE%97%E6%B3%95%E7%90%86%E8%AE%BA%E5%9F%BA%E7%A1%80.html)中的回溯法模板，不难写出如下C++代码：

```cpp
// 版本一
class Solution {
private:
    const string letterMap[10] = {
        "", // 0
        "", // 1
        "abc", // 2
        "def", // 3
        "ghi", // 4
        "jkl", // 5
        "mno", // 6
        "pqrs", // 7
        "tuv", // 8
        "wxyz", // 9
    };
public:
    vector<string> result;
    string s;
    void backtracking(const string& digits, int index) {
        if (index == digits.size()) {
            result.push_back(s);
            return;
        }
        int digit = digits[index] - '0';        // 将index指向的数字转为int
        string letters = letterMap[digit];      // 取数字对应的字符集
        for (int i = 0; i < letters.size(); i++) {
            s.push_back(letters[i]);            // 处理
            backtracking(digits, index + 1);    // 递归，注意index+1，一下层要处理下一个数字了
            s.pop_back();                       // 回溯
        }
    }
    vector<string> letterCombinations(string digits) {
        s.clear();
        result.clear();
        if (digits.size() == 0) {
            return result;
        }
        backtracking(digits, 0);
        return result;
    }
};
```

* 时间复杂度: O(3^m \* 4^n)，其中 m 是对应三个字母的数字个数，n 是对应四个字母的数字个数
* 空间复杂度: O(3^m \* 4^n)

一些写法，是把回溯的过程放在递归函数里了，例如如下代码，我可以写成这样：（注意注释中不一样的地方）

```cpp
// 版本二
class Solution {
private:
        const string letterMap[10] = {
            "", // 0
            "", // 1
            "abc", // 2
            "def", // 3
            "ghi", // 4
            "jkl", // 5
            "mno", // 6
            "pqrs", // 7
            "tuv", // 8
            "wxyz", // 9
        };
public:
    vector<string> result;
    void getCombinations(const string& digits, int index, const string& s) { // 注意参数的不同
        if (index == digits.size()) {
            result.push_back(s);
            return;
        }
        int digit = digits[index] - '0';
        string letters = letterMap[digit];
        for (int i = 0; i < letters.size(); i++) {
            getCombinations(digits, index + 1, s + letters[i]);  // 注意这里的不同
        }
    }
    vector<string> letterCombinations(string digits) {
        result.clear();
        if (digits.size() == 0) {
            return result;
        }
        getCombinations(digits, 0, "");
        return result;

    }
};
```

我不建议把回溯藏在递归的参数里这种写法，很不直观，我在[二叉树：以为使用了递归，其实还隐藏着回溯 **(opens new window)**](https://programmercarl.com/%E4%BA%8C%E5%8F%89%E6%A0%91%E4%B8%AD%E9%80%92%E5%BD%92%E5%B8%A6%E7%9D%80%E5%9B%9E%E6%BA%AF.html)这篇文章中也深度分析了，回溯隐藏在了哪里。

所以大家可以按照版本一来写就可以了。

## 总结

本篇将题目的三个要点一一列出，并重点强调了和前面讲解过的[77. 组合 **(opens new window)**](https://programmercarl.com/0077.%E7%BB%84%E5%90%88.html)和[216.组合总和III **(opens new window)**](https://programmercarl.com/0216.%E7%BB%84%E5%90%88%E6%80%BB%E5%92%8CIII.html)的区别，本题是多个集合求组合，所以在回溯的搜索过程中，都有一些细节需要注意的。

其实本题不算难，但也处处是细节，大家还要自己亲自动手写一写。

## 其他语言版本

### Python

回溯

```python
class Solution:
    def __init__(self):
        self.letterMap = [
            "",     # 0
            "",     # 1
            "abc",  # 2
            "def",  # 3
            "ghi",  # 4
            "jkl",  # 5
            "mno",  # 6
            "pqrs", # 7
            "tuv",  # 8
            "wxyz"  # 9
        ]
        self.result = []
        self.s = ""
  
    def backtracking(self, digits, index):
        if index == len(digits):
            self.result.append(self.s)
            return
        digit = int(digits[index])    # 将索引处的数字转换为整数
        letters = self.letterMap[digit]    # 获取对应的字符集
        for i in range(len(letters)):
            self.s += letters[i]    # 处理字符
            self.backtracking(digits, index + 1)    # 递归调用，注意索引加1，处理下一个数字
            self.s = self.s[:-1]    # 回溯，删除最后添加的字符
  
    def letterCombinations(self, digits):
        if len(digits) == 0:
            return self.result
        self.backtracking(digits, 0)
        return self.result

```

回溯精简（版本一）

```python
class Solution:
    def __init__(self):
        self.letterMap = [
            "",     # 0
            "",     # 1
            "abc",  # 2
            "def",  # 3
            "ghi",  # 4
            "jkl",  # 5
            "mno",  # 6
            "pqrs", # 7
            "tuv",  # 8
            "wxyz"  # 9
        ]
        self.result = []
  
    def getCombinations(self, digits, index, s):
        if index == len(digits):
            self.result.append(s)
            return
        digit = int(digits[index])
        letters = self.letterMap[digit]
        for letter in letters:
            self.getCombinations(digits, index + 1, s + letter)
  
    def letterCombinations(self, digits):
        if len(digits) == 0:
            return self.result
        self.getCombinations(digits, 0, "")
        return self.result

```

回溯精简（版本二）

```python
class Solution:
    def __init__(self):
        self.letterMap = [
            "",     # 0
            "",     # 1
            "abc",  # 2
            "def",  # 3
            "ghi",  # 4
            "jkl",  # 5
            "mno",  # 6
            "pqrs", # 7
            "tuv",  # 8
            "wxyz"  # 9
        ]
  
    def getCombinations(self, digits, index, s, result):
        if index == len(digits):
            result.append(s)
            return
        digit = int(digits[index])
        letters = self.letterMap[digit]
        for letter in letters:
            self.getCombinations(digits, index + 1, s + letter, result)
  
    def letterCombinations(self, digits):
        result = []
        if len(digits) == 0:
            return result
        self.getCombinations(digits, 0, "", result)
        return result


```

回溯优化使用列表

```python
class Solution:
    def __init__(self):
        self.letterMap = [
            "",     # 0
            "",     # 1
            "abc",  # 2
            "def",  # 3
            "ghi",  # 4
            "jkl",  # 5
            "mno",  # 6
            "pqrs", # 7
            "tuv",  # 8
            "wxyz"  # 9
        ]
  
    def getCombinations(self, digits, index, path, result):
        if index == len(digits):
            result.append(''.join(path))
            return
        digit = int(digits[index])
        letters = self.letterMap[digit]
        for letter in letters:
            path.append(letter)
            self.getCombinations(digits, index + 1, path, result)
            path.pop()
  
    def letterCombinations(self, digits):
        result = []
        if len(digits) == 0:
            return result
        self.getCombinations(digits, 0, [], result)
        return result



```

# 六、本周小结！（回溯算法系列一）

## 周一

本周我们正式开始了回溯算法系列，那么首先当然是概述。

在[关于回溯算法，你该了解这些！ **(opens new window)**](https://programmercarl.com/%E5%9B%9E%E6%BA%AF%E7%AE%97%E6%B3%95%E7%90%86%E8%AE%BA%E5%9F%BA%E7%A1%80.html)中介绍了什么是回溯，回溯法的效率，回溯法解决的问题以及回溯法模板。

**回溯是递归的副产品，只要有递归就会有回溯**。

回溯法就是暴力搜索，并不是什么高效的算法，最多在剪枝一下。

回溯算法能解决如下问题：

* 组合问题：N个数里面按一定规则找出k个数的集合
* 排列问题：N个数按一定规则全排列，有几种排列方式
* 切割问题：一个字符串按一定规则有几种切割方式
* 子集问题：一个N个数的集合里有多少符合条件的子集
* 棋盘问题：N皇后，解数独等等

是不是感觉回溯算法有点厉害了。

回溯法确实不好理解，所以需要把回溯法抽象为一个图形来理解就容易多了，每一道回溯法的题目都可以抽象为树形结构。

针对很多同学都写不好回溯，我在[关于回溯算法，你该了解这些！ **(opens new window)**](https://programmercarl.com/%E5%9B%9E%E6%BA%AF%E7%AE%97%E6%B3%95%E7%90%86%E8%AE%BA%E5%9F%BA%E7%A1%80.html)用回溯三部曲，分析了回溯算法，并给出了回溯法的模板。

这个模板会伴随整个回溯法系列！

## 周二

在[回溯算法：求组合问题！ **(opens new window)**](https://programmercarl.com/0077.%E7%BB%84%E5%90%88.html)中，我们开始用回溯法解决第一道题目，组合问题。

我在文中开始的时候给大家列举k层for循环例子，进而得出都是同样是暴力解法，为什么要用回溯法。

**此时大家应该深有体会回溯法的魅力，用递归控制for循环嵌套的数量！**

本题我把回溯问题抽象为树形结构，可以直观的看出其搜索的过程：**for循环横向遍历，递归纵向遍历，回溯不断调整结果集**。

## 周三

针对[回溯算法：求组合问题！ **(opens new window)**](https://programmercarl.com/0077.%E7%BB%84%E5%90%88.html)还可以做剪枝的操作。

在[回溯算法：组合问题再剪剪枝 **(opens new window)**](https://programmercarl.com/0077.%E7%BB%84%E5%90%88%E4%BC%98%E5%8C%96.html)中把回溯法代码做了剪枝优化，在文中我依然把问题抽象为一个树形结构，大家可以一目了然剪的究竟是哪里。

**剪枝精髓是：for循环在寻找起点的时候要有一个范围，如果这个起点到集合终止之间的元素已经不够 题目要求的k个元素了，就没有必要搜索了**。

## 周四

在[回溯算法：求组合总和！ **(opens new window)**](https://programmercarl.com/0216.%E7%BB%84%E5%90%88%E6%80%BB%E5%92%8CIII.html)中，相当于 [回溯算法：求组合问题！ **(opens new window)**](https://programmercarl.com/0077.%E7%BB%84%E5%90%88.html)加了一个元素总和的限制。

整体思路还是一样的，本题的剪枝会好想一些，即：**已选元素总和如果已经大于n（题中要求的和）了，那么往后遍历就没有意义了，直接剪掉**。

在本题中，依然还可以有一个剪枝，就是[回溯算法：组合问题再剪剪枝 **(opens new window)**](https://programmercarl.com/0077.%E7%BB%84%E5%90%88%E4%BC%98%E5%8C%96.html)中提到的，对for循环选择的起始范围的剪枝。

所以，剪枝的代码，可以把for循环，加上 `i <= 9 - (k - path.size()) + 1` 的限制！

组合总和问题还有一些花样，下周还会介绍到。

## 周五

在[回溯算法：电话号码的字母组合 **(opens new window)**](https://programmercarl.com/0017.%E7%94%B5%E8%AF%9D%E5%8F%B7%E7%A0%81%E7%9A%84%E5%AD%97%E6%AF%8D%E7%BB%84%E5%90%88.html)中，开始用多个集合来求组合，还是熟悉的模板题目，但是有一些细节。

例如这里for循环，可不像是在 [回溯算法：求组合问题！ **(opens new window)**](https://programmercarl.com/0077.%E7%BB%84%E5%90%88.html)和[回溯算法：求组合总和！ **(opens new window)**](https://programmercarl.com/0216.%E7%BB%84%E5%90%88%E6%80%BB%E5%92%8CIII.html)中从startIndex开始遍历的。

**因为本题每一个数字代表的是不同集合，也就是求不同集合之间的组合，而[回溯算法：求组合问题！ **(opens new window)**](https://programmercarl.com/0077.%E7%BB%84%E5%90%88.html)和[回溯算法：求组合总和！ **(opens new window)**](https://programmercarl.com/0216.%E7%BB%84%E5%90%88%E6%80%BB%E5%92%8CIII.html)都是是求同一个集合中的组合！**

如果大家在现场面试的时候，一定要注意各种输入异常的情况，例如本题输入1 \* #按键。

其实本题不算难，但也处处是细节，还是要反复琢磨。

## 周六

因为之前链表系列没有写总结，虽然链表系列已经是两个月前的事情，但还是有必要补一下。

所以给出[链表：总结篇！ **(opens new window)**](https://programmercarl.com/%E9%93%BE%E8%A1%A8%E6%80%BB%E7%BB%93%E7%AF%87.html)，这里对之前链表理论基础和经典题目进行了总结。

同时对[链表：环找到了，那入口呢？ **(opens new window)**](https://programmercarl.com/0142.%E7%8E%AF%E5%BD%A2%E9%93%BE%E8%A1%A8II.html)中求环入口的问题又进行了补充证明，可以说把环形链表的方方面面都讲的很通透了，大家如果没有做过环形链表的题目一定要去做一做。

## 总结

相信通过这一周对回溯法的学习，大家已经掌握其题本套路了，也不会对回溯法那么畏惧了。

回溯法抽象为树形结构后，其遍历过程就是：**for循环横向遍历，递归纵向遍历，回溯不断调整结果集**。

这个是我做了很多回溯的题目，不断摸索其规律才总结出来的。

对于回溯法的整体框架，网上搜的文章这块一般都说不清楚，按照天上掉下来的代码对着讲解，不知道究竟是怎么来的，也不知道为什么要这么写。

所以，录友们刚开始学回溯法，起跑姿势就很标准了。

下周依然是回溯法，难度又要上升一个台阶了。

最后祝录友们周末愉快！

**如果感觉「代码随想录」不错，就分享给身边的同学朋友吧，一起来学习算法！**

---

* 微信：[程序员Carl(opens new window)](https://mp.weixin.qq.com/s/b66DFkOp8OOxdZC_xLZxfw)
* B站：[代码随想录(opens new window)](https://space.bilibili.com/525438321)
* 知识星球：[代码随想录](https://mp.weixin.qq.com/s/QVF6upVMSbgvZy8lHZS3CQ)


# 七、39. 组合总和

[力扣题目链接(opens new window)](https://leetcode.cn/problems/combination-sum/)

给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的数字可以无限制重复被选取。

说明：

* 所有数字（包括 target）都是正整数。
* 解集不能包含重复的组合。

示例 1：

* 输入：candidates = [2,3,6,7], target = 7,
* 所求解集为： [ [7], [2,2,3] ]

示例 2：

* 输入：candidates = [2,3,5], target = 8,
* 所求解集为： [ [2,2,2,2], [2,3,3], [3,5] ]

## 算法公开课

**[《代码随想录》算法视频公开课 **(opens new window)**](https://programmercarl.com/other/gongkaike.html)：[Leetcode:39. 组合总和讲解 **(opens new window)**](https://www.bilibili.com/video/BV1KT4y1M7HJ)，相信结合视频再看本篇题解，更有助于大家对本题的理解**。

## 思路

题目中的**无限制重复被选取，吓得我赶紧想想 出现0 可咋办**，然后看到下面提示：1 <= candidates[i] <= 200，我就放心了。

本题和[77.组合 **(opens new window)**](https://programmercarl.com/0077.%E7%BB%84%E5%90%88.html)，[216.组合总和III **(opens new window)**](https://programmercarl.com/0216.%E7%BB%84%E5%90%88%E6%80%BB%E5%92%8CIII.html)的区别是：本题没有数量要求，可以无限重复，但是有总和的限制，所以间接的也是有个数的限制。

本题搜索的过程抽象成树形结构如下：

![39.组合总和](https://code-thinking-1253855093.file.myqcloud.com/pics/20201223170730367.png) 注意图中叶子节点的返回条件，因为本题没有组合数量要求，仅仅是总和的限制，所以递归没有层数的限制，只要选取的元素总和超过target，就返回！

而在[77.组合 **(opens new window)**](https://programmercarl.com/0077.%E7%BB%84%E5%90%88.html)和[216.组合总和III **(opens new window)**](https://programmercarl.com/0216.%E7%BB%84%E5%90%88%E6%80%BB%E5%92%8CIII.html)中都可以知道要递归K层，因为要取k个元素的组合。

### 回溯三部曲

* 递归函数参数

这里依然是定义两个全局变量，二维数组result存放结果集，数组path存放符合条件的结果。（这两个变量可以作为函数参数传入）

首先是题目中给出的参数，集合candidates, 和目标值target。

此外我还定义了int型的sum变量来统计单一结果path里的总和，其实这个sum也可以不用，用target做相应的减法就可以了，最后如何target==0就说明找到符合的结果了，但为了代码逻辑清晰，我依然用了sum。

**本题还需要startIndex来控制for循环的起始位置，对于组合问题，什么时候需要startIndex呢？**

我举过例子，如果是一个集合来求组合的话，就需要startIndex，例如：[77.组合 **(opens new window)**](https://programmercarl.com/0077.%E7%BB%84%E5%90%88.html)，[216.组合总和III **(opens new window)**](https://programmercarl.com/0216.%E7%BB%84%E5%90%88%E6%80%BB%E5%92%8CIII.html)。

如果是多个集合取组合，各个集合之间相互不影响，那么就不用startIndex，例如：[17.电话号码的字母组合(opens new window)](https://programmercarl.com/0017.%E7%94%B5%E8%AF%9D%E5%8F%B7%E7%A0%81%E7%9A%84%E5%AD%97%E6%AF%8D%E7%BB%84%E5%90%88.html)

**注意以上我只是说求组合的情况，如果是排列问题，又是另一套分析的套路，后面我在讲解排列的时候会重点介绍**。

代码如下：

```cpp
vector<vector<int>> result;
vector<int> path;
void backtracking(vector<int>& candidates, int target, int sum, int startIndex)
```

* 递归终止条件

在如下树形结构中：

https://code-thinking-1253855093.file.myqcloud.com/pics/20201223170730367-20230310135337214.png（图像链接）

从叶子节点可以清晰看到，终止只有两种情况，sum大于target和sum等于target。

sum等于target的时候，需要收集结果，代码如下：

```cpp
if (sum > target) {
    return;
}
if (sum == target) {
    result.push_back(path);
    return;
}
```

* 单层搜索的逻辑

单层for循环依然是从startIndex开始，搜索candidates集合。

**注意本题和[77.组合 **(opens new window)**](https://programmercarl.com/0077.%E7%BB%84%E5%90%88.html)、[216.组合总和III **(opens new window)**](https://programmercarl.com/0216.%E7%BB%84%E5%90%88%E6%80%BB%E5%92%8CIII.html)的一个区别是：本题元素为可重复选取的**。

如何重复选取呢，看代码，注释部分：

```cpp
for (int i = startIndex; i < candidates.size(); i++) {
    sum += candidates[i];
    path.push_back(candidates[i]);
    backtracking(candidates, target, sum, i); // 关键点:不用i+1了，表示可以重复读取当前的数
    sum -= candidates[i];   // 回溯
    path.pop_back();        // 回溯
}
```

按照[关于回溯算法，你该了解这些！ **(opens new window)**](https://programmercarl.com/%E5%9B%9E%E6%BA%AF%E7%AE%97%E6%B3%95%E7%90%86%E8%AE%BA%E5%9F%BA%E7%A1%80.html)中给出的模板，不难写出如下C++完整代码：

```cpp
// 版本一
class Solution {
private:
    vector<vector<int>> result;
    vector<int> path;
    void backtracking(vector<int>& candidates, int target, int sum, int startIndex) {
        if (sum > target) {
            return;
        }
        if (sum == target) {
            result.push_back(path);
            return;
        }

        for (int i = startIndex; i < candidates.size(); i++) {
            sum += candidates[i];
            path.push_back(candidates[i]);
            backtracking(candidates, target, sum, i); // 不用i+1了，表示可以重复读取当前的数
            sum -= candidates[i];
            path.pop_back();
        }
    }
public:
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        result.clear();
        path.clear();
        backtracking(candidates, target, 0, 0);
        return result;
    }
};
```

### 剪枝优化

在这个树形结构中：

https://code-thinking-1253855093.file.myqcloud.com/pics/20201223170730367-20230310135342472.png（图像链接）

以及上面的版本一的代码大家可以看到，对于sum已经大于target的情况，其实是依然进入了下一层递归，只是下一层递归结束判断的时候，会判断sum > target的话就返回。

其实如果已经知道下一层的sum会大于target，就没有必要进入下一层递归了。

那么可以在for循环的搜索范围上做做文章了。

**对总集合排序之后，如果下一层的sum（就是本层的 sum + candidates[i]）已经大于target，就可以结束本轮for循环的遍历**。

如图：

https://code-thinking-1253855093.file.myqcloud.com/pics/20201223170809182.png（图像链接）

for循环剪枝代码如下：

```text
for (int i = startIndex; i < candidates.size() && sum + candidates[i] <= target; i++)
```

整体代码如下：（注意注释的部分）

```cpp
class Solution {
private:
    vector<vector<int>> result;
    vector<int> path;
    void backtracking(vector<int>& candidates, int target, int sum, int startIndex) {
        if (sum == target) {
            result.push_back(path);
            return;
        }

        // 如果 sum + candidates[i] > target 就终止遍历
        for (int i = startIndex; i < candidates.size() && sum + candidates[i] <= target; i++) {
            sum += candidates[i];
            path.push_back(candidates[i]);
            backtracking(candidates, target, sum, i);
            sum -= candidates[i];
            path.pop_back();

        }
    }
public:
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        result.clear();
        path.clear();
        sort(candidates.begin(), candidates.end()); // 需要排序
        backtracking(candidates, target, 0, 0);
        return result;
    }
};
```

* 时间复杂度: O(n \* 2^n)，注意这只是复杂度的上界，因为剪枝的存在，真实的时间复杂度远小于此
* 空间复杂度: O(target)

## 总结

本题和我们之前讲过的[77.组合 **(opens new window)**](https://programmercarl.com/0077.%E7%BB%84%E5%90%88.html)、[216.组合总和III **(opens new window)**](https://programmercarl.com/0216.%E7%BB%84%E5%90%88%E6%80%BB%E5%92%8CIII.html)有两点不同：

* 组合没有数量要求
* 元素可无限重复选取

针对这两个问题，我都做了详细的分析。

并且给出了对于组合问题，什么时候用startIndex，什么时候不用，并用[17.电话号码的字母组合 **(opens new window)**](https://programmercarl.com/0017.%E7%94%B5%E8%AF%9D%E5%8F%B7%E7%A0%81%E7%9A%84%E5%AD%97%E6%AF%8D%E7%BB%84%E5%90%88.html)做了对比。

最后还给出了本题的剪枝优化，这个优化如果是初学者的话并不容易想到。

**在求和问题中，排序之后加剪枝是常见的套路！**

可以看出我写的文章都会大量引用之前的文章，就是要不断作对比，分析其差异，然后给出代码解决的方法，这样才能彻底理解题目的本质与难点。

## 其他语言版本

### Python

回溯（版本一）

```python
class Solution:

    def backtracking(self, candidates, target, total, startIndex, path, result):
        if total > target:
            return
        if total == target:
            result.append(path[:])
            return

        for i in range(startIndex, len(candidates)):
            total += candidates[i]
            path.append(candidates[i])
            self.backtracking(candidates, target, total, i, path, result)  # 不用i+1了，表示可以重复读取当前的数
            total -= candidates[i]
            path.pop()

    def combinationSum(self, candidates, target):
        result = []
        self.backtracking(candidates, target, 0, 0, [], result)
        return result

```

回溯剪枝（版本一）

```python
class Solution:

    def backtracking(self, candidates, target, total, startIndex, path, result):
        if total == target:
            result.append(path[:])
            return

        for i in range(startIndex, len(candidates)):
            if total + candidates[i] > target:
                break
            total += candidates[i]
            path.append(candidates[i])
            self.backtracking(candidates, target, total, i, path, result)
            total -= candidates[i]
            path.pop()

    def combinationSum(self, candidates, target):
        result = []
        candidates.sort()  # 需要排序
        self.backtracking(candidates, target, 0, 0, [], result)
        return result

```

回溯（版本二）

```python
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result =[]
        self.backtracking(candidates, target, 0, [], result)
        return result
    def backtracking(self, candidates, target, startIndex, path, result):
        if target == 0:
            result.append(path[:])
            return
        if target < 0:
            return
        for i in range(startIndex, len(candidates)):
            path.append(candidates[i])
            self.backtracking(candidates, target - candidates[i], i, path, result)
            path.pop()

```

回溯剪枝（版本二）

```python
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result =[]
        candidates.sort()
        self.backtracking(candidates, target, 0, [], result)
        return result
    def backtracking(self, candidates, target, startIndex, path, result):
        if target == 0:
            result.append(path[:])
            return

        for i in range(startIndex, len(candidates)):
            if target - candidates[i]  < 0:
                break
            path.append(candidates[i])
            self.backtracking(candidates, target - candidates[i], i, path, result)
            path.pop()

```

