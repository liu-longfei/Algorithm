# 一、关于贪心算法，你该了解这些！

题目分类大纲如下：

https://code-thinking-1253855093.file.myqcloud.com/pics/20210917104315.png（图像链接）

## 算法公开课

[《代码随想录》算法视频公开课 **(opens new window)**](https://programmercarl.com/other/gongkaike.html)：[贪心算法理论基础！ **(opens new window)**](https://www.bilibili.com/video/BV1WK4y1R71x/),**相信结合视频再看本篇题解，更有助于大家对本题的理解**。

## 什么是贪心

**贪心的本质是选择每一阶段的局部最优，从而达到全局最优**。

这么说有点抽象，来举一个例子：

例如，有一堆钞票，你可以拿走十张，如果想达到最大的金额，你要怎么拿？

指定每次拿最大的，最终结果就是拿走最大数额的钱。

每次拿最大的就是局部最优，最后拿走最大数额的钱就是推出全局最优。

再举一个例子如果是 有一堆盒子，你有一个背包体积为n，如何把背包尽可能装满，如果还每次选最大的盒子，就不行了。这时候就需要动态规划。动态规划的问题在下一个系列会详细讲解。

## 贪心的套路（什么时候用贪心）

很多同学做贪心的题目的时候，想不出来是贪心，想知道有没有什么套路可以一看就看出来是贪心。

**说实话贪心算法并没有固定的套路**。

所以唯一的难点就是如何通过局部最优，推出整体最优。

那么如何能看出局部最优是否能推出整体最优呢？有没有什么固定策略或者套路呢？

**不好意思，也没有！** 靠自己手动模拟，如果模拟可行，就可以试一试贪心策略，如果不可行，可能需要动态规划。

有同学问了如何验证可不可以用贪心算法呢？

**最好用的策略就是举反例，如果想不到反例，那么就试一试贪心吧**。

可有同学认为手动模拟，举例子得出的结论不靠谱，想要严格的数学证明。

一般数学证明有如下两种方法：

* 数学归纳法
* 反证法

看教课书上讲解贪心可以是一堆公式，估计大家连看都不想看，所以数学证明就不在我要讲解的范围内了，大家感兴趣可以自行查找资料。

**面试中基本不会让面试者现场证明贪心的合理性，代码写出来跑过测试用例即可，或者自己能自圆其说理由就行了**。

举一个不太恰当的例子：我要用一下1+1 = 2，但我要先证明1+1 为什么等于2。严谨是严谨了，但没必要。

虽然这个例子很极端，但可以表达这么个意思：**刷题或者面试的时候，手动模拟一下感觉可以局部最优推出整体最优，而且想不到反例，那么就试一试贪心**。

**例如刚刚举的拿钞票的例子，就是模拟一下每次拿做大的，最后就能拿到最多的钱，这还要数学证明的话，其实就不在算法面试的范围内了，可以看看专业的数学书籍！**

所以这也是为什么很多同学通过（accept）了贪心的题目，但都不知道自己用了贪心算法，**因为贪心有时候就是常识性的推导，所以会认为本应该就这么做！**

**那么刷题的时候什么时候真的需要数学推导呢？**

例如这道题目：[链表：环找到了，那入口呢？ **(opens new window)**](https://programmercarl.com/0142.%E7%8E%AF%E5%BD%A2%E9%93%BE%E8%A1%A8II.html)，这道题不用数学推导一下，就找不出环的起始位置，想试一下就不知道怎么试，这种题目确实需要数学简单推导一下。

## 贪心一般解题步骤

贪心算法一般分为如下四步：

* 将问题分解为若干个子问题
* 找出适合的贪心策略
* 求解每一个子问题的最优解
* 将局部最优解堆叠成全局最优解

这个四步其实过于理论化了，我们平时在做贪心类的题目 很难去按照这四步去思考，真是有点“鸡肋”。

做题的时候，只要想清楚 局部最优 是什么，如果推导出全局最优，其实就够了。

## 总结

本篇给出了什么是贪心以及大家关心的贪心算法固定套路。

**不好意思了，贪心没有套路，说白了就是常识性推导加上举反例**。

最后给出贪心的一般解题步骤，大家可以发现这个解题步骤也是比较抽象的，不像是二叉树，回溯算法，给出了那么具体的解题套路和模板。

# 二、455.分发饼干

[力扣题目链接(opens new window)](https://leetcode.cn/problems/assign-cookies/)

假设你是一位很棒的家长，想要给你的孩子们一些小饼干。但是，每个孩子最多只能给一块饼干。

对每个孩子 i，都有一个胃口值  g[i]，这是能让孩子们满足胃口的饼干的最小尺寸；并且每块饼干 j，都有一个尺寸 s[j] 。如果 s[j] >= g[i]，我们可以将这个饼干 j 分配给孩子 i ，这个孩子会得到满足。你的目标是尽可能满足越多数量的孩子，并输出这个最大数值。

示例  1:

* 输入: g = [1,2,3], s = [1,1]
* 输出: 1 解释:你有三个孩子和两块小饼干，3 个孩子的胃口值分别是：1,2,3。虽然你有两块小饼干，由于他们的尺寸都是 1，你只能让胃口值是 1 的孩子满足。所以你应该输出 1。

示例  2:

* 输入: g = [1,2], s = [1,2,3]
* 输出: 2
* 解释:你有两个孩子和三块小饼干，2 个孩子的胃口值分别是 1,2。你拥有的饼干数量和尺寸都足以让所有孩子满足。所以你应该输出 2.

提示：

* 1 <= g.length <= 3 \* 10^4
* 0 <= s.length <= 3 \* 10^4
* 1 <= g[i], s[j] <= 2^31 - 1

## 算法公开课

[《代码随想录》算法视频公开课 **(opens new window)**](https://programmercarl.com/other/gongkaike.html)：[贪心算法，你想先喂哪个小孩？| LeetCode：455.分发饼干 **(opens new window)**](https://www.bilibili.com/video/BV1MM411b7cq)，**相信结合视频在看本篇题解，更有助于大家对本题的理解**。

## 思路

为了满足更多的小孩，就不要造成饼干尺寸的浪费。

大尺寸的饼干既可以满足胃口大的孩子也可以满足胃口小的孩子，那么就应该优先满足胃口大的。

**这里的局部最优就是大饼干喂给胃口大的，充分利用饼干尺寸喂饱一个，全局最优就是喂饱尽可能多的小孩**。

可以尝试使用贪心策略，先将饼干数组和小孩数组排序。

然后从后向前遍历小孩数组，用大饼干优先满足胃口大的，并统计满足小孩数量。

如图：

https://code-thinking-1253855093.file.myqcloud.com/pics/20230405225628.png（图像链接）

这个例子可以看出饼干 9 只有喂给胃口为 7 的小孩，这样才是整体最优解，并想不出反例，那么就可以撸代码了。

C++代码整体如下：

```cpp
// 版本一
class Solution {
public:
    int findContentChildren(vector<int>& g, vector<int>& s) {
        sort(g.begin(), g.end());
        sort(s.begin(), s.end());
        int index = s.size() - 1; // 饼干数组的下标
        int result = 0;
        for (int i = g.size() - 1; i >= 0; i--) { // 遍历胃口
            if (index >= 0 && s[index] >= g[i]) { // 遍历饼干
                result++;
                index--;
            }
        }
        return result;
    }
};
```

* 时间复杂度：O(nlogn)
* 空间复杂度：O(1)

从代码中可以看出我用了一个 index 来控制饼干数组的遍历，遍历饼干并没有再起一个 for 循环，而是采用自减的方式，这也是常用的技巧。

有的同学看到要遍历两个数组，就想到用两个 for 循环，那样逻辑其实就复杂了。

### 注意事项

注意版本一的代码中，可以看出来，是先遍历的胃口，在遍历的饼干，那么可不可以 先遍历 饼干，在遍历胃口呢？

其实是不可以的。

外面的 for 是里的下标 i 是固定移动的，而 if 里面的下标 index 是符合条件才移动的。

如果 for 控制的是饼干， if 控制胃口，就是出现如下情况 ：

https://code-thinking-1253855093.file.myqcloud.com/pics/20230112102848.png（图像链接）

if 里的 index 指向 胃口 10， for 里的 i 指向饼干 9，因为 饼干 9 满足不了 胃口 10，所以 i 持续向前移动，而 index 走不到`s[index] >= g[i]` 的逻辑，所以 index 不会移动，那么当 i 持续向前移动，最后所有的饼干都匹配不上。

所以 一定要 for 控制 胃口，里面的 if 控制饼干。

### 其他思路

**也可以换一个思路，小饼干先喂饱小胃口**

代码如下：

```cpp
class Solution {
public:
    int findContentChildren(vector<int>& g, vector<int>& s) {
        sort(g.begin(),g.end());
        sort(s.begin(),s.end());
        int index = 0;
        for(int i = 0; i < s.size(); i++) { // 饼干
            if(index < g.size() && g[index] <= s[i]){ // 胃口
                index++;
            }
        }
        return index;
    }
};
```

* 时间复杂度：O(nlogn)
* 空间复杂度：O(1)

细心的录友可以发现，这种写法，两个循环的顺序改变了，先遍历的饼干，在遍历的胃口，这是因为遍历顺序变了，我们是从小到大遍历。

理由在上面 “注意事项”中 已经讲过。

## 总结

这道题是贪心很好的一道入门题目，思路还是比较容易想到的。

文中详细介绍了思考的过程，**想清楚局部最优，想清楚全局最优，感觉局部最优是可以推出全局最优，并想不出反例，那么就试一试贪心**。

## 其他语言版本

### Python

贪心 大饼干优先

```python
class Solution:
    def findContentChildren(self, g, s):
        g.sort()  # 将孩子的贪心因子排序
        s.sort()  # 将饼干的尺寸排序
        index = len(s) - 1  # 饼干数组的下标，从最后一个饼干开始
        result = 0  # 满足孩子的数量
        for i in range(len(g)-1, -1, -1):  # 遍历胃口，从最后一个孩子开始
            if index >= 0 and s[index] >= g[i]:  # 遍历饼干
                result += 1
                index -= 1
        return result

```

贪心 小饼干优先

```python
class Solution:
    def findContentChildren(self, g, s):
        g.sort()  # 将孩子的贪心因子排序
        s.sort()  # 将饼干的尺寸排序
        index = 0
        for i in range(len(s)):  # 遍历饼干
            if index < len(g) and g[index] <= s[i]:  # 如果当前孩子的贪心因子小于等于当前饼干尺寸
                index += 1  # 满足一个孩子，指向下一个孩子
        return index  # 返回满足的孩子数目

```

# 三、376. 摆动序列

[力扣题目链接(opens new window)](https://leetcode.cn/problems/wiggle-subsequence/)

如果连续数字之间的差严格地在正数和负数之间交替，则数字序列称为摆动序列。第一个差（如果存在的话）可能是正数或负数。少于两个元素的序列也是摆动序列。

例如， [1,7,4,9,2,5] 是一个摆动序列，因为差值 (6,-3,5,-7,3)  是正负交替出现的。相反, [1,4,7,2,5]  和  [1,7,4,5,5] 不是摆动序列，第一个序列是因为它的前两个差值都是正数，第二个序列是因为它的最后一个差值为零。

给定一个整数序列，返回作为摆动序列的最长子序列的长度。 通过从原始序列中删除一些（也可以不删除）元素来获得子序列，剩下的元素保持其原始顺序。

示例 1:

* 输入: [1,7,4,9,2,5]
* 输出: 6
* 解释: 整个序列均为摆动序列。

示例 2:

* 输入: [1,17,5,10,13,15,10,5,16,8]
* 输出: 7
* 解释: 这个序列包含几个长度为 7 摆动序列，其中一个可为[1,17,10,13,10,16,8]。

示例 3:

* 输入: [1,2,3,4,5,6,7,8,9]
* 输出: 2

## 算法公开课

[《代码随想录》算法视频公开课 **(opens new window)**](https://programmercarl.com/other/gongkaike.html)：[贪心算法，寻找摆动有细节！| LeetCode：376.摆动序列 **(opens new window)**](https://www.bilibili.com/video/BV17M411b7NS)，**相信结合视频在看本篇题解，更有助于大家对本题的理解**。

## 思路

### 思路 1（贪心解法）

本题要求通过从原始序列中删除一些（也可以不删除）元素来获得子序列，剩下的元素保持其原始顺序。

相信这么一说吓退不少同学，这要求最大摆动序列又可以修改数组，这得如何修改呢？

来分析一下，要求删除元素使其达到最大摆动序列，应该删除什么元素呢？

用示例二来举例，如图所示：

https://code-thinking-1253855093.file.myqcloud.com/pics/20201124174327597.png（图像链接）

**局部最优：删除单调坡度上的节点（不包括单调坡度两端的节点），那么这个坡度就可以有两个局部峰值**。

**整体最优：整个序列有最多的局部峰值，从而达到最长摆动序列**。

局部最优推出全局最优，并举不出反例，那么试试贪心！

（为方便表述，以下说的峰值都是指局部峰值）

**实际操作上，其实连删除的操作都不用做，因为题目要求的是最长摆动子序列的长度，所以只需要统计数组的峰值数量就可以了（相当于是删除单一坡度上的节点，然后统计长度）**

**这就是贪心所贪的地方，让峰值尽可能的保持峰值，然后删除单一坡度上的节点**

在计算是否有峰值的时候，大家知道遍历的下标 i ，计算 prediff（nums[i] - nums[i-1]） 和 curdiff（nums[i+1] - nums[i]），如果`prediff < 0 && curdiff > 0` 或者 `prediff > 0 && curdiff < 0` 此时就有波动就需要统计。

这是我们思考本题的一个大体思路，但本题要考虑三种情况：

1. 情况一：上下坡中有平坡
2. 情况二：数组首尾两端
3. 情况三：单调坡中有平坡

#### 情况一：上下坡中有平坡

例如 [1,2,2,2,1]这样的数组，如图：

https://code-thinking-1253855093.file.myqcloud.com/pics/20230106170449.png（图像链接）

它的摇摆序列长度是多少呢？ **其实是长度是 3**，也就是我们在删除的时候 要不删除左面的三个 2，要不就删除右边的三个 2。

如图，可以统一规则，删除左边的三个 2：

https://code-thinking-1253855093.file.myqcloud.com/pics/20230106172613.png（图像链接）

在图中，当 i 指向第一个 2 的时候，`prediff > 0 && curdiff = 0` ，当 i 指向最后一个 2 的时候 `prediff = 0 && curdiff < 0`。

如果我们采用，删左面三个 2 的规则，那么 当 `prediff = 0 && curdiff < 0` 也要记录一个峰值，因为他是把之前相同的元素都删掉留下的峰值。

所以我们记录峰值的条件应该是： `(preDiff <= 0 && curDiff > 0) || (preDiff >= 0 && curDiff < 0)`，为什么这里允许 prediff == 0 ，就是为了 上面我说的这种情况。

#### 情况二：数组首尾两端

所以本题统计峰值的时候，数组最左面和最右面如何统计呢？

题目中说了，如果只有两个不同的元素，那摆动序列也是 2。

例如序列[2,5]，如果靠统计差值来计算峰值个数就需要考虑数组最左面和最右面的特殊情况。

因为我们在计算 prediff（nums[i] - nums[i-1]） 和 curdiff（nums[i+1] - nums[i]）的时候，至少需要三个数字才能计算，而数组只有两个数字。

这里我们可以写死，就是 如果只有两个元素，且元素不同，那么结果为 2。

不写死的话，如何和我们的判断规则结合在一起呢？

可以假设，数组最前面还有一个数字，那这个数字应该是什么呢？

之前我们在 讨论 情况一：相同数字连续 的时候， prediff = 0 ，curdiff < 0 或者 >0 也记为波谷。

那么为了规则统一，针对序列[2,5]，可以假设为[2,2,5]，这样它就有坡度了即 preDiff = 0，如图：

https://code-thinking-1253855093.file.myqcloud.com/pics/20201124174357612.png（图像链接）

针对以上情形，result 初始为 1（默认最右面有一个峰值），此时 curDiff > 0 && preDiff <= 0，那么 result++（计算了左面的峰值），最后得到的 result 就是 2（峰值个数为 2 即摆动序列长度为 2）

经过以上分析后，我们可以写出如下代码：

```cpp
// 版本一
class Solution {
public:
    int wiggleMaxLength(vector<int>& nums) {
        if (nums.size() <= 1) return nums.size();
        int curDiff = 0; // 当前一对差值
        int preDiff = 0; // 前一对差值
        int result = 1;  // 记录峰值个数，序列默认序列最右边有一个峰值
        for (int i = 0; i < nums.size() - 1; i++) {
            curDiff = nums[i + 1] - nums[i];
            // 出现峰值
            if ((preDiff <= 0 && curDiff > 0) || (preDiff >= 0 && curDiff < 0)) {
                result++;
            }
            preDiff = curDiff;
        }
        return result;
    }
};
```

* 时间复杂度：O(n)
* 空间复杂度：O(1)

此时大家是不是发现 以上代码提交也不能通过本题？

所以此时我们要讨论情况三！

#### 情况三：单调坡度有平坡

在版本一中，我们忽略了一种情况，即 如果在一个单调坡度上有平坡，例如[1,2,2,2,3,4]，如图：

https://code-thinking-1253855093.file.myqcloud.com/pics/20230108171505.png（图像链接）

图中，我们可以看出，版本一的代码在三个地方记录峰值，但其实结果因为是 2，因为 单调中的平坡 不能算峰值（即摆动）。

之所以版本一会出问题，是因为我们实时更新了 prediff。

那么我们应该什么时候更新 prediff 呢？

我们只需要在 这个坡度 摆动变化的时候，更新 prediff 就行，这样 prediff 在 单调区间有平坡的时候 就不会发生变化，造成我们的误判。

所以本题的最终代码为：

```cpp

// 版本二
class Solution {
public:
    int wiggleMaxLength(vector<int>& nums) {
        if (nums.size() <= 1) return nums.size();
        int curDiff = 0; // 当前一对差值
        int preDiff = 0; // 前一对差值
        int result = 1;  // 记录峰值个数，序列默认序列最右边有一个峰值
        for (int i = 0; i < nums.size() - 1; i++) {
            curDiff = nums[i + 1] - nums[i];
            // 出现峰值
            if ((preDiff <= 0 && curDiff > 0) || (preDiff >= 0 && curDiff < 0)) {
                result++;
                preDiff = curDiff; // 注意这里，只在摆动变化的时候更新prediff
            }
        }
        return result;
    }
};
```

其实本题看起来好像简单，但需要考虑的情况还是很复杂的，而且很难一次性想到位。

**本题异常情况的本质，就是要考虑平坡**， 平坡分两种，一个是 上下中间有平坡，一个是单调有平坡，如图：

https://code-thinking-1253855093.file.myqcloud.com/pics/20230108174452.png（图像链接）

### 思路 2（动态规划）

考虑用动态规划的思想来解决这个问题。

很容易可以发现，对于我们当前考虑的这个数，要么是作为山峰（即 nums[i] > nums[i-1]），要么是作为山谷（即 nums[i] < nums[i - 1]）。

* 设 dp 状态`dp[i][0]`，表示考虑前 i 个数，第 i 个数作为山峰的摆动子序列的最长长度
* 设 dp 状态`dp[i][1]`，表示考虑前 i 个数，第 i 个数作为山谷的摆动子序列的最长长度

则转移方程为：

* `dp[i][0] = max(dp[i][0], dp[j][1] + 1)`，其中`0 < j < i`且`nums[j] < nums[i]`，表示将 nums[i]接到前面某个山谷后面，作为山峰。
* `dp[i][1] = max(dp[i][1], dp[j][0] + 1)`，其中`0 < j < i`且`nums[j] > nums[i]`，表示将 nums[i]接到前面某个山峰后面，作为山谷。

初始状态：

由于一个数可以接到前面的某个数后面，也可以以自身为子序列的起点，所以初始状态为：`dp[0][0] = dp[0][1] = 1`。

C++代码如下：

```cpp
class Solution {
public:
    int dp[1005][2];
    int wiggleMaxLength(vector<int>& nums) {
        memset(dp, 0, sizeof dp);
        dp[0][0] = dp[0][1] = 1;
        for (int i = 1; i < nums.size(); ++i) {
            dp[i][0] = dp[i][1] = 1;
            for (int j = 0; j < i; ++j) {
                if (nums[j] > nums[i]) dp[i][1] = max(dp[i][1], dp[j][0] + 1);
            }
            for (int j = 0; j < i; ++j) {
                if (nums[j] < nums[i]) dp[i][0] = max(dp[i][0], dp[j][1] + 1);
            }
        }
        return max(dp[nums.size() - 1][0], dp[nums.size() - 1][1]);
    }
};
```

* 时间复杂度：O(n^2)
* 空间复杂度：O(n)

**进阶**

可以用两棵线段树来维护区间的最大值

* 每次更新`dp[i][0]`，则在`tree1`的`nums[i]`位置值更新为`dp[i][0]`
* 每次更新`dp[i][1]`，则在`tree2`的`nums[i]`位置值更新为`dp[i][1]`
* 则 dp 转移方程中就没有必要 j 从 0 遍历到 i-1，可以直接在线段树中查询指定区间的值即可。

时间复杂度：O(nlog n)

空间复杂度：O(n)

## 其他语言版本

### Python

贪心（版本一）

```python
class Solution:
    def wiggleMaxLength(self, nums):
        if len(nums) <= 1:
            return len(nums)  # 如果数组长度为0或1，则返回数组长度
        curDiff = 0  # 当前一对元素的差值
        preDiff = 0  # 前一对元素的差值
        result = 1  # 记录峰值的个数，初始为1（默认最右边的元素被视为峰值）
        for i in range(len(nums) - 1):
            curDiff = nums[i + 1] - nums[i]  # 计算下一个元素与当前元素的差值
            # 如果遇到一个峰值
            if (preDiff <= 0 and curDiff > 0) or (preDiff >= 0 and curDiff < 0):
                result += 1  # 峰值个数加1
                preDiff = curDiff  # 注意这里，只在摆动变化的时候更新preDiff
        return result  # 返回最长摆动子序列的长度

```

贪心（版本二）

```python
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)  # 如果数组长度为0或1，则返回数组长度
        preDiff,curDiff ,result  = 0,0,1  #题目里nums长度大于等于1，当长度为1时，其实到不了for循环里去，所以不用考虑nums长度
        for i in range(len(nums) - 1):
            curDiff = nums[i + 1] - nums[i]
            if curDiff * preDiff <= 0 and curDiff !=0:  #差值为0时，不算摆动
                result += 1
                preDiff = curDiff  #如果当前差值和上一个差值为一正一负时，才需要用当前差值替代上一个差值
        return result

```

动态规划（版本一）

```python
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        # 0 i 作为波峰的最大长度
        # 1 i 作为波谷的最大长度
        # dp是一个列表，列表中每个元素是长度为 2 的列表
        dp = []
        for i in range(len(nums)):
            # 初始为[1, 1]
            dp.append([1, 1])
            for j in range(i):
                # nums[i] 为波谷
                if nums[j] > nums[i]:
                    dp[i][1] = max(dp[i][1], dp[j][0] + 1)
                # nums[i] 为波峰
                if nums[j] < nums[i]:
                    dp[i][0] = max(dp[i][0], dp[j][1] + 1)
        return max(dp[-1][0], dp[-1][1])
```

动态规划（版本二）

```python
class Solution:
    def wiggleMaxLength(self, nums):
        dp = [[0, 0] for _ in range(len(nums))]  # 创建二维dp数组，用于记录摆动序列的最大长度
        dp[0][0] = dp[0][1] = 1  # 初始条件，序列中的第一个元素默认为峰值，最小长度为1
        for i in range(1, len(nums)):
            dp[i][0] = dp[i][1] = 1  # 初始化当前位置的dp值为1
            for j in range(i):
                if nums[j] > nums[i]:
                    dp[i][1] = max(dp[i][1], dp[j][0] + 1)  # 如果前一个数比当前数大，可以形成一个上升峰值，更新dp[i][1]
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i][0] = max(dp[i][0], dp[j][1] + 1)  # 如果前一个数比当前数小，可以形成一个下降峰值，更新dp[i][0]
        return max(dp[-1][0], dp[-1][1])  # 返回最大的摆动序列长度

```

动态规划（版本三）优化

```python
class Solution:
    def wiggleMaxLength(self, nums):
        if len(nums) <= 1:
            return len(nums)  # 如果数组长度为0或1，则返回数组长度
    
        up = down = 1  # 记录上升和下降摆动序列的最大长度
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                up = down + 1  # 如果当前数比前一个数大，则可以形成一个上升峰值
            elif nums[i] < nums[i-1]:
                down = up + 1  # 如果当前数比前一个数小，则可以形成一个下降峰值
    
        return max(up, down)  # 返回上升和下降摆动序列的最大长度


```


# 四、53. 最大子序和

[力扣题目链接(opens new window)](https://leetcode.cn/problems/maximum-subarray/)

给定一个整数数组 nums，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

示例:

* 输入: [-2,1,-3,4,-1,2,1,-5,4]
* 输出: 6
* 解释:  连续子数组  [4,-1,2,1] 的和最大，为  6。

## 算法公开课

[《代码随想录》算法视频公开课 **(opens new window)**](https://programmercarl.com/other/gongkaike.html)：[贪心算法的巧妙需要慢慢体会！LeetCode：53. 最大子序和 **(opens new window)**](https://www.bilibili.com/video/BV1aY4y1Z7ya)，**相信结合视频在看本篇题解，更有助于大家对本题的理解**。

## 思路

### 暴力解法

暴力解法的思路，第一层 for 就是设置起始位置，第二层 for 循环遍历数组寻找最大值

```cpp
class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int result = INT32_MIN;
        int count = 0;
        for (int i = 0; i < nums.size(); i++) { // 设置起始位置
            count = 0;
            for (int j = i; j < nums.size(); j++) { // 每次从起始位置i开始遍历寻找最大值
                count += nums[j];
                result = count > result ? count : result;
            }
        }
        return result;
    }
};
```

* 时间复杂度：O(n^2)
* 空间复杂度：O(1)

以上暴力的解法 C++勉强可以过，其他语言就不确定了。

### 贪心解法

**贪心贪的是哪里呢？**

如果 -2 1 在一起，计算起点的时候，一定是从 1 开始计算，因为负数只会拉低总和，这就是贪心贪的地方！

局部最优：当前“连续和”为负数的时候立刻放弃，从下一个元素重新计算“连续和”，因为负数加上下一个元素 “连续和”只会越来越小。

全局最优：选取最大“连续和”

**局部最优的情况下，并记录最大的“连续和”，可以推出全局最优**。

从代码角度上来讲：遍历 nums，从头开始用 count 累积，如果 count 一旦加上 nums[i]变为负数，那么就应该从 nums[i+1]开始从 0 累积 count 了，因为已经变为负数的 count，只会拖累总和。

**这相当于是暴力解法中的不断调整最大子序和区间的起始位置**。

**那有同学问了，区间终止位置不用调整么？ 如何才能得到最大“连续和”呢？**

区间的终止位置，其实就是如果 count 取到最大值了，及时记录下来了。例如如下代码：

```text
if (count > result) result = count;
```

**这样相当于是用 result 记录最大子序和区间和（变相的算是调整了终止位置）**。

如动画所示：

https://code-thinking.cdn.bcebos.com/gifs/53.%E6%9C%80%E5%A4%A7%E5%AD%90%E5%BA%8F%E5%92%8C.gif（图像链接）

红色的起始位置就是贪心每次取 count 为正数的时候，开始一个区间的统计。

那么不难写出如下 C++代码（关键地方已经注释）

```cpp
class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int result = INT32_MIN;
        int count = 0;
        for (int i = 0; i < nums.size(); i++) {
            count += nums[i];
            if (count > result) { // 取区间累计的最大值（相当于不断确定最大子序终止位置）
                result = count;
            }
            if (count <= 0) count = 0; // 相当于重置最大子序起始位置，因为遇到负数一定是拉低总和
        }
        return result;
    }
};
```

* 时间复杂度：O(n)
* 空间复杂度：O(1)

当然题目没有说如果数组为空，应该返回什么，所以数组为空的话返回啥都可以了。

### 常见误区

误区一：

不少同学认为 如果输入用例都是-1，或者 都是负数，这个贪心算法跑出来的结果是 0， 这是**又一次证明脑洞模拟不靠谱的经典案例**，建议大家把代码运行一下试一试，就知道了，也会理解 为什么 result 要初始化为最小负数了。

误区二：

大家在使用贪心算法求解本题，经常陷入的误区，就是分不清，是遇到 负数就选择起始位置，还是连续和为负选择起始位置。

在动画演示用，大家可以发现， 4，遇到 -1 的时候，我们依然累加了，为什么呢？

因为和为 3，只要连续和还是正数就会 对后面的元素 起到增大总和的作用。 所以只要连续和为正数我们就保留。

这里也会有录友疑惑，那 4 + -1 之后 不就变小了吗？ 会不会错过 4 成为最大连续和的可能性？

其实并不会，因为还有一个变量 result 一直在更新 最大的连续和，只要有更大的连续和出现，result 就更新了，那么 result 已经把 4 更新了，后面 连续和变成 3，也不会对最后结果有影响。

### 动态规划

当然本题还可以用动态规划来做，在代码随想录动态规划章节我会详细介绍，如果大家想在想看，可以直接跳转：[动态规划版本详解(opens new window)](https://programmercarl.com/0053.%E6%9C%80%E5%A4%A7%E5%AD%90%E5%BA%8F%E5%92%8C%EF%BC%88%E5%8A%A8%E6%80%81%E8%A7%84%E5%88%92%EF%BC%89.html#%E6%80%9D%E8%B7%AF)

那么先给出我的 dp 代码如下，有时间的录友可以提前做一做：

```cpp
class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        if (nums.size() == 0) return 0;
        vector<int> dp(nums.size(), 0); // dp[i]表示包括i之前的最大连续子序列和
        dp[0] = nums[0];
        int result = dp[0];
        for (int i = 1; i < nums.size(); i++) {
            dp[i] = max(dp[i - 1] + nums[i], nums[i]); // 状态转移公式
            if (dp[i] > result) result = dp[i]; // result 保存dp[i]的最大值
        }
        return result;
    }
};
```

* 时间复杂度：O(n)
* 空间复杂度：O(n)

## 总结

本题的贪心思路其实并不好想，这也进一步验证了，别看贪心理论很直白，有时候看似是常识，但贪心的题目一点都不简单！

后续将介绍的贪心题目都挺难的，所以贪心很有意思，别小看贪心！

## 其他语言版本

### Python

暴力法

```python
class Solution:
    def maxSubArray(self, nums):
        result = float('-inf')  # 初始化结果为负无穷大
        count = 0
        for i in range(len(nums)):  # 设置起始位置
            count = 0
            for j in range(i, len(nums)):  # 从起始位置i开始遍历寻找最大值
                count += nums[j]
                result = max(count, result)  # 更新最大值
        return result

```

```python
class Solution:
    def maxSubArray(self, nums):
        result = float('-inf')  # 初始化结果为负无穷大
        count = 0
        for i in range(len(nums)):
            count += nums[i]
            if count > result:  # 取区间累计的最大值（相当于不断确定最大子序终止位置）
                result = count
            if count <= 0:  # 相当于重置最大子序起始位置，因为遇到负数一定是拉低总和
                count = 0
        return result


```


# 五、本周小结！（贪心算法系列一）

## 周一

本周正式开始了贪心算法，在[关于贪心算法，你该了解这些！ **(opens new window)**](https://programmercarl.com/%E8%B4%AA%E5%BF%83%E7%AE%97%E6%B3%95%E7%90%86%E8%AE%BA%E5%9F%BA%E7%A1%80.html)中，我们介绍了什么是贪心以及贪心的套路。

**贪心的本质是选择每一阶段的局部最优，从而达到全局最优。**

有没有啥套路呢？

**不好意思，贪心没套路，就刷题而言，如果感觉好像局部最优可以推出全局最优，然后想不到反例，那就试一试贪心吧！**

而严格的数据证明一般有如下两种：

* 数学归纳法
* 反证法

数学就不在讲解范围内了，感兴趣的同学可以自己去查一查资料。

正是因为贪心算法有时候会感觉这是常识，本就应该这么做！ 所以大家经常看到网上有人说这是一道贪心题目，有人说这不是。

这里说一下我的依据：**如果找到局部最优，然后推出整体最优，那么就是贪心**，大家可以参考哈。

## 周二

在[贪心算法：分发饼干 **(opens new window)**](https://programmercarl.com/0455.%E5%88%86%E5%8F%91%E9%A5%BC%E5%B9%B2.html)中讲解了贪心算法的第一道题目。

这道题目很明显能看出来是用贪心，也是入门好题。

我在文中给出**局部最优：大饼干喂给胃口大的，充分利用饼干尺寸喂饱一个，全局最优：喂饱尽可能多的小孩**。

很多录友都是用小饼干优先先喂饱小胃口的。

后来我想一想，虽然结果是一样的，但是大家的这个思考方式更好一些。

**因为用小饼干优先喂饱小胃口的 这样可以尽量保证最后省下来的是大饼干（虽然题目没有这个要求）！**

所以还是小饼干优先先喂饱小胃口更好一些，也比较直观。

一些录友不清楚[贪心算法：分发饼干 **(opens new window)**](https://programmercarl.com/0455.%E5%88%86%E5%8F%91%E9%A5%BC%E5%B9%B2.html)中时间复杂度是怎么来的？

就是快排O(nlog n)，遍历O(n)，加一起就是还是O(nlogn)。

## 周三

接下来就要上一点难度了，要不然大家会误以为贪心算法就是常识判断一下就行了。

在[贪心算法：摆动序列 **(opens new window)**](https://programmercarl.com/0376.%E6%91%86%E5%8A%A8%E5%BA%8F%E5%88%97.html)中，需要计算最长摇摆序列。

其实就是让序列有尽可能多的局部峰值。

局部最优：删除单调坡度上的节点（不包括单调坡度两端的节点），那么这个坡度就可以有两个局部峰值。

整体最优：整个序列有最多的局部峰值，从而达到最长摆动序列。

在计算峰值的时候，还是有一些代码技巧的，例如序列两端的峰值如何处理。

这些技巧，其实还是要多看多用才会掌握。

## 周四

在[贪心算法：最大子序和 **(opens new window)**](https://programmercarl.com/0053.%E6%9C%80%E5%A4%A7%E5%AD%90%E5%BA%8F%E5%92%8C.html)中，详细讲解了用贪心的方式来求最大子序列和，其实这道题目是一道动态规划的题目。

**贪心的思路为局部最优：当前“连续和”为负数的时候立刻放弃，从下一个元素重新计算“连续和”，因为负数加上下一个元素 “连续和”只会越来越小。从而推出全局最优：选取最大“连续和”**

代码很简单，但是思路却比较难。还需要反复琢磨。

针对[贪心算法：最大子序和 **(opens new window)**](https://programmercarl.com/0053.%E6%9C%80%E5%A4%A7%E5%AD%90%E5%BA%8F%E5%92%8C.html)文章中给出的贪心代码如下；

```cpp
class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int result = INT32_MIN;
        int count = 0;
        for (int i = 0; i < nums.size(); i++) {
            count += nums[i];
            if (count > result) { // 取区间累计的最大值（相当于不断确定最大子序终止位置）
                result = count;
            }
            if (count <= 0) count = 0; // 相当于重置最大子序起始位置，因为遇到负数一定是拉低总和
        }
        return result;
    }
};
```

不少同学都来问，如果数组全是负数这个代码就有问题了，如果数组里有int最小值这个代码就有问题了。

大家不要脑洞模拟哈，可以亲自构造一些测试数据试一试，就发现其实没有问题。

数组都为负数，result记录的就是最大的负数，如果数组里有int最小值，那么最终result就是int最小值。

## 总结

本周我们讲解了[贪心算法的理论基础 **(opens new window)**](https://programmercarl.com/%E8%B4%AA%E5%BF%83%E7%AE%97%E6%B3%95%E7%90%86%E8%AE%BA%E5%9F%BA%E7%A1%80.html)，了解了贪心本质：局部最优推出全局最优。

然后讲解了第一道题目[分发饼干 **(opens new window)**](https://programmercarl.com/0455.%E5%88%86%E5%8F%91%E9%A5%BC%E5%B9%B2.html)，还是比较基础的，可能会给大家一种贪心算法比较简单的错觉，因为贪心有时候接近于常识。

其实我还准备一些简单的贪心题目，甚至网上很多都质疑这些题目是不是贪心算法。这些题目我没有立刻发出来，因为真的会让大家感觉贪心过于简单，而忽略了贪心的本质：局部最优和全局最优两个关键点。

**所以我在贪心系列难度会有所交替，难的题目在于拓展思路，简单的题目在于分析清楚其贪心的本质，后续我还会发一些简单的题目来做贪心的分析。**

在[摆动序列 **(opens new window)**](https://programmercarl.com/0376.%E6%91%86%E5%8A%A8%E5%BA%8F%E5%88%97.html)中大家就初步感受到贪心没那么简单了。

本周最后是[最大子序和 **(opens new window)**](https://programmercarl.com/0053.%E6%9C%80%E5%A4%A7%E5%AD%90%E5%BA%8F%E5%92%8C.html)，这道题目要用贪心的方式做出来，就比较有难度，都知道负数加上正数之后会变小，但是这道题目依然会让很多人搞混淆，其关键在于：**不能让“连续和”为负数的时候加上下一个元素，而不是 不让“连续和”加上一个负数**。这块真的需要仔细体会！


# 六、122.买卖股票的最佳时机 II

[力扣题目链接(opens new window)](https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-ii/)

给定一个数组，它的第  i 个元素是一支给定股票第 i 天的价格。

设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。

注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

示例 1:

* 输入: [7,1,5,3,6,4]
* 输出: 7
* 解释: 在第 2 天（股票价格 = 1）的时候买入，在第 3 天（股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4。随后，在第 4 天（股票价格 = 3）的时候买入，在第 5 天（股票价格 = 6）的时候卖出, 这笔交易所能获得利润 = 6-3 = 3 。

示例 2:

* 输入: [1,2,3,4,5]
* 输出: 4
* 解释: 在第 1 天（股票价格 = 1）的时候买入，在第 5 天 （股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。注意你不能在第 1 天和第 2 天接连购买股票，之后再将它们卖出。因为这样属于同时参与了多笔交易，你必须在再次购买前出售掉之前的股票。

示例  3:

* 输入: [7,6,4,3,1]
* 输出: 0
* 解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。

提示：

* 1 <= prices.length <= 3 \* 10 ^ 4
* 0 <= prices[i] <= 10 ^ 4

## 算法公开课

**[《代码随想录》算法视频公开课 **(opens new window)**](https://programmercarl.com/other/gongkaike.html)：[贪心算法也能解决股票问题！LeetCode：122.买卖股票最佳时机 II **(opens new window)**](https://www.bilibili.com/video/BV1ev4y1C7na)，相信结合视频在看本篇题解，更有助于大家对本题的理解**。

## 思路

本题首先要清楚两点：

* 只有一只股票！
* 当前只有买股票或者卖股票的操作

想获得利润至少要两天为一个交易单元。

### 贪心算法

这道题目可能我们只会想，选一个低的买入，再选个高的卖，再选一个低的买入.....循环反复。

**如果想到其实最终利润是可以分解的，那么本题就很容易了！**

如何分解呢？

假如第 0 天买入，第 3 天卖出，那么利润为：prices[3] - prices[0]。

相当于(prices[3] - prices[2]) + (prices[2] - prices[1]) + (prices[1] - prices[0])。

**此时就是把利润分解为每天为单位的维度，而不是从 0 天到第 3 天整体去考虑！**

那么根据 prices 可以得到每天的利润序列：(prices[i] - prices[i - 1]).....(prices[1] - prices[0])。

如图：

https://code-thinking-1253855093.file.myqcloud.com/pics/2020112917480858-20230310134659477.png（图像链接）

一些同学陷入：第一天怎么就没有利润呢，第一天到底算不算的困惑中。

第一天当然没有利润，至少要第二天才会有利润，所以利润的序列比股票序列少一天！

从图中可以发现，其实我们需要收集每天的正利润就可以，**收集正利润的区间，就是股票买卖的区间，而我们只需要关注最终利润，不需要记录区间**。

那么只收集正利润就是贪心所贪的地方！

**局部最优：收集每天的正利润，全局最优：求得最大利润**。

局部最优可以推出全局最优，找不出反例，试一试贪心！

对应 C++代码如下：

```cpp
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int result = 0;
        for (int i = 1; i < prices.size(); i++) {
            result += max(prices[i] - prices[i - 1], 0);
        }
        return result;
    }
};
```

* 时间复杂度：O(n)
* 空间复杂度：O(1)

### 动态规划

动态规划将在下一个系列详细讲解，本题解先给出我的 C++代码（带详细注释），想先学习的话，可以看本篇：[122.买卖股票的最佳时机II（动态规划）(opens new window)](https://programmercarl.com/0122.%E4%B9%B0%E5%8D%96%E8%82%A1%E7%A5%A8%E7%9A%84%E6%9C%80%E4%BD%B3%E6%97%B6%E6%9C%BAII%EF%BC%88%E5%8A%A8%E6%80%81%E8%A7%84%E5%88%92%EF%BC%89.html#%E6%80%9D%E8%B7%AF)

```cpp
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        // dp[i][1]第i天持有的最多现金
        // dp[i][0]第i天持有股票后的最多现金
        int n = prices.size();
        vector<vector<int>> dp(n, vector<int>(2, 0));
        dp[0][0] -= prices[0]; // 持股票
        for (int i = 1; i < n; i++) {
            // 第i天持股票所剩最多现金 = max(第i-1天持股票所剩现金, 第i-1天持现金-买第i天的股票)
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] - prices[i]);
            // 第i天持有最多现金 = max(第i-1天持有的最多现金，第i-1天持有股票的最多现金+第i天卖出股票)
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] + prices[i]);
        }
        return max(dp[n - 1][0], dp[n - 1][1]);
    }
};
```

* 时间复杂度：\$O(n)\$
* 空间复杂度：\$O(n)\$

## 总结

股票问题其实是一个系列的，属于动态规划的范畴，因为目前在讲解贪心系列，所以股票问题会在之后的动态规划系列中详细讲解。

**可以看出有时候，贪心往往比动态规划更巧妙，更好用，所以别小看了贪心算法**。

**本题中理解利润拆分是关键点！** 不要整块的去看，而是把整体利润拆为每天的利润。

一旦想到这里了，很自然就会想到贪心了，即：只收集每天的正利润，最后稳稳的就是最大利润了。

## 其他语言版本

### Python:

贪心:

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        for i in range(1, len(prices)):
            result += max(prices[i] - prices[i - 1], 0)
        return result
```

动态规划:

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        length = len(prices)
        # dp[i][0]第i天持有股票后的最多现金
        # dp[i][1]第i天持有的最多现金
        dp = [[0] * 2 for _ in range(length)]
        dp[0][0] = -prices[0]
        dp[0][1] = 0
        for i in range(1, length):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] - prices[i]) #注意这里是和121. 买卖股票的最佳时机唯一不同的地方
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] + prices[i])
        return dp[-1][1]
```

