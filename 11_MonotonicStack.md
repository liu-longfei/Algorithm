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

