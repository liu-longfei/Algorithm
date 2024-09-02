# Monotonic stack


# 一、739. 每日温度

[力扣题目链接(opens new window)](https://leetcode.cn/problems/daily-temperatures/)

请根据每日 气温 列表，重新生成一个列表。对应位置的输出为：要想观测到更高的气温，至少需要等待的天数。如果气温在这之后都不会升高，请在该位置用 0 来代替。

例如，给定一个列表 temperatures = [73, 74, 75, 71, 69, 72, 76, 73]，你的输出应该是 [1, 1, 4, 2, 1, 1, 0, 0]。

提示：气温 列表长度的范围是 [1, 30000]。每个气温的值的均为华氏度，都是在 [30, 100] 范围内的整数。

## 算法公开课

[《代码随想录》算法视频公开课 **(opens new window)**](https://programmercarl.com/other/gongkaike.html)：[单调栈，你该了解的，这里都讲了！LeetCode:739.每日温度 **(opens new window)**](https://www.bilibili.com/video/BV1my4y1Z7jj/)，**相信结合视频在看本篇题解，更有助于大家对本题的理解**。

## 思路

首先想到的当然是暴力解法，两层for循环，把至少需要等待的天数就搜出来了。时间复杂度是O(n^2)

那么接下来在来看看使用单调栈的解法。

那有同学就问了，我怎么能想到用单调栈呢？ 什么时候用单调栈呢？

**通常是一维数组，要寻找任一个元素的右边或者左边第一个比自己大或者小的元素的位置，此时我们就要想到可以用单调栈了**。时间复杂度为O(n)。

例如本题其实就是找找到一个元素右边第一个比自己大的元素，此时就应该想到用单调栈了。

那么单调栈的原理是什么呢？为什么时间复杂度是O(n)就可以找到每一个元素的右边第一个比它大的元素位置呢？

**单调栈的本质是空间换时间**，因为在遍历的过程中需要用一个栈来记录右边第一个比当前元素高的元素，优点是整个数组只需要遍历一次。

**更直白来说，就是用一个栈来记录我们遍历过的元素**，因为我们遍历数组的时候，我们不知道之前都遍历了哪些元素，以至于遍历一个元素找不到是不是之前遍历过一个更小的，所以我们需要用一个容器（这里用单调栈）来记录我们遍历过的元素。

在使用单调栈的时候首先要明确如下几点：

1. 单调栈里存放的元素是什么？

单调栈里只需要存放元素的下标i就可以了，如果需要使用对应的元素，直接T[i]就可以获取。

2. 单调栈里元素是递增呢？ 还是递减呢？

**注意以下讲解中，顺序的描述为 从栈头到栈底的顺序**，因为单纯的说从左到右或者从前到后，不说栈头朝哪个方向的话，大家一定比较懵。

这里我们要使用递增循序（再强调一下是指从栈头到栈底的顺序），因为只有递增的时候，栈里要加入一个元素i的时候，才知道栈顶元素在数组中右面第一个比栈顶元素大的元素是i。

即：如果求一个元素右边第一个更大元素，单调栈就是递增的，如果求一个元素右边第一个更小元素，单调栈就是递减的。

文字描述理解起来有点费劲，接下来我画了一系列的图，来讲解单调栈的工作过程，大家再去思考，本题为什么是递增栈。

使用单调栈主要有三个判断条件。

* 当前遍历的元素T[i]小于栈顶元素T[st.top()]的情况
* 当前遍历的元素T[i]等于栈顶元素T[st.top()]的情况
* 当前遍历的元素T[i]大于栈顶元素T[st.top()]的情况

**把这三种情况分析清楚了，也就理解透彻了**。

接下来我们用temperatures = [73, 74, 75, 71, 71, 72, 76, 73]为例来逐步分析，输出应该是 [1, 1, 4, 2, 1, 1, 0, 0]。

---

首先先将第一个遍历元素加入单调栈

https://code-thinking-1253855093.file.myqcloud.com/pics/20210219124434172.jpg（图像链接）

加入T[1] = 74，因为T[1] > T[0]（当前遍历的元素T[i]大于栈顶元素T[st.top()]的情况）。

我们要保持一个递增单调栈（从栈头到栈底），所以将T[0]弹出，T[1]加入，此时result数组可以记录了，result[0] = 1，即T[0]右面第一个比T[0]大的元素是T[1]。

https://code-thinking-1253855093.file.myqcloud.com/pics/20210219124504299.jpg（图像链接）

加入T[2]，同理，T[1]弹出

https://code-thinking-1253855093.file.myqcloud.com/pics/20210219124527361.jpg（图像链接）

加入T[3]，T[3] < T[2] （当前遍历的元素T[i]小于栈顶元素T[st.top()]的情况），加T[3]加入单调栈。

https://code-thinking-1253855093.file.myqcloud.com/pics/20210219124610761.jpg（图像链接）

加入T[4]，T[4] == T[3] （当前遍历的元素T[i]等于栈顶元素T[st.top()]的情况），此时依然要加入栈，不用计算距离，因为我们要求的是右面第一个大于本元素的位置，而不是大于等于！

https://code-thinking-1253855093.file.myqcloud.com/pics/20210219124633444.jpg（图像链接）

加入T[5]，T[5] > T[4] （当前遍历的元素T[i]大于栈顶元素T[st.top()]的情况），将T[4]弹出，同时计算距离，更新result

https://code-thinking-1253855093.file.myqcloud.com/pics/20210219124700567.jpg（图像链接）

T[4]弹出之后， T[5] > T[3] （当前遍历的元素T[i]大于栈顶元素T[st.top()]的情况），将T[3]继续弹出，同时计算距离，更新result

https://code-thinking-1253855093.file.myqcloud.com/pics/20210219124726613.jpg（图像链接）

直到发现T[5]小于T[st.top()]，终止弹出，将T[5]加入单调栈

https://code-thinking-1253855093.file.myqcloud.com/pics/20210219124807715.jpg（图像链接）

加入T[6]，同理，需要将栈里的T[5]，T[2]弹出

https://code-thinking-1253855093.file.myqcloud.com/pics/2021021912483374.jpg（图像链接）

同理，继续弹出

https://code-thinking-1253855093.file.myqcloud.com/pics/2021021912490098.jpg（图像链接）

此时栈里只剩下了T[6]

https://code-thinking-1253855093.file.myqcloud.com/pics/20210219124930156.jpg（图像链接）

加入T[7]， T[7] < T[6] 直接入栈，这就是最后的情况，result数组也更新完了。

https://code-thinking-1253855093.file.myqcloud.com/pics/20210219124957216.jpg（图像链接）

此时有同学可能就疑惑了，那result[6] , result[7]怎么没更新啊，元素也一直在栈里。

其实定义result数组的时候，就应该直接初始化为0，如果result没有更新，说明这个元素右面没有更大的了，也就是为0。

以上在图解的时候，已经把，这三种情况都做了详细的分析。

* 情况一：当前遍历的元素T[i]小于栈顶元素T[st.top()]的情况
* 情况二：当前遍历的元素T[i]等于栈顶元素T[st.top()]的情况
* 情况三：当前遍历的元素T[i]大于栈顶元素T[st.top()]的情况

通过以上过程，大家可以自己再模拟一遍，就会发现：只有单调栈递增（从栈口到栈底顺序），就是求右边第一个比自己大的，单调栈递减的话，就是求右边第一个比自己小的。

C++代码如下：

```cpp
// 版本一
class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& T) {
        // 递增栈
        stack<int> st;
        vector<int> result(T.size(), 0);
        st.push(0);
        for (int i = 1; i < T.size(); i++) {
            if (T[i] < T[st.top()]) {                       // 情况一
                st.push(i);
            } else if (T[i] == T[st.top()]) {               // 情况二
                st.push(i);
            } else {
                while (!st.empty() && T[i] > T[st.top()]) { // 情况三
                    result[st.top()] = i - st.top();
                    st.pop();
                }
                st.push(i);
            }
        }
        return result;
    }
};
```

**建议一开始 都把每种情况分析好，不要上来看简短的代码，关键逻辑都被隐藏了**。

精简代码如下：

```cpp
// 版本二
class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& T) {
        stack<int> st; // 递增栈
        vector<int> result(T.size(), 0);
        for (int i = 0; i < T.size(); i++) {
            while (!st.empty() && T[i] > T[st.top()]) { // 注意栈不能为空
                result[st.top()] = i - st.top();
                st.pop();
            }
            st.push(i);

        }
        return result;
    }
};
```

* 时间复杂度：O(n)
* 空间复杂度：O(n)

精简的代码是直接把情况一二三都合并到了一起，其实这种代码精简是精简，但思路不是很清晰。

建议大家把情况一二三想清楚了，先写出版本一的代码，然后在其基础上在做精简！

## 其他语言版本

### Python：

> 未精简版本

```python
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0]*len(temperatures)
        stack = [0]
        for i in range(1,len(temperatures)):
            # 情况一和情况二
            if temperatures[i]<=temperatures[stack[-1]]:
                stack.append(i)
            # 情况三
            else:
                while len(stack) != 0 and temperatures[i]>temperatures[stack[-1]]:
                    answer[stack[-1]]=i-stack[-1]
                    stack.pop()
                stack.append(i)

        return answer
```

> 精简版本

```python
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0]*len(temperatures)
        stack = []
        for i in range(len(temperatures)):
            while len(stack)>0 and temperatures[i] > temperatures[stack[-1]]:
                answer[stack[-1]] = i - stack[-1]
                stack.pop()
            stack.append(i)
        return answer
```

# 二、496.下一个更大元素 I

[力扣题目链接(opens new window)](https://leetcode.cn/problems/next-greater-element-i/)

给你两个 没有重复元素 的数组 nums1 和 nums2 ，其中nums1 是 nums2 的子集。

请你找出 nums1 中每个元素在 nums2 中的下一个比其大的值。

nums1 中数字 x 的下一个更大元素是指 x 在 nums2 中对应位置的右边的第一个比 x 大的元素。如果不存在，对应位置输出 -1 。

示例 1:

输入: nums1 = [4,1,2], nums2 = [1,3,4,2].
输出: [-1,3,-1]
解释:
对于 num1 中的数字 4 ，你无法在第二个数组中找到下一个更大的数字，因此输出 -1 。
对于 num1 中的数字 1 ，第二个数组中数字1右边的下一个较大数字是 3 。
对于 num1 中的数字 2 ，第二个数组中没有下一个更大的数字，因此输出 -1 。

示例 2:
输入: nums1 = [2,4], nums2 = [1,2,3,4].
输出: [3,-1]
解释:
对于 num1 中的数字 2 ，第二个数组中的下一个较大数字是 3 。
对于 num1 中的数字 4 ，第二个数组中没有下一个更大的数字，因此输出-1 。

提示：

* 1 <= nums1.length <= nums2.length <= 1000
* 0 <= nums1[i], nums2[i] <= 10^4
* nums1和nums2中所有整数 互不相同
* nums1 中的所有整数同样出现在 nums2 中

## 算法公开课

**[《代码随想录》算法视频公开课 **(opens new window)**](https://programmercarl.com/other/gongkaike.html)：[单调栈，套上一个壳子就有点绕了| LeetCode:496.下一个更大元素 **(opens new window)**](https://www.bilibili.com/video/BV1jA411m7dX/)，相信结合视频再看本篇题解，更有助于大家对本题的理解**。

## 思路

做本题之前，建议先做一下[739. 每日温度(opens new window)](https://programmercarl.com/0739.%E6%AF%8F%E6%97%A5%E6%B8%A9%E5%BA%A6.html)

在[739. 每日温度 **(opens new window)**](https://programmercarl.com/0739.%E6%AF%8F%E6%97%A5%E6%B8%A9%E5%BA%A6.html)中是求每个元素下一个比当前元素大的元素的位置。

本题则是说nums1 是 nums2的子集，找nums1中的元素在nums2中下一个比当前元素大的元素。

看上去和[739. 每日温度 **(opens new window)**](https://programmercarl.com/0739.%E6%AF%8F%E6%97%A5%E6%B8%A9%E5%BA%A6.html)就如出一辙了。

几乎是一样的，但是这么绕了一下，其实还上升了一点难度。

需要对单调栈使用的更熟练一些，才能顺利的把本题写出来。

从题目示例中我们可以看出最后是要求nums1的每个元素在nums2中下一个比当前元素大的元素，那么就要定义一个和nums1一样大小的数组result来存放结果。

一些同学可能看到两个数组都已经懵了，不知道要定一个一个多大的result数组来存放结果了。

**这么定义这个result数组初始化应该为多少呢？**

题目说如果不存在对应位置就输出 -1 ，所以result数组如果某位置没有被赋值，那么就应该是是-1，所以就初始化为-1。

在遍历nums2的过程中，我们要判断nums2[i]是否在nums1中出现过，因为最后是要根据nums1元素的下标来更新result数组。

**注意题目中说是两个没有重复元素 的数组 nums1 和 nums2**。

没有重复元素，我们就可以用map来做映射了。根据数值快速找到下标，还可以判断nums2[i]是否在nums1中出现过。

C++中，当我们要使用集合来解决哈希问题的时候，优先使用unordered\_set，因为它的查询和增删效率是最优的。我在[关于哈希表，你该了解这些！ **(opens new window)**](https://programmercarl.com/%E5%93%88%E5%B8%8C%E8%A1%A8%E7%90%86%E8%AE%BA%E5%9F%BA%E7%A1%80.html)中也做了详细的解释。

那么预处理代码如下:

```cpp
unordered_map<int, int> umap; // key:下标元素，value：下标
for (int i = 0; i < nums1.size(); i++) {
    umap[nums1[i]] = i;
}
```

使用单调栈，首先要想单调栈是从大到小还是从小到大。

本题和739. 每日温度是一样的。

栈头到栈底的顺序，要从小到大，也就是保持栈里的元素为递增顺序。只要保持递增，才能找到右边第一个比自己大的元素。

可能这里有一些同学不理解，那么可以自己尝试一下用递减栈，能不能求出来。**其实递减栈就是求右边第一个比自己小的元素了**。

接下来就要分析如下三种情况，一定要分析清楚。

1. 情况一：当前遍历的元素T[i]小于栈顶元素T[st.top()]的情况

此时满足递增栈（栈头到栈底的顺序），所以直接入栈。

2. 情况二：当前遍历的元素T[i]等于栈顶元素T[st.top()]的情况

如果相等的话，依然直接入栈，因为我们要求的是右边第一个比自己大的元素，而不是大于等于！

3. 情况三：当前遍历的元素T[i]大于栈顶元素T[st.top()]的情况

此时如果入栈就不满足递增栈了，这也是找到右边第一个比自己大的元素的时候。

判断栈顶元素是否在nums1里出现过，（注意栈里的元素是nums2的元素），如果出现过，开始记录结果。

记录结果这块逻辑有一点小绕，要清楚，此时栈顶元素在nums2数组中右面第一个大的元素是nums2[i]（即当前遍历元素）。

代码如下：

```cpp
while (!st.empty() && nums2[i] > nums2[st.top()]) {
    if (umap.count(nums2[st.top()]) > 0) { // 看map里是否存在这个元素
        int index = umap[nums2[st.top()]]; // 根据map找到nums2[st.top()] 在 nums1中的下标
        result[index] = nums2[i];
    }
    st.pop();
}
st.push(i);
```

以上分析完毕，C++代码如下：（其实本题代码和 [739. 每日温度 **(opens new window)**](https://programmercarl.com/0739.%E6%AF%8F%E6%97%A5%E6%B8%A9%E5%BA%A6.html)是基本差不多的）

```cpp
// 版本一
class Solution {
public:
    vector<int> nextGreaterElement(vector<int>& nums1, vector<int>& nums2) {
        stack<int> st;
        vector<int> result(nums1.size(), -1);
        if (nums1.size() == 0) return result;

        unordered_map<int, int> umap; // key:下标元素，value：下标
        for (int i = 0; i < nums1.size(); i++) {
            umap[nums1[i]] = i;
        }
        st.push(0);
        for (int i = 1; i < nums2.size(); i++) {
            if (nums2[i] < nums2[st.top()]) {           // 情况一
                st.push(i);
            } else if (nums2[i] == nums2[st.top()]) {   // 情况二
                st.push(i);
            } else {                                    // 情况三
                while (!st.empty() && nums2[i] > nums2[st.top()]) {
                    if (umap.count(nums2[st.top()]) > 0) { // 看map里是否存在这个元素
                        int index = umap[nums2[st.top()]]; // 根据map找到nums2[st.top()] 在 nums1中的下标
                        result[index] = nums2[i];
                    }
                    st.pop();
                }
                st.push(i);
            }
        }
        return result;
    }
};
```

针对版本一，进行代码精简后，代码如下：

```cpp
// 版本二
class Solution {
public:
    vector<int> nextGreaterElement(vector<int>& nums1, vector<int>& nums2) {
        stack<int> st;
        vector<int> result(nums1.size(), -1);
        if (nums1.size() == 0) return result;

        unordered_map<int, int> umap; // key:下标元素，value：下标
        for (int i = 0; i < nums1.size(); i++) {
            umap[nums1[i]] = i;
        }
        st.push(0);
        for (int i = 1; i < nums2.size(); i++) {
            while (!st.empty() && nums2[i] > nums2[st.top()]) {
                if (umap.count(nums2[st.top()]) > 0) { // 看map里是否存在这个元素
                    int index = umap[nums2[st.top()]]; // 根据map找到nums2[st.top()] 在 nums1中的下标
                    result[index] = nums2[i];
                }
                st.pop();
            }
            st.push(i);
        }
        return result;
    }
};
```

精简的代码是直接把情况一二三都合并到了一起，其实这种代码精简是精简，但思路不是很清晰。

建议大家把情况一二三想清楚了，先写出版本一的代码，然后在其基础上在做精简！ 

## 其他语言版本

### Python3

```python
# 版本一
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = [-1]*len(nums1)
        stack = [0]
        for i in range(1,len(nums2)):
            # 情况一情况二
            if nums2[i]<=nums2[stack[-1]]:
                stack.append(i)
            # 情况三
            else:
                while len(stack)!=0 and nums2[i]>nums2[stack[-1]]:
                    if nums2[stack[-1]] in nums1:
                        index = nums1.index(nums2[stack[-1]])
                        result[index]=nums2[i]
                    stack.pop()               
                stack.append(i)
        return result

# 版本二
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        # 创建答案数组
        ans = [-1] * len(nums1)
        for i in range(len(nums2)):
            while len(stack) > 0 and nums2[i] > nums2[stack[-1]]:
                # 判断 num1 是否有 nums2[stack[-1]]。如果没有这个判断会出现指针异常
                if nums2[stack[-1]] in nums1:
                    # 锁定 num1 检索的 index
                    index = nums1.index(nums2[stack[-1]])
                    # 更新答案数组
                    ans[index] = nums2[i]
                # 弹出小元素
                # 这个代码一定要放在 if 外面。否则单调栈的逻辑就不成立了
                stack.pop()
            stack.append(i)
        return ans
```

# 三、503.下一个更大元素II

[力扣题目链接(opens new window)](https://leetcode.cn/problems/next-greater-element-ii/)

给定一个循环数组（最后一个元素的下一个元素是数组的第一个元素），输出每个元素的下一个更大元素。数字 x 的下一个更大的元素是按数组遍历顺序，这个数字之后的第一个比它更大的数，这意味着你应该循环地搜索它的下一个更大的数。如果不存在，则输出 -1。

示例 1:

* 输入: [1,2,1]
* 输出: [2,-1,2]
* 解释: 第一个 1 的下一个更大的数是 2；数字 2 找不到下一个更大的数；第二个 1 的下一个最大的数需要循环搜索，结果也是 2。

提示:

* 1 <= nums.length <= 10^4
* -10^9 <= nums[i] <= 10^9

## 算法公开课

**[《代码随想录》算法视频公开课 **(opens new window)**](https://programmercarl.com/other/gongkaike.html)：[单调栈，成环了可怎么办？LeetCode：503.下一个更大元素II **(opens new window)**](https://www.bilibili.com/video/BV15y4y1o7Dw/)，相信结合视频在看本篇题解，更有助于大家对本题的理解**。

## 思路

做本题之前建议先做[739. 每日温度 **(opens new window)**](https://programmercarl.com/0739.%E6%AF%8F%E6%97%A5%E6%B8%A9%E5%BA%A6.html)和 [496.下一个更大元素 I **(opens new window)**](https://programmercarl.com/0496.%E4%B8%8B%E4%B8%80%E4%B8%AA%E6%9B%B4%E5%A4%A7%E5%85%83%E7%B4%A0I.html)。

这道题和[739. 每日温度 **(opens new window)**](https://programmercarl.com/0739.%E6%AF%8F%E6%97%A5%E6%B8%A9%E5%BA%A6.html)也几乎如出一辙。

不过，本题要循环数组了。

关于单调栈的讲解我在题解[739. 每日温度 **(opens new window)**](https://programmercarl.com/0739.%E6%AF%8F%E6%97%A5%E6%B8%A9%E5%BA%A6.html)中已经详细讲解了。

本篇我侧重与说一说，如何处理循环数组。

相信不少同学看到这道题，就想那我直接把两个数组拼接在一起，然后使用单调栈求下一个最大值不就行了！

确实可以！

将两个nums数组拼接在一起，使用单调栈计算出每一个元素的下一个最大值，最后再把结果集即result数组resize到原数组大小就可以了。

代码如下：

```cpp
// 版本一
class Solution {
public:
    vector<int> nextGreaterElements(vector<int>& nums) {
        // 拼接一个新的nums
        vector<int> nums1(nums.begin(), nums.end());
        nums.insert(nums.end(), nums1.begin(), nums1.end());
        // 用新的nums大小来初始化result
        vector<int> result(nums.size(), -1);
        if (nums.size() == 0) return result;

        // 开始单调栈
        stack<int> st;
        st.push(0);
        for (int i = 1; i < nums.size(); i++) { 
            if (nums[i] < nums[st.top()]) st.push(i); 
            else if (nums[i] == nums[st.top()]) st.push(i);
            else { 
                while (!st.empty() && nums[i] > nums[st.top()]) {
                    result[st.top()] = nums[i];
                    st.pop();
                }
                st.push(i);
            }
        }
        // 最后再把结果集即result数组resize到原数组大小
        result.resize(nums.size() / 2);
        return result;
    }
};

```

这种写法确实比较直观，但做了很多无用操作，例如修改了nums数组，而且最后还要把result数组resize回去。

resize倒是不费时间，是O(1)的操作，但扩充nums数组相当于多了一个O(n)的操作。

其实也可以不扩充nums，而是在遍历的过程中模拟走了两边nums。

代码如下：

```cpp
// 版本二
class Solution {
public:
    vector<int> nextGreaterElements(vector<int>& nums) {
        vector<int> result(nums.size(), -1);
        if (nums.size() == 0) return result;
        stack<int> st;
        st.push(0);
        for (int i = 1; i < nums.size() * 2; i++) { 
            // 模拟遍历两边nums，注意一下都是用i % nums.size()来操作
            if (nums[i % nums.size()] < nums[st.top()]) st.push(i % nums.size());
            else if (nums[i % nums.size()] == nums[st.top()]) st.push(i % nums.size()); 
            else {
                while (!st.empty() && nums[i % nums.size()] > nums[st.top()]) {
                    result[st.top()] = nums[i % nums.size()];
                    st.pop();
                }
                st.push(i % nums.size());
            }
        }
        return result;
    }
};
```

可以版本二不仅代码精简了，也比版本一少做了无用功！

最后在给出 单调栈的精简版本，即三种情况都做了合并的操作。

```cpp
// 版本二
class Solution {
public:
    vector<int> nextGreaterElements(vector<int>& nums) {
        vector<int> result(nums.size(), -1);
        if (nums.size() == 0) return result;
        stack<int> st;
        for (int i = 0; i < nums.size() * 2; i++) {
            // 模拟遍历两边nums，注意一下都是用i % nums.size()来操作
            while (!st.empty() && nums[i % nums.size()] > nums[st.top()]) {
                result[st.top()] = nums[i % nums.size()];
                st.pop();
            }
            st.push(i % nums.size());
        }
        return result;
    }
};
```

## 其他语言版本

### Python:

```python
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        dp = [-1] * len(nums)
        stack = []
        for i in range(len(nums)*2):
            while(len(stack) != 0 and nums[i%len(nums)] > nums[stack[-1]]):
                    dp[stack[-1]] = nums[i%len(nums)]
                    stack.pop()
            stack.append(i%len(nums))
        return dp
```

