# 七、55. 跳跃游戏

[力扣题目链接(opens new window)](https://leetcode.cn/problems/jump-game/)

给定一个非负整数数组，你最初位于数组的第一个位置。

数组中的每个元素代表你在该位置可以跳跃的最大长度。

判断你是否能够到达最后一个位置。

示例  1:

* 输入: [2,3,1,1,4]
* 输出: true
* 解释: 我们可以先跳 1 步，从位置 0 到达 位置 1, 然后再从位置 1 跳 3 步到达最后一个位置。

示例  2:

* 输入: [3,2,1,0,4]
* 输出: false
* 解释: 无论怎样，你总会到达索引为 3 的位置。但该位置的最大跳跃长度是 0 ， 所以你永远不可能到达最后一个位置。

## 算法公开课

**[《代码随想录》算法视频公开课 **(opens new window)**](https://programmercarl.com/other/gongkaike.html)：[贪心算法，怎么跳跃不重要，关键在覆盖范围 | LeetCode：55.跳跃游戏 **(opens new window)**](https://www.bilibili.com/video/BV1VG4y1X7kB)，相信结合视频在看本篇题解，更有助于大家对本题的理解**。

## 思路

刚看到本题一开始可能想：当前位置元素如果是 3，我究竟是跳一步呢，还是两步呢，还是三步呢，究竟跳几步才是最优呢？

其实跳几步无所谓，关键在于可跳的覆盖范围！

不一定非要明确一次究竟跳几步，每次取最大的跳跃步数，这个就是可以跳跃的覆盖范围。

这个范围内，别管是怎么跳的，反正一定可以跳过来。

**那么这个问题就转化为跳跃覆盖范围究竟可不可以覆盖到终点！**

每次移动取最大跳跃步数（得到最大的覆盖范围），每移动一个单位，就更新最大覆盖范围。

**贪心算法局部最优解：每次取最大跳跃步数（取最大覆盖范围），整体最优解：最后得到整体最大覆盖范围，看是否能到终点**。

局部最优推出全局最优，找不出反例，试试贪心！

如图：

https://code-thinking-1253855093.file.myqcloud.com/pics/20230203105634.png（图像链接）

i 每次移动只能在 cover 的范围内移动，每移动一个元素，cover 得到该元素数值（新的覆盖范围）的补充，让 i 继续移动下去。

而 cover 每次只取 max(该元素数值补充后的范围, cover 本身范围)。

如果 cover 大于等于了终点下标，直接 return true 就可以了。

C++代码如下：

```cpp
class Solution {
public:
    bool canJump(vector<int>& nums) {
        int cover = 0;
        if (nums.size() == 1) return true; // 只有一个元素，就是能达到
        for (int i = 0; i <= cover; i++) { // 注意这里是小于等于cover
            cover = max(i + nums[i], cover);
            if (cover >= nums.size() - 1) return true; // 说明可以覆盖到终点了
        }
        return false;
    }
};
```

* 时间复杂度: O(n)
* 空间复杂度: O(1)

## 总结

这道题目关键点在于：不用拘泥于每次究竟跳几步，而是看覆盖范围，覆盖范围内一定是可以跳过来的，不用管是怎么跳的。

大家可以看出思路想出来了，代码还是非常简单的。

一些同学可能感觉，我在讲贪心系列的时候，题目和题目之间貌似没有什么联系？

**是真的就是没什么联系，因为贪心无套路**！没有个整体的贪心框架解决一系列问题，只能是接触各种类型的题目锻炼自己的贪心思维！

## 其他语言版本

### Python

```python
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        cover = 0
        if len(nums) == 1: return True
        i = 0
        # python不支持动态修改for循环中变量,使用while循环代替
        while i <= cover:
            cover = max(i + nums[i], cover)
            if cover >= len(nums) - 1: return True
            i += 1
        return False
```

```python
## for循环
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        cover = 0
        if len(nums) == 1: return True
        for i in range(len(nums)):
            if i <= cover:
                cover = max(i + nums[i], cover)
                if cover >= len(nums) - 1: return True
        return False
```
# 八、45.跳跃游戏 II

[力扣题目链接(opens new window)](https://leetcode.cn/problems/jump-game-ii/)

给定一个非负整数数组，你最初位于数组的第一个位置。

数组中的每个元素代表你在该位置可以跳跃的最大长度。

你的目标是使用最少的跳跃次数到达数组的最后一个位置。

示例:

* 输入: [2,3,1,1,4]
* 输出: 2
* 解释: 跳到最后一个位置的最小跳跃数是 2。从下标为 0 跳到下标为 1 的位置，跳  1  步，然后跳  3  步到达数组的最后一个位置。

说明: 假设你总是可以到达数组的最后一个位置。

## 算法公开课

**[《代码随想录》算法视频公开课 **(opens new window)**](https://programmercarl.com/other/gongkaike.html)：[贪心算法，最少跳几步还得看覆盖范围 | LeetCode： 45.跳跃游戏 II **(opens new window)**](https://www.bilibili.com/video/BV1Y24y1r7XZ)，相信结合视频在看本篇题解，更有助于大家对本题的理解**。

## 思路

本题相对于[55.跳跃游戏 **(opens new window)**](https://programmercarl.com/0055.%E8%B7%B3%E8%B7%83%E6%B8%B8%E6%88%8F.html)还是难了不少。

但思路是相似的，还是要看最大覆盖范围。

本题要计算最少步数，那么就要想清楚什么时候步数才一定要加一呢？

贪心的思路，局部最优：当前可移动距离尽可能多走，如果还没到终点，步数再加一。整体最优：一步尽可能多走，从而达到最少步数。

思路虽然是这样，但在写代码的时候还不能真的能跳多远就跳多远，那样就不知道下一步最远能跳到哪里了。

**所以真正解题的时候，要从覆盖范围出发，不管怎么跳，覆盖范围内一定是可以跳到的，以最小的步数增加覆盖范围，覆盖范围一旦覆盖了终点，得到的就是最少步数！**

**这里需要统计两个覆盖范围，当前这一步的最大覆盖和下一步最大覆盖**。

如果移动下标达到了当前这一步的最大覆盖最远距离了，还没有到终点的话，那么就必须再走一步来增加覆盖范围，直到覆盖范围覆盖了终点。

如图：

https://code-thinking-1253855093.file.myqcloud.com/pics/20201201232309103.png（图像链接）

**图中覆盖范围的意义在于，只要红色的区域，最多两步一定可以到！（不用管具体怎么跳，反正一定可以跳到）**

### 方法一

从图中可以看出来，就是移动下标达到了当前覆盖的最远距离下标时，步数就要加一，来增加覆盖距离。最后的步数就是最少步数。

这里还是有个特殊情况需要考虑，当移动下标达到了当前覆盖的最远距离下标时

* 如果当前覆盖最远距离下标不是是集合终点，步数就加一，还需要继续走。
* 如果当前覆盖最远距离下标就是是集合终点，步数不用加一，因为不能再往后走了。

C++代码如下：（详细注释）

```cpp
// 版本一
class Solution {
public:
    int jump(vector<int>& nums) {
        if (nums.size() == 1) return 0;
        int curDistance = 0;    // 当前覆盖最远距离下标
        int ans = 0;            // 记录走的最大步数
        int nextDistance = 0;   // 下一步覆盖最远距离下标
        for (int i = 0; i < nums.size(); i++) {
            nextDistance = max(nums[i] + i, nextDistance);  // 更新下一步覆盖最远距离下标
            if (i == curDistance) {                         // 遇到当前覆盖最远距离下标
                ans++;                                  // 需要走下一步
                curDistance = nextDistance;             // 更新当前覆盖最远距离下标（相当于加油了）
                if (nextDistance >= nums.size() - 1) break;  // 当前覆盖最远距到达集合终点，不用做ans++操作了，直接结束
            }
        }
        return ans;
    }
};
```

* 时间复杂度: O(n)
* 空间复杂度: O(1)

### 方法二

依然是贪心，思路和方法一差不多，代码可以简洁一些。

**针对于方法一的特殊情况，可以统一处理**，即：移动下标只要遇到当前覆盖最远距离的下标，直接步数加一，不考虑是不是终点的情况。

想要达到这样的效果，只要让移动下标，最大只能移动到 nums.size - 2 的地方就可以了。

因为当移动下标指向 nums.size - 2 时：

* 如果移动下标等于当前覆盖最大距离下标， 需要再走一步（即 ans++），因为最后一步一定是可以到的终点。（题目假设总是可以到达数组的最后一个位置），如图：

https://code-thinking-1253855093.file.myqcloud.com/pics/20201201232445286.png

* 如果移动下标不等于当前覆盖最大距离下标，说明当前覆盖最远距离就可以直接达到终点了，不需要再走一步。如图：

https://code-thinking-1253855093.file.myqcloud.com/pics/20201201232338693.png

代码如下：

```cpp
// 版本二
class Solution {
public:
    int jump(vector<int>& nums) {
        int curDistance = 0;    // 当前覆盖的最远距离下标
        int ans = 0;            // 记录走的最大步数
        int nextDistance = 0;   // 下一步覆盖的最远距离下标
        for (int i = 0; i < nums.size() - 1; i++) { // 注意这里是小于nums.size() - 1，这是关键所在
            nextDistance = max(nums[i] + i, nextDistance); // 更新下一步覆盖的最远距离下标
            if (i == curDistance) {                 // 遇到当前覆盖的最远距离下标
                curDistance = nextDistance;         // 更新当前覆盖的最远距离下标
                ans++;
            }
        }
        return ans;
    }
};
```

* 时间复杂度: O(n)
* 空间复杂度: O(1)

可以看出版本二的代码相对于版本一简化了不少！

**其精髓在于控制移动下标 i 只移动到 nums.size() - 2 的位置**，所以移动下标只要遇到当前覆盖最远距离的下标，直接步数加一，不用考虑别的了。

## 总结

相信大家可以发现，这道题目相当于[55.跳跃游戏 **(opens new window)**](https://programmercarl.com/0055.%E8%B7%B3%E8%B7%83%E6%B8%B8%E6%88%8F.html)难了不止一点。

但代码又十分简单，贪心就是这么巧妙。

理解本题的关键在于：**以最小的步数增加最大的覆盖范围，直到覆盖范围覆盖了终点**，这个范围内最少步数一定可以跳到，不用管具体是怎么跳的，不纠结于一步究竟跳一个单位还是两个单位。

## 其他语言版本

### Python

贪心（版本一）

```python
class Solution:
    def jump(self, nums):
        if len(nums) == 1:
            return 0
      
        cur_distance = 0  # 当前覆盖最远距离下标
        ans = 0  # 记录走的最大步数
        next_distance = 0  # 下一步覆盖最远距离下标
      
        for i in range(len(nums)):
            next_distance = max(nums[i] + i, next_distance)  # 更新下一步覆盖最远距离下标
            if i == cur_distance:  # 遇到当前覆盖最远距离下标
                ans += 1  # 需要走下一步
                cur_distance = next_distance  # 更新当前覆盖最远距离下标（相当于加油了）
                if next_distance >= len(nums) - 1:  # 当前覆盖最远距离达到数组末尾，不用再做ans++操作，直接结束
                    break
      
        return ans

```

贪心（版本二）

```python
class Solution:
    def jump(self, nums):
        cur_distance = 0  # 当前覆盖的最远距离下标
        ans = 0  # 记录走的最大步数
        next_distance = 0  # 下一步覆盖的最远距离下标
      
        for i in range(len(nums) - 1):  # 注意这里是小于len(nums) - 1，这是关键所在
            next_distance = max(nums[i] + i, next_distance)  # 更新下一步覆盖的最远距离下标
            if i == cur_distance:  # 遇到当前覆盖的最远距离下标
                cur_distance = next_distance  # 更新当前覆盖的最远距离下标
                ans += 1
      
        return ans

```

贪心（版本三） 类似‘55-跳跃游戏’写法

```python
class Solution:
    def jump(self, nums) -> int:
        if len(nums)==1:  # 如果数组只有一个元素，不需要跳跃，步数为0
            return 0
      
        i = 0  # 当前位置
        count = 0  # 步数计数器
        cover = 0  # 当前能够覆盖的最远距离
      
        while i <= cover:  # 当前位置小于等于当前能够覆盖的最远距离时循环
            for i in range(i, cover+1):  # 遍历从当前位置到当前能够覆盖的最远距离之间的所有位置
                cover = max(nums[i]+i, cover)  # 更新当前能够覆盖的最远距离
                if cover >= len(nums)-1:  # 如果当前能够覆盖的最远距离达到或超过数组的最后一个位置，直接返回步数+1
                    return count+1
            count += 1  # 每一轮遍历结束后，步数+1

      
```

动态规划

```python
class Solution:
    def jump(self, nums: List[int]) -> int:
        result = [10**4+1] * len(nums)  # 初始化结果数组，初始值为一个较大的数
        result[0] = 0  # 起始位置的步数为0

        for i in range(len(nums)):  # 遍历数组
            for j in range(nums[i] + 1):  # 在当前位置能够跳跃的范围内遍历
                if i + j < len(nums):  # 确保下一跳的位置不超过数组范围
                    result[i + j] = min(result[i + j], result[i] + 1)  # 更新到达下一跳位置的最少步数

        return result[-1]  # 返回到达最后一个位置的最少步数
```
# 九、1005.K次取反后最大化的数组和

[力扣题目链接(opens new window)](https://leetcode.cn/problems/maximize-sum-of-array-after-k-negations/)

给定一个整数数组 A，我们只能用以下方法修改该数组：我们选择某个索引 i 并将 A[i] 替换为 -A[i]，然后总共重复这个过程 K 次。（我们可以多次选择同一个索引 i。）

以这种方式修改数组后，返回数组可能的最大和。

示例 1：

* 输入：A = [4,2,3], K = 1
* 输出：5
* 解释：选择索引 (1) ，然后 A 变为 [4,-2,3]。

示例 2：

* 输入：A = [3,-1,0,2], K = 3
* 输出：6
* 解释：选择索引 (1, 2, 2) ，然后 A 变为 [3,1,0,2]。

示例 3：

* 输入：A = [2,-3,-1,5,-4], K = 2
* 输出：13
* 解释：选择索引 (1, 4) ，然后 A 变为 [2,3,-1,5,4]。

提示：

* 1 <= A.length <= 10000
* 1 <= K <= 10000
* -100 <= A[i] <= 100

## 算法公开课

**[《代码随想录》算法视频公开课 **(opens new window)**](https://programmercarl.com/other/gongkaike.html)：[贪心算法，这不就是常识？还能叫贪心？LeetCode：1005.K次取反后最大化的数组和 **(opens new window)**](https://www.bilibili.com/video/BV138411G7LY)，相信结合视频在看本篇题解，更有助于大家对本题的理解**。

## 思路

本题思路其实比较好想了，如何可以让数组和最大呢？

贪心的思路，局部最优：让绝对值大的负数变为正数，当前数值达到最大，整体最优：整个数组和达到最大。

局部最优可以推出全局最优。

那么如果将负数都转变为正数了，K依然大于0，此时的问题是一个有序正整数序列，如何转变K次正负，让 数组和 达到最大。

那么又是一个贪心：局部最优：只找数值最小的正整数进行反转，当前数值和可以达到最大（例如正整数数组{5, 3, 1}，反转1 得到-1 比 反转5得到的-5 大多了），全局最优：整个 数组和 达到最大。

虽然这道题目大家做的时候，可能都不会去想什么贪心算法，一鼓作气，就AC了。

**我这里其实是为了给大家展现出来 经常被大家忽略的贪心思路，这么一道简单题，就用了两次贪心！**

那么本题的解题步骤为：

* 第一步：将数组按照绝对值大小从大到小排序，**注意要按照绝对值的大小**
* 第二步：从前向后遍历，遇到负数将其变为正数，同时K--
* 第三步：如果K还大于0，那么反复转变数值最小的元素，将K用完
* 第四步：求和

对应C++代码如下：

```cpp
class Solution {
static bool cmp(int a, int b) {
    return abs(a) > abs(b);
}
public:
    int largestSumAfterKNegations(vector<int>& A, int K) {
        sort(A.begin(), A.end(), cmp);       // 第一步
        for (int i = 0; i < A.size(); i++) { // 第二步
            if (A[i] < 0 && K > 0) {
                A[i] *= -1;
                K--;
            }
        }
        if (K % 2 == 1) A[A.size() - 1] *= -1; // 第三步
        int result = 0;
        for (int a : A) result += a;        // 第四步
        return result;
    }
};
```

* 时间复杂度: O(nlogn)
* 空间复杂度: O(1)

## 总结

贪心的题目如果简单起来，会让人简单到开始怀疑：本来不就应该这么做么？这也算是算法？我认为这不是贪心？

本题其实很简单，不会贪心算法的同学都可以做出来，但是我还是全程用贪心的思路来讲解。

因为贪心的思考方式一定要有！

**如果没有贪心的思考方式（局部最优，全局最优），很容易陷入贪心简单题凭感觉做，贪心难题直接不会做，其实这样就锻炼不了贪心的思考方式了**。

所以明知道是贪心简单题，也要靠贪心的思考方式来解题，这样对培养解题感觉很有帮助。

## 其他语言版本

### Python

贪心

```python
class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        A.sort(key=lambda x: abs(x), reverse=True)  # 第一步：按照绝对值降序排序数组A

        for i in range(len(A)):  # 第二步：执行K次取反操作
            if A[i] < 0 and K > 0:
                A[i] *= -1
                K -= 1

        if K % 2 == 1:  # 第三步：如果K还有剩余次数，将绝对值最小的元素取反
            A[-1] *= -1

        result = sum(A)  # 第四步：计算数组A的元素和
        return result
```
