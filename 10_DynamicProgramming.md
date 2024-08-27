## 算法公开课

[《代码随想录》算法视频公开课 **(opens new window)**](https://programmercarl.com/other/gongkaike.html)：[动态规划理论基础 **(opens new window)**](https://www.bilibili.com/video/BV13Q4y197Wg)，**相信结合视频再看本篇题解，更有助于大家对本题的理解**。

## 一、什么是动态规划

动态规划，英文：Dynamic Programming，简称DP，如果某一问题有很多重叠子问题，使用动态规划是最有效的。

所以动态规划中每一个状态一定是由上一个状态推导出来的，**这一点就区分于贪心**，贪心没有状态推导，而是从局部直接选最优的，

在[关于贪心算法，你该了解这些！ **(opens new window)**](https://programmercarl.com/%E8%B4%AA%E5%BF%83%E7%AE%97%E6%B3%95%E7%90%86%E8%AE%BA%E5%9F%BA%E7%A1%80.html)中我举了一个背包问题的例子。

例如：有N件物品和一个最多能背重量为W 的背包。第i件物品的重量是weight[i]，得到的价值是value[i] 。**每件物品只能用一次**，求解将哪些物品装入背包里物品价值总和最大。

动态规划中dp[j]是由dp[j-weight[i]]推导出来的，然后取max(dp[j], dp[j - weight[i]] + value[i])。

但如果是贪心呢，每次拿物品选一个最大的或者最小的就完事了，和上一个状态没有关系。

所以贪心解决不了动态规划的问题。

**其实大家也不用死扣动规和贪心的理论区别，后面做做题目自然就知道了**。

而且很多讲解动态规划的文章都会讲最优子结构啊和重叠子问题啊这些，这些东西都是教科书的上定义，晦涩难懂而且不实用。

大家知道动规是由前一个状态推导出来的，而贪心是局部直接选最优的，对于刷题来说就够用了。

上述提到的背包问题，后序会详细讲解。

## 动态规划的解题步骤

做动规题目的时候，很多同学会陷入一个误区，就是以为把状态转移公式背下来，照葫芦画瓢改改，就开始写代码，甚至把题目AC之后，都不太清楚dp[i]表示的是什么。

**这就是一种朦胧的状态，然后就把题给过了，遇到稍稍难一点的，可能直接就不会了，然后看题解，然后继续照葫芦画瓢陷入这种恶性循环中**。

状态转移公式（递推公式）是很重要，但动规不仅仅只有递推公式。

**对于动态规划问题，我将拆解为如下五步曲，这五步都搞清楚了，才能说把动态规划真的掌握了！**

1. 确定dp数组（dp table）以及下标的含义
2. 确定递推公式
3. dp数组如何初始化
4. 确定遍历顺序
5. 举例推导dp数组

一些同学可能想为什么要先确定递推公式，然后在考虑初始化呢？

**因为一些情况是递推公式决定了dp数组要如何初始化！**

后面的讲解中我都是围绕着这五点来进行讲解。

可能刷过动态规划题目的同学可能都知道递推公式的重要性，感觉确定了递推公式这道题目就解出来了。

其实 确定递推公式 仅仅是解题里的一步而已！

一些同学知道递推公式，但搞不清楚dp数组应该如何初始化，或者正确的遍历顺序，以至于记下来公式，但写的程序怎么改都通过不了。

后序的讲解的大家就会慢慢感受到这五步的重要性了。

## 动态规划应该如何debug

相信动规的题目，很大部分同学都是这样做的。

看一下题解，感觉看懂了，然后照葫芦画瓢，如果能正好画对了，万事大吉，一旦要是没通过，就怎么改都通过不了，对 dp数组的初始化，递推公式，遍历顺序，处于一种黑盒的理解状态。

写动规题目，代码出问题很正常！

**找问题的最好方式就是把dp数组打印出来，看看究竟是不是按照自己思路推导的！**

一些同学对于dp的学习是黑盒的状态，就是不清楚dp数组的含义，不懂为什么这么初始化，递推公式背下来了，遍历顺序靠习惯就是这么写的，然后一鼓作气写出代码，如果代码能通过万事大吉，通过不了的话就凭感觉改一改。

这是一个很不好的习惯！

**做动规的题目，写代码之前一定要把状态转移在dp数组的上具体情况模拟一遍，心中有数，确定最后推出的是想要的结果**。

然后再写代码，如果代码没通过就打印dp数组，看看是不是和自己预先推导的哪里不一样。

如果打印出来和自己预先模拟推导是一样的，那么就是自己的递归公式、初始化或者遍历顺序有问题了。

如果和自己预先模拟推导的不一样，那么就是代码实现细节有问题。

**这样才是一个完整的思考过程，而不是一旦代码出问题，就毫无头绪的东改改西改改，最后过不了，或者说是稀里糊涂的过了**。

这也是我为什么在动规五步曲里强调推导dp数组的重要性。

举个例子哈：在「代码随想录」刷题小分队微信群里，一些录友可能代码通过不了，会把代码抛到讨论群里问：我这里代码都已经和题解一模一样了，为什么通过不了呢？

发出这样的问题之前，其实可以自己先思考这三个问题：

* 这道题目我举例推导状态转移公式了么？
* 我打印dp数组的日志了么？
* 打印出来了dp数组和我想的一样么？

**如果这灵魂三问自己都做到了，基本上这道题目也就解决了**，或者更清晰的知道自己究竟是哪一点不明白，是状态转移不明白，还是实现代码不知道该怎么写，还是不理解遍历dp数组的顺序。

然后在问问题，目的性就很强了，群里的小伙伴也可以快速知道提问者的疑惑了。

**注意这里不是说不让大家问问题哈， 而是说问问题之前要有自己的思考，问题要问到点子上！**

**大家工作之后就会发现，特别是大厂，问问题是一个专业活，是的，问问题也要体现出专业！**

如果问同事很不专业的问题，同事们会懒的回答，领导也会认为你缺乏思考能力，这对职场发展是很不利的。

所以大家在刷题的时候，就锻炼自己养成专业提问的好习惯。

## 总结

这一篇是动态规划的整体概述，讲解了什么是动态规划，动态规划的解题步骤，以及如何debug。

动态规划是一个很大的领域，今天这一篇讲解的内容是整个动态规划系列中都会使用到的一些理论基础。

在后序讲解中针对某一具体问题，还会讲解其对应的理论基础，例如背包问题中的01背包，leetcode上的题目都是01背包的应用，而没有纯01背包的问题，那么就需要在把对应的理论知识讲解一下。

大家会发现，我讲解的理论基础并不是教科书上各种动态规划的定义，错综复杂的公式。

这里理论基础篇已经是非常偏实用的了，每个知识点都是在解题实战中非常有用的内容，大家要重视起来哈。

今天我们开始新的征程了，你准备好了么？

# 二、509. 斐波那契数

[力扣题目链接(opens new window)](https://leetcode.cn/problems/fibonacci-number/)

斐波那契数，通常用 F(n) 表示，形成的序列称为 斐波那契数列 。该数列由 0 和 1 开始，后面的每一项数字都是前面两项数字的和。也就是： F(0) = 0，F(1) = 1 F(n) = F(n - 1) + F(n - 2)，其中 n > 1， 给你n ，请计算 F(n) 。

示例 1：

* 输入：2
* 输出：1
* 解释：F(2) = F(1) + F(0) = 1 + 0 = 1

示例 2：

* 输入：3
* 输出：2
* 解释：F(3) = F(2) + F(1) = 1 + 1 = 2

示例 3：

* 输入：4
* 输出：3
* 解释：F(4) = F(3) + F(2) = 2 + 1 = 3

提示：

* 0 <= n <= 30

## 算法公开课

[《代码随想录》算法视频公开课 **(opens new window)**](https://programmercarl.com/other/gongkaike.html)：[手把手带你入门动态规划 | leetcode：509.斐波那契数 **(opens new window)**](https://www.bilibili.com/video/BV1f5411K7mo)，**相信结合视频在看本篇题解，更有助于大家对本题的理解**。

## 思路

斐波那契数列大家应该非常熟悉不过了，非常适合作为动规第一道题目来练练手。

因为这道题目比较简单，可能一些同学并不需要做什么分析，直接顺手一写就过了。

**但「代码随想录」的风格是：简单题目是用来加深对解题方法论的理解的**。

通过这道题目让大家可以初步认识到，按照动规五部曲是如何解题的。

对于动规，如果没有方法论的话，可能简单题目可以顺手一写就过，难一点就不知道如何下手了。

所以我总结的动规五部曲，是要用来贯穿整个动态规划系列的，就像之前讲过[二叉树系列的递归三部曲 **(opens new window)**](https://www.programmercarl.com/%E4%BA%8C%E5%8F%89%E6%A0%91%E7%9A%84%E9%80%92%E5%BD%92%E9%81%8D%E5%8E%86.html)，[回溯法系列的回溯三部曲 **(opens new window)**](https://programmercarl.com/%E5%9B%9E%E6%BA%AF%E7%AE%97%E6%B3%95%E7%90%86%E8%AE%BA%E5%9F%BA%E7%A1%80.html)一样。后面慢慢大家就会体会到，动规五部曲方法的重要性。

### 动态规划

动规五部曲：

这里我们要用一个一维dp数组来保存递归的结果

1. 确定dp数组以及下标的含义

dp[i]的定义为：第i个数的斐波那契数值是dp[i]

2. 确定递推公式

为什么这是一道非常简单的入门题目呢？

**因为题目已经把递推公式直接给我们了：状态转移方程 dp[i] = dp[i - 1] + dp[i - 2];**

3. dp数组如何初始化

**题目中把如何初始化也直接给我们了，如下：**

```text
dp[0] = 0;
dp[1] = 1;
```

4. 确定遍历顺序

从递归公式dp[i] = dp[i - 1] + dp[i - 2];中可以看出，dp[i]是依赖 dp[i - 1] 和 dp[i - 2]，那么遍历的顺序一定是从前到后遍历的

5. 举例推导dp数组

按照这个递推公式dp[i] = dp[i - 1] + dp[i - 2]，我们来推导一下，当N为10的时候，dp数组应该是如下的数列：

0 1 1 2 3 5 8 13 21 34 55

如果代码写出来，发现结果不对，就把dp数组打印出来看看和我们推导的数列是不是一致的。

以上我们用动规的方法分析完了，C++代码如下：

```cpp
class Solution {
public:
    int fib(int N) {
        if (N <= 1) return N;
        vector<int> dp(N + 1);
        dp[0] = 0;
        dp[1] = 1;
        for (int i = 2; i <= N; i++) {
            dp[i] = dp[i - 1] + dp[i - 2];
        }
        return dp[N];
    }
};
```

* 时间复杂度：O(n)
* 空间复杂度：O(n)

当然可以发现，我们只需要维护两个数值就可以了，不需要记录整个序列。

代码如下：

```cpp
class Solution {
public:
    int fib(int N) {
        if (N <= 1) return N;
        int dp[2];
        dp[0] = 0;
        dp[1] = 1;
        for (int i = 2; i <= N; i++) {
            int sum = dp[0] + dp[1];
            dp[0] = dp[1];
            dp[1] = sum;
        }
        return dp[1];
    }
};
```

* 时间复杂度：O(n)
* 空间复杂度：O(1)

### 递归解法

本题还可以使用递归解法来做

代码如下：

```cpp
class Solution {
public:
    int fib(int N) {
        if (N < 2) return N;
        return fib(N - 1) + fib(N - 2);
    }
};
```

* 时间复杂度：O(2^n)
* 空间复杂度：O(n)，算上了编程语言中实现递归的系统栈所占空间

这个递归的时间复杂度大家画一下树形图就知道了，如果不清晰的同学，可以看这篇：[通过一道面试题目，讲一讲递归算法的时间复杂度！(opens new window)](https://programmercarl.com/%E5%89%8D%E5%BA%8F/%E9%80%9A%E8%BF%87%E4%B8%80%E9%81%93%E9%9D%A2%E8%AF%95%E9%A2%98%E7%9B%AE%EF%BC%8C%E8%AE%B2%E4%B8%80%E8%AE%B2%E9%80%92%E5%BD%92%E7%AE%97%E6%B3%95%E7%9A%84%E6%97%B6%E9%97%B4%E5%A4%8D%E6%9D%82%E5%BA%A6%EF%BC%81.html)

## 总结

斐波那契数列这道题目是非常基础的题目，我在后面的动态规划的讲解中将会多次提到斐波那契数列！

这里我严格按照[关于动态规划，你该了解这些！ **(opens new window)**](https://programmercarl.com/%E5%8A%A8%E6%80%81%E8%A7%84%E5%88%92%E7%90%86%E8%AE%BA%E5%9F%BA%E7%A1%80.html)中的动规五部曲来分析了这道题目，一些分析步骤可能同学感觉没有必要搞的这么复杂，代码其实上来就可以撸出来。

但我还是强调一下，简单题是用来掌握方法论的，动规五部曲将在接下来的动态规划讲解中发挥重要作用，敬请期待！

就酱，循序渐进学算法，认准「代码随想录」！

## 其他语言版本

### Python

动态规划（版本一）

```python

class Solution:
    def fib(self, n: int) -> int:
   
        # 排除 Corner Case
        if n == 0:
            return 0
  
        # 创建 dp table 
        dp = [0] * (n + 1)

        # 初始化 dp 数组
        dp[0] = 0
        dp[1] = 1

        # 遍历顺序: 由前向后。因为后面要用到前面的状态
        for i in range(2, n + 1):

            # 确定递归公式/状态转移公式
            dp[i] = dp[i - 1] + dp[i - 2]
  
        # 返回答案
        return dp[n]

```

动态规划（版本二）

```python

class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
  
        dp = [0, 1]
  
        for i in range(2, n + 1):
            total = dp[0] + dp[1]
            dp[0] = dp[1]
            dp[1] = total
  
        return dp[1]


```

动态规划（版本三）

```python
class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
  
        prev1, prev2 = 0, 1
  
        for _ in range(2, n + 1):
            curr = prev1 + prev2
            prev1, prev2 = prev2, curr
  
        return prev2

```

递归（版本一）

```python

class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        return self.fib(n - 1) + self.fib(n - 2)
```

# 三、70. 爬楼梯

[力扣题目链接(opens new window)](https://leetcode.cn/problems/climbing-stairs/)

假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

注意：给定 n 是一个正整数。

示例 1：

* 输入： 2
* 输出： 2
* 解释： 有两种方法可以爬到楼顶。
  * 1 阶 + 1 阶
  * 2 阶

示例 2：

* 输入： 3
* 输出： 3
* 解释： 有三种方法可以爬到楼顶。
  * 1 阶 + 1 阶 + 1 阶
  * 1 阶 + 2 阶
  * 2 阶 + 1 阶

## 算法公开课

[《代码随想录》算法视频公开课 **(opens new window)**](https://programmercarl.com/other/gongkaike.html)：[带你学透动态规划-爬楼梯|LeetCode:70.爬楼梯） **(opens new window)**](https://www.bilibili.com/video/BV17h411h7UH)，**相信结合视频再看本篇题解，更有助于大家对本题的理解**。

## 思路

本题大家如果没有接触过的话，会感觉比较难，多举几个例子，就可以发现其规律。

爬到第一层楼梯有一种方法，爬到二层楼梯有两种方法。

那么第一层楼梯再跨两步就到第三层 ，第二层楼梯再跨一步就到第三层。

所以到第三层楼梯的状态可以由第二层楼梯 和 到第一层楼梯状态推导出来，那么就可以想到动态规划了。

我们来分析一下，动规五部曲：

定义一个一维数组来记录不同楼层的状态

1. 确定dp数组以及下标的含义

dp[i]： 爬到第i层楼梯，有dp[i]种方法

2. 确定递推公式

如何可以推出dp[i]呢？

从dp[i]的定义可以看出，dp[i] 可以有两个方向推出来。

首先是dp[i - 1]，上i-1层楼梯，有dp[i - 1]种方法，那么再一步跳一个台阶不就是dp[i]了么。

还有就是dp[i - 2]，上i-2层楼梯，有dp[i - 2]种方法，那么再一步跳两个台阶不就是dp[i]了么。

那么dp[i]就是 dp[i - 1]与dp[i - 2]之和！

所以dp[i] = dp[i - 1] + dp[i - 2] 。

在推导dp[i]的时候，一定要时刻想着dp[i]的定义，否则容易跑偏。

这体现出确定dp数组以及下标的含义的重要性！

3. dp数组如何初始化

再回顾一下dp[i]的定义：爬到第i层楼梯，有dp[i]种方法。

那么i为0，dp[i]应该是多少呢，这个可以有很多解释，但基本都是直接奔着答案去解释的。

例如强行安慰自己爬到第0层，也有一种方法，什么都不做也就是一种方法即：dp[0] = 1，相当于直接站在楼顶。

但总有点牵强的成分。

那还这么理解呢：我就认为跑到第0层，方法就是0啊，一步只能走一个台阶或者两个台阶，然而楼层是0，直接站楼顶上了，就是不用方法，dp[0]就应该是0.

**其实这么争论下去没有意义，大部分解释说dp[0]应该为1的理由其实是因为dp[0]=1的话在递推的过程中i从2开始遍历本题就能过，然后就往结果上靠去解释dp[0] = 1**。

从dp数组定义的角度上来说，dp[0] = 0 也能说得通。

需要注意的是：题目中说了n是一个正整数，题目根本就没说n有为0的情况。

所以本题其实就不应该讨论dp[0]的初始化！

我相信dp[1] = 1，dp[2] = 2，这个初始化大家应该都没有争议的。

所以我的原则是：不考虑dp[0]如何初始化，只初始化dp[1] = 1，dp[2] = 2，然后从i = 3开始递推，这样才符合dp[i]的定义。

4. 确定遍历顺序

从递推公式dp[i] = dp[i - 1] + dp[i - 2];中可以看出，遍历顺序一定是从前向后遍历的

5. 举例推导dp数组

举例当n为5的时候，dp table（dp数组）应该是这样的

https://code-thinking-1253855093.file.myqcloud.com/pics/20210105202546299.png（图像链接）

如果代码出问题了，就把dp table 打印出来，看看究竟是不是和自己推导的一样。

**此时大家应该发现了，这不就是斐波那契数列么！**

唯一的区别是，没有讨论dp[0]应该是什么，因为dp[0]在本题没有意义！

以上五部分析完之后，C++代码如下：

```cpp
// 版本一
class Solution {
public:
    int climbStairs(int n) {
        if (n <= 1) return n; // 因为下面直接对dp[2]操作了，防止空指针
        vector<int> dp(n + 1);
        dp[1] = 1;
        dp[2] = 2;
        for (int i = 3; i <= n; i++) { // 注意i是从3开始的
            dp[i] = dp[i - 1] + dp[i - 2];
        }
        return dp[n];
    }
};
```

* 时间复杂度：\$O(n)\$
* 空间复杂度：\$O(n)\$

当然依然也可以，优化一下空间复杂度，代码如下：

```cpp
// 版本二
class Solution {
public:
    int climbStairs(int n) {
        if (n <= 1) return n;
        int dp[3];
        dp[1] = 1;
        dp[2] = 2;
        for (int i = 3; i <= n; i++) {
            int sum = dp[1] + dp[2];
            dp[1] = dp[2];
            dp[2] = sum;
        }
        return dp[2];
    }
};
```

* 时间复杂度：\$O(n)\$
* 空间复杂度：\$O(1)\$

后面将讲解的很多动规的题目其实都是当前状态依赖前两个，或者前三个状态，都可以做空间上的优化，**但我个人认为面试中能写出版本一就够了哈，清晰明了，如果面试官要求进一步优化空间的话，我们再去优化**。

因为版本一才能体现出动规的思想精髓，递推的状态变化。

## 拓展

这道题目还可以继续深化，就是一步一个台阶，两个台阶，三个台阶，直到 m个台阶，有多少种方法爬到n阶楼顶。

这又有难度了，这其实是一个完全背包问题，但力扣上没有这种题目，大家可以去卡码网去做一下 [57. 爬楼梯(opens new window)](https://kamacoder.com/problempage.php?pid=1067)

所以后续我在讲解背包问题的时候，今天这道题还会从背包问题的角度上来再讲一遍。 如果想提前看一下，可以看这篇:[70.爬楼梯完全背包版本(opens new window)](https://programmercarl.com/0070.%E7%88%AC%E6%A5%BC%E6%A2%AF%E5%AE%8C%E5%85%A8%E8%83%8C%E5%8C%85%E7%89%88%E6%9C%AC.html)

这里我先给出本题的代码：

```cpp
class Solution {
public:
    int climbStairs(int n) {
        vector<int> dp(n + 1, 0);
        dp[0] = 1;
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= m; j++) { // 把m换成2，就可以AC爬楼梯这道题
                if (i - j >= 0) dp[i] += dp[i - j];
            }
        }
        return dp[n];
    }
};
```

代码中m表示最多可以爬m个台阶。

**以上代码不能运行哈，我主要是为了体现只要把m换成2，粘过去，就可以AC爬楼梯这道题，不信你就粘一下试试**。

**此时我就发现一个绝佳的大厂面试题**，第一道题就是单纯的爬楼梯，然后看候选人的代码实现，如果把dp[0]的定义成1了，就可以发难了，为什么dp[0]一定要初始化为1，此时可能候选人就要强行给dp[0]应该是1找各种理由。那这就是一个考察点了，对dp[i]的定义理解的不深入。

然后可以继续发难，如果一步一个台阶，两个台阶，三个台阶，直到 m个台阶，有多少种方法爬到n阶楼顶。这道题目leetcode上并没有原题，绝对是考察候选人算法能力的绝佳好题。

这一连套问下来，候选人算法能力如何，面试官心里就有数了。

**其实大厂面试最喜欢的问题就是这种简单题，然后慢慢变化，在小细节上考察候选人**。

## 总结

这道题目和[动态规划：斐波那契数 **(opens new window)**](https://programmercarl.com/0509.%E6%96%90%E6%B3%A2%E9%82%A3%E5%A5%91%E6%95%B0.html)题目基本是一样的，但是会发现本题相比[动态规划：斐波那契数 **(opens new window)**](https://programmercarl.com/0509.%E6%96%90%E6%B3%A2%E9%82%A3%E5%A5%91%E6%95%B0.html)难多了，为什么呢？

关键是 [动态规划：斐波那契数 **(opens new window)**](https://programmercarl.com/0509.%E6%96%90%E6%B3%A2%E9%82%A3%E5%A5%91%E6%95%B0.html)题目描述就已经把动规五部曲里的递归公式和如何初始化都给出来了，剩下几部曲也自然而然的推出来了。

而本题，就需要逐个分析了，大家现在应该初步感受出[关于动态规划，你该了解这些！ **(opens new window)**](https://programmercarl.com/%E5%8A%A8%E6%80%81%E8%A7%84%E5%88%92%E7%90%86%E8%AE%BA%E5%9F%BA%E7%A1%80.html)里给出的动规五部曲了。

简单题是用来掌握方法论的，例如昨天斐波那契的题目够简单了吧，但昨天和今天可以使用一套方法分析出来的，这就是方法论！

所以不要轻视简单题，那种凭感觉就刷过去了，其实和没掌握区别不大，只有掌握方法论并说清一二三，才能触类旁通，举一反三哈！

## 其他语言版本

### Python

动态规划（版本一）

```python
# 空间复杂度为O(n)版本
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return n
    
        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2
    
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
    
        return dp[n]

```

动态规划（版本二）

```python

# 空间复杂度为O(3)版本
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return n
    
        dp = [0] * 3
        dp[1] = 1
        dp[2] = 2
    
        for i in range(3, n + 1):
            total = dp[1] + dp[2]
            dp[1] = dp[2]
            dp[2] = total
    
        return dp[2]

```

动态规划（版本三）

```python

# 空间复杂度为O(1)版本
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return n
    
        prev1 = 1
        prev2 = 2
    
        for i in range(3, n + 1):
            total = prev1 + prev2
            prev1 = prev2
            prev2 = total
    
        return prev2


```


# 四、746. 使用最小花费爬楼梯

[力扣题目链接(opens new window)](https://leetcode.cn/problems/min-cost-climbing-stairs/)

**旧题目描述**：

数组的每个下标作为一个阶梯，第 i 个阶梯对应着一个非负数的体力花费值 cost[i]（下标从 0 开始）。

每当你爬上一个阶梯你都要花费对应的体力值，一旦支付了相应的体力值，你就可以选择向上爬一个阶梯或者爬两个阶梯。

请你找出达到楼层顶部的最低花费。在开始时，你可以选择从下标为 0 或 1 的元素作为初始阶梯。

示例 1：

* 输入：cost = [10, 15, 20]
* 输出：15
* 解释：最低花费是从 cost[1] 开始，然后走两步即可到阶梯顶，一共花费 15 。

示例 2：

* 输入：cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
* 输出：6
* 解释：最低花费方式是从 cost[0] 开始，逐个经过那些 1 ，跳过 cost[3] ，一共花费 6 。

提示：

* cost 的长度范围是 [2, 1000]。
* cost[i] 将会是一个整型数据，范围为 [0, 999] 。

## 算法公开课

[《代码随想录》算法视频公开课 **(opens new window)**](https://programmercarl.com/other/gongkaike.html)：：[动态规划开更了！| LeetCode：746. 使用最小花费爬楼梯 **(opens new window)**](https://www.bilibili.com/video/BV16G411c7yZ/)，**相信结合视频再看本篇题解，更有助于大家对本题的理解**。

---

本题之前的题目描述是很模糊的，看不出来，第一步需要花费体力值，最后一步不用花费，还是说 第一步不花费体力值，最后一步花费。

后来力扣改了题目描述，**新题目描述**：

给你一个整数数组 cost ，其中 cost[i] 是从楼梯第 i 个台阶向上爬需要支付的费用。一旦你支付此费用，即可选择向上爬一个或者两个台阶。

你可以选择从下标为 0 或下标为 1 的台阶开始爬楼梯。

请你计算并返回达到楼梯顶部的最低花费。

https://code-thinking-1253855093.file.myqcloud.com/pics/20221031170131.png（图像链接）

## 思路

（**在力扣修改了题目描述下，我又重新修改了题解**）

修改之后的题意就比较明确了，题目中说 “你可以选择从下标为 0 或下标为 1 的台阶开始爬楼梯” 也就是相当于 跳到 下标 0 或者 下标 1 是不花费体力的， 从 下标 0 下标1 开始跳就要花费体力了。

1. 确定dp数组以及下标的含义

使用动态规划，就要有一个数组来记录状态，本题只需要一个一维数组dp[i]就可以了。

**dp[i]的定义：到达第i台阶所花费的最少体力为dp[i]**。

**对于dp数组的定义，大家一定要清晰！**

2. 确定递推公式

**可以有两个途径得到dp[i]，一个是dp[i-1] 一个是dp[i-2]**。

dp[i - 1] 跳到 dp[i] 需要花费 dp[i - 1] + cost[i - 1]。

dp[i - 2] 跳到 dp[i] 需要花费 dp[i - 2] + cost[i - 2]。

那么究竟是选从dp[i - 1]跳还是从dp[i - 2]跳呢？

一定是选最小的，所以dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2]);

3. dp数组如何初始化

看一下递归公式，dp[i]由dp[i - 1]，dp[i - 2]推出，既然初始化所有的dp[i]是不可能的，那么只初始化dp[0]和dp[1]就够了，其他的最终都是dp[0]dp[1]推出。

那么 dp[0] 应该是多少呢？ 根据dp数组的定义，到达第0台阶所花费的最小体力为dp[0]，那么有同学可能想，那dp[0] 应该是 cost[0]，例如 cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1] 的话，dp[0] 就是 cost[0] 应该是1。

这里就要说明本题力扣为什么改题意，而且修改题意之后 就清晰很多的原因了。

新题目描述中明确说了 “你可以选择从下标为 0 或下标为 1 的台阶开始爬楼梯。” 也就是说 到达 第 0 个台阶是不花费的，但从 第0 个台阶 往上跳的话，需要花费 cost[0]。

所以初始化 dp[0] = 0，dp[1] = 0;

4. 确定遍历顺序

最后一步，递归公式有了，初始化有了，如何遍历呢？

本题的遍历顺序其实比较简单，简单到很多同学都忽略了思考这一步直接就把代码写出来了。

因为是模拟台阶，而且dp[i]由dp[i-1]dp[i-2]推出，所以是从前到后遍历cost数组就可以了。

> **但是稍稍有点难度的动态规划，其遍历顺序并不容易确定下来**。 例如：01背包，都知道两个for循环，一个for遍历物品嵌套一个for遍历背包容量，那么为什么不是一个for遍历背包容量嵌套一个for遍历物品呢？ 以及在使用一维dp数组的时候遍历背包容量为什么要倒序呢？

**这些都与遍历顺序息息相关。当然背包问题后续「代码随想录」都会重点讲解的！**

5. 举例推导dp数组

拿示例2：cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1] ，来模拟一下dp数组的状态变化，如下：

https://code-thinking-1253855093.file.myqcloud.com/pics/20221026175104.png（图像链接）

如果大家代码写出来有问题，就把dp数组打印出来，看看和如上推导的是不是一样的。

以上分析完毕，整体C++代码如下：

```cpp
class Solution {
public:
    int minCostClimbingStairs(vector<int>& cost) {
        vector<int> dp(cost.size() + 1);
        dp[0] = 0; // 默认第一步都是不花费体力的
        dp[1] = 0;
        for (int i = 2; i <= cost.size(); i++) {
            dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2]);
        }
        return dp[cost.size()];
    }
};
```

* 时间复杂度：O(n)
* 空间复杂度：O(n)

还可以优化空间复杂度，因为dp[i]就是由前两位推出来的，那么也不用dp数组了，C++代码如下：

```cpp
// 版本二
class Solution {
public:
    int minCostClimbingStairs(vector<int>& cost) {
        int dp0 = 0;
        int dp1 = 0;
        for (int i = 2; i <= cost.size(); i++) {
            int dpi = min(dp1 + cost[i - 1], dp0 + cost[i - 2]);
            dp0 = dp1; // 记录一下前两位
            dp1 = dpi;
        }
        return dp1;
    }
};

```

* 时间复杂度：O(n)
* 空间复杂度：O(1)

当然如果在面试中，能写出版本一就行，除非面试官额外要求 空间复杂度，那么再去思考版本二，因为版本二还是有点绕。版本一才是正常思路。

## 拓展

旧力扣描述，如果按照 第一步是花费的，最后一步不花费，那么代码是这么写的，提交也可以通过

```cpp
// 版本一
class Solution {
public:
    int minCostClimbingStairs(vector<int>& cost) {
        vector<int> dp(cost.size());
        dp[0] = cost[0]; // 第一步有花费
        dp[1] = cost[1];
        for (int i = 2; i < cost.size(); i++) {
            dp[i] = min(dp[i - 1], dp[i - 2]) + cost[i];
        }
        // 注意最后一步可以理解为不用花费，所以取倒数第一步，第二步的最少值
        return min(dp[cost.size() - 1], dp[cost.size() - 2]);
    }
};
```

当然如果对 动态规划 理解不够深入的话，拓展内容就别看了，容易越看越懵。

## 总结

大家可以发现这道题目相对于 昨天的[动态规划：爬楼梯 **(opens new window)**](https://programmercarl.com/0070.%E7%88%AC%E6%A5%BC%E6%A2%AF.html)又难了一点，但整体思路是一样的。

从[动态规划：斐波那契数 **(opens new window)**](https://programmercarl.com/0509.%E6%96%90%E6%B3%A2%E9%82%A3%E5%A5%91%E6%95%B0.html)到 [动态规划：爬楼梯 **(opens new window)**](https://programmercarl.com/0070.%E7%88%AC%E6%A5%BC%E6%A2%AF.html)再到今天这道题目，录友们感受到循序渐进的梯度了嘛。

每个系列开始的时候，都有录友和我反馈说题目太简单了，赶紧上难度，但也有录友和我说有点难了，快跟不上了。

其实我选的题目都是有目的性的，就算是简单题，也是为了练习方法论，然后难度都是梯度上来的，一环扣一环。

但我也可以随便选来一道难题讲呗，这其实是最省事的，不用管什么题目顺序，看心情找一道就讲。

难的是把题目按梯度排好，循序渐进，再按照统一方法论把这些都串起来，所以大家不要催我哈，按照我的节奏一步一步来就行了。

## 其他语言版本

以下版本其他语言版本，大多是按照旧力扣题解来写的，欢迎大家在[Github **(opens new window)**](https://github.com/youngyangyang04/leetcode-master)上[提交pr **(opens new window)**](https://mp.weixin.qq.com/s/tqCxrMEU-ajQumL1i8im9A)，修正一波。

### Python

动态规划（版本一）

```python

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0] * (len(cost) + 1)
        dp[0] = 0  # 初始值，表示从起点开始不需要花费体力
        dp[1] = 0  # 初始值，表示经过第一步不需要花费体力
      
        for i in range(2, len(cost) + 1):
            # 在第i步，可以选择从前一步（i-1）花费体力到达当前步，或者从前两步（i-2）花费体力到达当前步
            # 选择其中花费体力较小的路径，加上当前步的花费，更新dp数组
            dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])
      
        return dp[len(cost)]  # 返回到达楼顶的最小花费

```

动态规划（版本二）

```python
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp0 = 0  # 初始值，表示从起点开始不需要花费体力
        dp1 = 0  # 初始值，表示经过第一步不需要花费体力
      
        for i in range(2, len(cost) + 1):
            # 在第i步，可以选择从前一步（i-1）花费体力到达当前步，或者从前两步（i-2）花费体力到达当前步
            # 选择其中花费体力较小的路径，加上当前步的花费，得到当前步的最小花费
            dpi = min(dp1 + cost[i - 1], dp0 + cost[i - 2])
          
            dp0 = dp1  # 更新dp0为前一步的值，即上一次循环中的dp1
            dp1 = dpi  # 更新dp1为当前步的最小花费
      
        return dp1  # 返回到达楼顶的最小花费

```

动态规划（版本三）

```python
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0] * len(cost)
        dp[0] = cost[0]  # 第一步有花费
        dp[1] = cost[1]
        for i in range(2, len(cost)):
            dp[i] = min(dp[i - 1], dp[i - 2]) + cost[i]
        # 注意最后一步可以理解为不用花费，所以取倒数第一步，第二步的最少值
        return min(dp[-1], dp[-2])

```

动态规划（版本四）

```python
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        prev_1 = cost[0]  # 前一步的最小花费
        prev_2 = cost[1]  # 前两步的最小花费
        for i in range(2, n):
            current = min(prev_1, prev_2) + cost[i]  # 当前位置的最小花费
            prev_1, prev_2 = prev_2, current  # 更新前一步和前两步的最小花费
        return min(prev_1, prev_2)  # 最后一步可以理解为不用花费，取倒数第一步和第二步的最少值


```

# 五、本周小结！（动态规划系列一）

这周我们正式开始动态规划的学习！

## 周一

在[关于动态规划，你该了解这些！ **(opens new window)**](https://programmercarl.com/%E5%8A%A8%E6%80%81%E8%A7%84%E5%88%92%E7%90%86%E8%AE%BA%E5%9F%BA%E7%A1%80.html)中我们讲解了动态规划的基础知识。

首先讲一下动规和贪心的区别，其实大家不用太强调理论上的区别，做做题，就感受出来了。

然后我们讲了动规的五部曲：

1. 确定dp数组（dp table）以及下标的含义
2. 确定递推公式
3. dp数组如何初始化
4. 确定遍历顺序
5. 举例推导dp数组

后序我们在讲解动规的题目时候，都离不开这五步！

本周都是简单题目，大家可能会感觉 按照这五部来好麻烦，凭感觉随手一写，直接就过，越到后面越会感觉，凭感觉这个事还是不靠谱的。

最后我们讲了动态规划题目应该如何debug，相信一些录友做动规的题目，一旦报错也是凭感觉来改。

其实只要把dp数组打印出来，哪里有问题一目了然！

**如果代码写出来了，一直AC不了，灵魂三问：**

1. 这道题目我举例推导状态转移公式了么？
2. 我打印dp数组的日志了么？
3. 打印出来了dp数组和我想的一样么？

专治各种代码写出来了但AC不了的疑难杂症。

## 周二

这道题目[动态规划：斐波那契数 **(opens new window)**](https://programmercarl.com/0509.%E6%96%90%E6%B3%A2%E9%82%A3%E5%A5%91%E6%95%B0.html)是当之无愧的动规入门题。

简单题，我们就是用来了解方法论的，用动规五部曲走一遍，题目其实已经把递推公式，和dp数组如何初始化都给我们了。

## 周三

[动态规划：爬楼梯 **(opens new window)**](https://programmercarl.com/0070.%E7%88%AC%E6%A5%BC%E6%A2%AF.html)这道题目其实就是斐波那契数列。

但正常思考过程应该是推导完递推公式之后，发现这是斐波那契，而不是上来就知道这是斐波那契。

在这道题目的第三步，确认dp数组如何初始化，其实就可以看出来，对dp[i]定义理解的深度。

dp[0]其实就是一个无意义的存在，不用去初始化dp[0]。

有的题解是把dp[0]初始化为1，然后遍历的时候i从2开始遍历，这样是可以解题的，然后强行解释一波dp[0]应该等于1的含义。

一个严谨的思考过程，应该是初始化dp[1] = 1，dp[2] = 2，然后i从3开始遍历，代码如下：

```cpp
dp[1] = 1;
dp[2] = 2;
for (int i = 3; i <= n; i++) { // 注意i是从3开始的
    dp[i] = dp[i - 1] + dp[i - 2];
}
```

这个可以是面试的一个小问题，考察候选人对dp[i]定义的理解程度。

这道题目还可以继续深化，就是一步一个台阶，两个台阶，三个台阶，直到 m个台阶，有多少种方法爬到n阶楼顶。

这又有难度了，这其实是一个完全背包问题，但力扣上没有这种题目，所以后续我在讲解背包问题的时候，今天这道题还会拿从背包问题的角度上来再讲一遍。

这里我先给出我的实现代码：

```cpp
class Solution {
public:
    int climbStairs(int n) {
        vector<int> dp(n + 1, 0);
        dp[0] = 1;
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= m; j++) { // 把m换成2，就可以AC爬楼梯这道题
                if (i - j >= 0) dp[i] += dp[i - j];
            }
        }
        return dp[n];
    }
};
```

代码中m表示最多可以爬m个台阶。

**以上代码不能运行哈，我主要是为了体现只要把m换成2，粘过去，就可以AC爬楼梯这道题，不信你就粘一下试试**。

**此时我就发现一个绝佳的大厂面试题**，第一道题就是单纯的爬楼梯，然后看候选人的代码实现，如果把dp[0]的定义成1了，就可以发难了，为什么dp[0]一定要初始化为1，此时可能候选人就要强行给dp[0]应该是1找各种理由。那这就是一个考察点了，对dp[i]的定义理解的不深入。

然后可以继续发难，如果一步一个台阶，两个台阶，三个台阶，直到 m个台阶，有多少种方法爬到n阶楼顶。这道题目leetcode上并没有原题，绝对是考察候选人算法能力的绝佳好题。

这一连套问下来，候选人算法能力如何，面试官心里就有数了。

**其实大厂面试最喜欢问题的就是这种简单题，然后慢慢变化，在小细节上考察候选人**。

这道绝佳的面试题我没有用过，如果录友们有面试别人的需求，就把这个套路拿去吧。

我在[通过一道面试题目，讲一讲递归算法的时间复杂度！ **(opens new window)**](https://programmercarl.com/%E5%89%8D%E5%BA%8F/%E9%80%9A%E8%BF%87%E4%B8%80%E9%81%93%E9%9D%A2%E8%AF%95%E9%A2%98%E7%9B%AE%EF%BC%8C%E8%AE%B2%E4%B8%80%E8%AE%B2%E9%80%92%E5%BD%92%E7%AE%97%E6%B3%95%E7%9A%84%E6%97%B6%E9%97%B4%E5%A4%8D%E6%9D%82%E5%BA%A6%EF%BC%81.html)中，以我自己面试别人的真实经历，通过求x的n次方 这么简单的题目，就可以考察候选人对算法性能以及递归的理解深度，录友们可以看看，绝对有收获！

## 周四

这道题目[动态规划：使用最小花费爬楼梯 **(opens new window)**](https://programmercarl.com/0746.%E4%BD%BF%E7%94%A8%E6%9C%80%E5%B0%8F%E8%8A%B1%E8%B4%B9%E7%88%AC%E6%A5%BC%E6%A2%AF.html)就是在爬台阶的基础上加了一个花费，

这道题描述也确实有点魔幻。

题目描述为：每当你爬上一个阶梯你都要花费对应的体力值，一旦支付了相应的体力值，你就可以选择向上爬一个阶梯或者爬两个阶梯。

示例1：

输入：cost = [10, 15, 20] 输出：15

**从题目描述可以看出：要不是第一步不需要花费体力，要不就是第最后一步不需要花费体力，我个人理解：题意说的其实是第一步是要支付费用的！**。因为是当你爬上一个台阶就要花费对应的体力值！

所以我定义的dp[i]意思是也是第一步是要花费体力的，最后一步不用花费体力了，因为已经支付了。

之后一些录友在留言区说 可以定义dp[i]为:第一步是不花费体力，最后一步是花费体力的。

所以代码也可以这么写：

```cpp
class Solution {
public:
    int minCostClimbingStairs(vector<int>& cost) {
        vector<int> dp(cost.size() + 1);
        dp[0] = 0; // 默认第一步都是不花费体力的
        dp[1] = 0;
        for (int i = 2; i <= cost.size(); i++) {
            dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2]);
        }
        return dp[cost.size()];
    }
};
```

这么写看上去比较顺，但是就是感觉和题目描述的不太符。也没有必要这么细扣题意了，大家只要知道，题目的意思反正就是要不是第一步不花费，要不是最后一步不花费，都可以。

## 总结

本周题目简单一些，也非常合适初学者来练练手。

下周开始上难度了哈，然后大下周就开始讲解背包问题，好戏还在后面，录友们跟上哈。

学算法，认准「代码随想录」就够了，Carl带你打怪升级！

# 六、62.不同路径

[力扣题目链接(opens new window)](https://leetcode.cn/problems/unique-paths/)

一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为 “Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 “Finish” ）。

问总共有多少条不同的路径？

示例 1：

https://code-thinking-1253855093.file.myqcloud.com/pics/20210110174033215.png（图像链接）

* 输入：m = 3, n = 7
* 输出：28

示例 2：

* 输入：m = 2, n = 3
* 输出：3

解释： 从左上角开始，总共有 3 条路径可以到达右下角。

1. 向右 -> 向右 -> 向下
2. 向右 -> 向下 -> 向右
3. 向下 -> 向右 -> 向右

示例 3：

* 输入：m = 7, n = 3
* 输出：28

示例 4：

* 输入：m = 3, n = 3
* 输出：6

提示：

* 1 <= m, n <= 100
* 题目数据保证答案小于等于 2 \* 10^9

## 算法公开课

[《代码随想录》算法视频公开课 **(opens new window)**](https://programmercarl.com/other/gongkaike.html)：[动态规划中如何初始化很重要！| LeetCode：62.不同路径 **(opens new window)**](https://www.bilibili.com/video/BV1ve4y1x7Eu/)，**相信结合视频再看本篇题解，更有助于大家对本题的理解**。

## 思路

### 深搜

这道题目，刚一看最直观的想法就是用图论里的深搜，来枚举出来有多少种路径。

注意题目中说机器人每次只能向下或者向右移动一步，那么其实**机器人走过的路径可以抽象为一棵二叉树，而叶子节点就是终点！**

如图举例：

https://code-thinking-1253855093.file.myqcloud.com/pics/20201209113602700.png（图像链接）

此时问题就可以转化为求二叉树叶子节点的个数，代码如下：

```cpp
class Solution {
private:
    int dfs(int i, int j, int m, int n) {
        if (i > m || j > n) return 0; // 越界了
        if (i == m && j == n) return 1; // 找到一种方法，相当于找到了叶子节点
        return dfs(i + 1, j, m, n) + dfs(i, j + 1, m, n);
    }
public:
    int uniquePaths(int m, int n) {
        return dfs(1, 1, m, n);
    }
};
```

**大家如果提交了代码就会发现超时了！**

来分析一下时间复杂度，这个深搜的算法，其实就是要遍历整个二叉树。

这棵树的深度其实就是m+n-1（深度按从1开始计算）。

那二叉树的节点个数就是 2^(m + n - 1) - 1。可以理解深搜的算法就是遍历了整个满二叉树（其实没有遍历整个满二叉树，只是近似而已）

所以上面深搜代码的时间复杂度为O(2^(m + n - 1) - 1)，可以看出，这是指数级别的时间复杂度，是非常大的。

### 动态规划

机器人从(0 , 0) 位置出发，到(m - 1, n - 1)终点。

按照动规五部曲来分析：

1. 确定dp数组（dp table）以及下标的含义

dp[i][j] ：表示从（0 ，0）出发，到(i, j) 有dp[i][j]条不同的路径。

2. 确定递推公式

想要求dp[i][j]，只能有两个方向来推导出来，即dp[i - 1][j] 和 dp[i][j - 1]。

此时在回顾一下 dp[i - 1][j] 表示啥，是从(0, 0)的位置到(i - 1, j)有几条路径，dp[i][j - 1]同理。

那么很自然，dp[i][j] = dp[i - 1][j] + dp[i][j - 1]，因为dp[i][j]只有这两个方向过来。

3. dp数组的初始化

如何初始化呢，首先dp[i][0]一定都是1，因为从(0, 0)的位置到(i, 0)的路径只有一条，那么dp[0][j]也同理。

所以初始化代码为：

```text
for (int i = 0; i < m; i++) dp[i][0] = 1;
for (int j = 0; j < n; j++) dp[0][j] = 1;
```

4. 确定遍历顺序

这里要看一下递推公式dp[i][j] = dp[i - 1][j] + dp[i][j - 1]，dp[i][j]都是从其上方和左方推导而来，那么从左到右一层一层遍历就可以了。

这样就可以保证推导dp[i][j]的时候，dp[i - 1][j] 和 dp[i][j - 1]一定是有数值的。

5. 举例推导dp数组

如图所示：

https://code-thinking-1253855093.file.myqcloud.com/pics/20201209113631392.png（图像链接）

以上动规五部曲分析完毕，C++代码如下：

```cpp
class Solution {
public:
    int uniquePaths(int m, int n) {
        vector<vector<int>> dp(m, vector<int>(n, 0));
        for (int i = 0; i < m; i++) dp[i][0] = 1;
        for (int j = 0; j < n; j++) dp[0][j] = 1;
        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1];
            }
        }
        return dp[m - 1][n - 1];
    }
};
```

* 时间复杂度：O(m × n)
* 空间复杂度：O(m × n)

其实用一个一维数组（也可以理解是滚动数组）就可以了，但是不利于理解，可以优化点空间，建议先理解了二维，在理解一维，C++代码如下：

```cpp
class Solution {
public:
    int uniquePaths(int m, int n) {
        vector<int> dp(n);
        for (int i = 0; i < n; i++) dp[i] = 1;
        for (int j = 1; j < m; j++) {
            for (int i = 1; i < n; i++) {
                dp[i] += dp[i - 1];
            }
        }
        return dp[n - 1];
    }
};
```

* 时间复杂度：O(m × n)
* 空间复杂度：O(n)

### 数论方法

在这个图中，可以看出一共m，n的话，无论怎么走，走到终点都需要 m + n - 2 步。

https://code-thinking-1253855093.file.myqcloud.com/pics/20201209113602700-20230310120944078.png（图像链接）

在这m + n - 2 步中，一定有 m - 1 步是要向下走的，不用管什么时候向下走。

那么有几种走法呢？ 可以转化为，给你m + n - 2个不同的数，随便取m - 1个数，有几种取法。

那么这就是一个组合问题了。

那么答案，如图所示：

https://code-thinking-1253855093.file.myqcloud.com/pics/20201209113725324.png（图像链接）

**求组合的时候，要防止两个int相乘溢出！** 所以不能把算式的分子都算出来，分母都算出来再做除法。

例如如下代码是不行的。

```cpp
class Solution {
public:
    int uniquePaths(int m, int n) {
        int numerator = 1, denominator = 1;
        int count = m - 1;
        int t = m + n - 2;
        while (count--) numerator *= (t--); // 计算分子，此时分子就会溢出
        for (int i = 1; i <= m - 1; i++) denominator *= i; // 计算分母
        return numerator / denominator;
    }
};

```

需要在计算分子的时候，不断除以分母，代码如下：

```cpp
class Solution {
public:
    int uniquePaths(int m, int n) {
        long long numerator = 1; // 分子
        int denominator = m - 1; // 分母
        int count = m - 1;
        int t = m + n - 2;
        while (count--) {
            numerator *= (t--);
            while (denominator != 0 && numerator % denominator == 0) {
                numerator /= denominator;
                denominator--;
            }
        }
        return numerator;
    }
};
```

* 时间复杂度：O(m)
* 空间复杂度：O(1)

**计算组合问题的代码还是有难度的，特别是处理溢出的情况！**

## 总结

本文分别给出了深搜，动规，数论三种方法。

深搜当然是超时了，顺便分析了一下使用深搜的时间复杂度，就可以看出为什么超时了。

然后在给出动规的方法，依然是使用动规五部曲，这次我们就要考虑如何正确的初始化了，初始化和遍历顺序其实也很重要！

## 其他语言版本

### Python

递归

```python
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 or n == 1:
            return 1
        return self.uniquePaths(m - 1, n) + self.uniquePaths(m, n - 1)

```

动态规划（版本一）

```python
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # 创建一个二维列表用于存储唯一路径数
        dp = [[0] * n for _ in range(m)]
      
        # 设置第一行和第一列的基本情况
        for i in range(m):
            dp[i][0] = 1
        for j in range(n):
            dp[0][j] = 1
      
        # 计算每个单元格的唯一路径数
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
      
        # 返回右下角单元格的唯一路径数
        return dp[m - 1][n - 1]

```

动态规划（版本二）

```python
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # 创建一个一维列表用于存储每列的唯一路径数
        dp = [1] * n
      
        # 计算每个单元格的唯一路径数
        for j in range(1, m):
            for i in range(1, n):
                dp[i] += dp[i - 1]
      
        # 返回右下角单元格的唯一路径数
        return dp[n - 1]
```

数论

```python
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        numerator = 1  # 分子
        denominator = m - 1  # 分母
        count = m - 1  # 计数器，表示剩余需要计算的乘积项个数
        t = m + n - 2  # 初始乘积项
        while count > 0:
            numerator *= t  # 计算乘积项的分子部分
            t -= 1  # 递减乘积项
            while denominator != 0 and numerator % denominator == 0:
                numerator //= denominator  # 约简分子
                denominator -= 1  # 递减分母
            count -= 1  # 计数器减1，继续下一项的计算
        return numerator  # 返回最终的唯一路径数

```


# 七、63. 不同路径 II

[力扣题目链接(opens new window)](https://leetcode.cn/problems/unique-paths-ii/)

一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。

现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？

网格中的障碍物和空位置分别用 1 和 0 来表示。

示例 1：

https://code-thinking-1253855093.file.myqcloud.com/pics/20210111204939971.png（图像链接）

* 输入：obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
* 输出：2

解释：

* 3x3 网格的正中间有一个障碍物。
* 从左上角到右下角一共有 2 条不同的路径：
  1. 向右 -> 向右 -> 向下 -> 向下
  2. 向下 -> 向下 -> 向右 -> 向右

示例 2：

https://code-thinking-1253855093.file.myqcloud.com/pics/20210111205857918.png（图像链接）

* 输入：obstacleGrid = [[0,1],[0,0]]
* 输出：1

提示：

* m == obstacleGrid.length
* n == obstacleGrid[i].length
* 1 <= m, n <= 100
* obstacleGrid[i][j] 为 0 或 1

## 算法公开课

**[《代码随想录》算法视频公开课 **(opens new window)**](https://programmercarl.com/other/gongkaike.html)：[动态规划，这次遇到障碍了| LeetCode：63. 不同路径 II **(opens new window)**](https://www.bilibili.com/video/BV1Ld4y1k7c6/)，相信结合视频再看本篇题解，更有助于大家对本题的理解**。

## 思路

这道题相对于[62.不同路径 **(opens new window)**](https://programmercarl.com/0062.%E4%B8%8D%E5%90%8C%E8%B7%AF%E5%BE%84.html)就是有了障碍。

第一次接触这种题目的同学可能会有点懵，这有障碍了，应该怎么算呢？

[62.不同路径 **(opens new window)**](https://programmercarl.com/0062.%E4%B8%8D%E5%90%8C%E8%B7%AF%E5%BE%84.html)中我们已经详细分析了没有障碍的情况，有障碍的话，其实就是标记对应的dp table（dp数组）保持初始值(0)就可以了。

动规五部曲：

1. 确定dp数组（dp table）以及下标的含义

dp[i][j] ：表示从（0 ，0）出发，到(i, j) 有dp[i][j]条不同的路径。

2. 确定递推公式

递推公式和62.不同路径一样，dp[i][j] = dp[i - 1][j] + dp[i][j - 1]。

但这里需要注意一点，因为有了障碍，(i, j)如果就是障碍的话应该就保持初始状态（初始状态为0）。

所以代码为：

```cpp
if (obstacleGrid[i][j] == 0) { // 当(i, j)没有障碍的时候，再推导dp[i][j]
    dp[i][j] = dp[i - 1][j] + dp[i][j - 1];
}
```

3. dp数组如何初始化

在[62.不同路径 **(opens new window)**](https://programmercarl.com/0062.%E4%B8%8D%E5%90%8C%E8%B7%AF%E5%BE%84.html)不同路径中我们给出如下的初始化：

```cpp
vector<vector<int>> dp(m, vector<int>(n, 0)); // 初始值为0
for (int i = 0; i < m; i++) dp[i][0] = 1;
for (int j = 0; j < n; j++) dp[0][j] = 1;
```

因为从(0, 0)的位置到(i, 0)的路径只有一条，所以dp[i][0]一定为1，dp[0][j]也同理。

但如果(i, 0) 这条边有了障碍之后，障碍之后（包括障碍）都是走不到的位置了，所以障碍之后的dp[i][0]应该还是初始值0。

如图：

https://code-thinking-1253855093.file.myqcloud.com/pics/20210104114513928.png（图像链接）

下标(0, j)的初始化情况同理。

所以本题初始化代码为：

```cpp
vector<vector<int>> dp(m, vector<int>(n, 0));
for (int i = 0; i < m && obstacleGrid[i][0] == 0; i++) dp[i][0] = 1;
for (int j = 0; j < n && obstacleGrid[0][j] == 0; j++) dp[0][j] = 1;
```

**注意代码里for循环的终止条件，一旦遇到obstacleGrid[i][0] == 1的情况就停止dp[i][0]的赋值1的操作，dp[0][j]同理**

4. 确定遍历顺序

从递归公式dp[i][j] = dp[i - 1][j] + dp[i][j - 1] 中可以看出，一定是从左到右一层一层遍历，这样保证推导dp[i][j]的时候，dp[i - 1][j] 和 dp[i][j - 1]一定是有数值。

代码如下：

```cpp
for (int i = 1; i < m; i++) {
    for (int j = 1; j < n; j++) {
        if (obstacleGrid[i][j] == 1) continue;
        dp[i][j] = dp[i - 1][j] + dp[i][j - 1];
    }
}
```

5. 举例推导dp数组

拿示例1来举例如题：

https://code-thinking-1253855093.file.myqcloud.com/pics/20210104114548983.png（图像链接）

对应的dp table 如图：

https://code-thinking-1253855093.file.myqcloud.com/pics/20210104114610256.png（图像链接）

如果这个图看不懂，建议再理解一下递归公式，然后照着文章中说的遍历顺序，自己推导一下！

动规五部分分析完毕，对应C++代码如下：

```cpp
class Solution {
public:
    int uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid) {
        int m = obstacleGrid.size();
        int n = obstacleGrid[0].size();
        if (obstacleGrid[m - 1][n - 1] == 1 || obstacleGrid[0][0] == 1) //如果在起点或终点出现了障碍，直接返回0
            return 0;
        vector<vector<int>> dp(m, vector<int>(n, 0));
        for (int i = 0; i < m && obstacleGrid[i][0] == 0; i++) dp[i][0] = 1;
        for (int j = 0; j < n && obstacleGrid[0][j] == 0; j++) dp[0][j] = 1;
        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                if (obstacleGrid[i][j] == 1) continue;
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1];
            }
        }
        return dp[m - 1][n - 1];
    }
};
```

* 时间复杂度：O(n × m)，n、m 分别为obstacleGrid 长度和宽度
* 空间复杂度：O(n × m)

同样我们给出空间优化版本：

```cpp
class Solution {
public:
    int uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid) {
        if (obstacleGrid[0][0] == 1)
            return 0;
        vector<int> dp(obstacleGrid[0].size());
        for (int j = 0; j < dp.size(); ++j)
            if (obstacleGrid[0][j] == 1)
                dp[j] = 0;
            else if (j == 0)
                dp[j] = 1;
            else
                dp[j] = dp[j-1];

        for (int i = 1; i < obstacleGrid.size(); ++i)
            for (int j = 0; j < dp.size(); ++j){
                if (obstacleGrid[i][j] == 1)
                    dp[j] = 0;
                else if (j != 0)
                    dp[j] = dp[j] + dp[j-1];
            }
        return dp.back();
    }
};
```

* 时间复杂度：O(n × m)，n、m 分别为obstacleGrid 长度和宽度
* 空间复杂度：O(m)

## 总结

本题是[62.不同路径 **(opens new window)**](https://programmercarl.com/0062.%E4%B8%8D%E5%90%8C%E8%B7%AF%E5%BE%84.html)的障碍版，整体思路大体一致。

但就算是做过62.不同路径，在做本题也会有感觉遇到障碍无从下手。

其实只要考虑到，遇到障碍dp[i][j]保持0就可以了。

也有一些小细节，例如：初始化的部分，很容易忽略了障碍之后应该都是0的情况。

## 其他语言版本

### Python

动态规划（版本一）

```python
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        if obstacleGrid[m - 1][n - 1] == 1 or obstacleGrid[0][0] == 1:
            return 0
        dp = [[0] * n for _ in range(m)]
        for i in range(m):
            if obstacleGrid[i][0] == 0:  # 遇到障碍物时，直接退出循环，后面默认都是0
                dp[i][0] = 1
            else:
                break
        for j in range(n):
            if obstacleGrid[0][j] == 0:
                dp[0][j] = 1
            else:
                break
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    continue
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[m - 1][n - 1]

```

动态规划（版本二）

```python
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        m = len(obstacleGrid)  # 网格的行数
        n = len(obstacleGrid[0])  # 网格的列数
      
        if obstacleGrid[m - 1][n - 1] == 1 or obstacleGrid[0][0] == 1:
            # 如果起点或终点有障碍物，直接返回0
            return 0
      
        dp = [[0] * n for _ in range(m)]  # 创建一个二维列表用于存储路径数
      
        # 设置起点的路径数为1
        dp[0][0] = 1 if obstacleGrid[0][0] == 0 else 0
      
        # 计算第一列的路径数
        for i in range(1, m):
            if obstacleGrid[i][0] == 0:
                dp[i][0] = dp[i - 1][0]
      
        # 计算第一行的路径数
        for j in range(1, n):
            if obstacleGrid[0][j] == 0:
                dp[0][j] = dp[0][j - 1]
      
        # 计算其他位置的路径数
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    continue
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
      
        return dp[m - 1][n - 1]  # 返回终点的路径数


```

动态规划（版本三）

```python
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        if obstacleGrid[0][0] == 1:
            return 0
      
        dp = [0] * len(obstacleGrid[0])  # 创建一个一维列表用于存储路径数
      
        # 初始化第一行的路径数
        for j in range(len(dp)):
            if obstacleGrid[0][j] == 1:
                dp[j] = 0
            elif j == 0:
                dp[j] = 1
            else:
                dp[j] = dp[j - 1]

        # 计算其他行的路径数
        for i in range(1, len(obstacleGrid)):
            for j in range(len(dp)):
                if obstacleGrid[i][j] == 1:
                    dp[j] = 0
                elif j != 0:
                    dp[j] = dp[j] + dp[j - 1]
      
        return dp[-1]  # 返回最后一个元素，即终点的路径数

```

动态规划（版本四）

```python
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        if obstacleGrid[0][0] == 1:
            return 0
      
        m, n = len(obstacleGrid), len(obstacleGrid[0])
      
        dp = [0] * n  # 创建一个一维列表用于存储路径数
      
        # 初始化第一行的路径数
        for j in range(n):
            if obstacleGrid[0][j] == 1:
                break
            dp[j] = 1

        # 计算其他行的路径数
        for i in range(1, m):
            if obstacleGrid[i][0] == 1:
                dp[0] = 0
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    dp[j] = 0
                else:
                    dp[j] += dp[j - 1]
      
        return dp[-1]  # 返回最后一个元素，即终点的路径数

```

动态规划（版本五）

```python
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        if obstacleGrid[0][0] == 1:
            return 0
      
        m, n = len(obstacleGrid), len(obstacleGrid[0])
      
        dp = [0] * n  # 创建一个一维列表用于存储路径数
      
        # 初始化第一行的路径数
        for j in range(n):
            if obstacleGrid[0][j] == 1:
                break
            dp[j] = 1

        # 计算其他行的路径数
        for i in range(1, m):
            if obstacleGrid[i][0] == 1:
                dp[0] = 0
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    dp[j] = 0
                    continue
              
                dp[j] += dp[j - 1]
      
        return dp[-1]  # 返回最后一个元素，即终点的路径数


```

