# 七、459.重复的子字符串

[力扣题目链接(opens new window)](https://leetcode.cn/problems/repeated-substring-pattern/)

给定一个非空的字符串，判断它是否可以由它的一个子串重复多次构成。给定的字符串只含有小写英文字母，并且长度不超过10000。

示例 1:

* 输入: "abab"
* 输出: True
* 解释: 可由子字符串 "ab" 重复两次构成。

示例 2:

* 输入: "aba"
* 输出: False

示例 3:

* 输入: "abcabcabcabc"
* 输出: True
* 解释: 可由子字符串 "abc" 重复四次构成。 (或者子字符串 "abcabc" 重复两次构成。)

## 算法公开课

[《代码随想录》算法视频公开课 **(opens new window)**](https://programmercarl.com/other/gongkaike.html)：[字符串这么玩，可有点难度！ | LeetCode：459.重复的子字符串 **(opens new window)**](https://www.bilibili.com/video/BV1cg41127fw)，**相信结合视频再看本篇题解，更有助于大家对本题的理解**。

## 思路

暴力的解法， 就是一个for循环获取 子串的终止位置， 然后判断子串是否能重复构成字符串，又嵌套一个for循环，所以是O(n^2)的时间复杂度。

有的同学可以想，怎么一个for循环就可以获取子串吗？ 至少得一个for获取子串起始位置，一个for获取子串结束位置吧。

其实我们只需要判断，以第一个字母为开始的子串就可以，所以一个for循环获取子串的终止位置就行了。 而且遍历的时候 都不用遍历结束，只需要遍历到中间位置，因为子串结束位置大于中间位置的话，一定不能重复组成字符串。

暴力的解法，这里就不详细讲解了。

主要讲一讲移动匹配 和 KMP两种方法。

### 移动匹配

当一个字符串s：abcabc，内部由重复的子串组成，那么这个字符串的结构一定是这样的：

https://code-thinking-1253855093.file.myqcloud.com/pics/20220728104518.png（图像链接）

也就是由前后相同的子串组成。

那么既然前面有相同的子串，后面有相同的子串，用 s + s，这样组成的字符串中，后面的子串做前串，前面的子串做后串，就一定还能组成一个s，如图：

https://code-thinking-1253855093.file.myqcloud.com/pics/20220728104931.png（图像链接）

所以判断字符串s是否由重复子串组成，只要两个s拼接在一起，里面还出现一个s的话，就说明是由重复子串组成。

当然，我们在判断 s + s 拼接的字符串里是否出现一个s的的时候，**要刨除 s + s 的首字符和尾字符**，这样避免在s+s中搜索出原来的s，我们要搜索的是中间拼接出来的s。

代码如下：

```cpp
class Solution {
public:
    bool repeatedSubstringPattern(string s) {
        string t = s + s;
        t.erase(t.begin()); t.erase(t.end() - 1); // 掐头去尾
        if (t.find(s) != std::string::npos) return true; // r
        return false;
    }
};
```

* 时间复杂度: O(n)
* 空间复杂度: O(1)

不过这种解法还有一个问题，就是 我们最终还是要判断 一个字符串（s + s）是否出现过 s 的过程，大家可能直接用contains，find 之类的库函数。 却忽略了实现这些函数的时间复杂度（暴力解法是m \* n，一般库函数实现为 O(m + n)）。

如果我们做过 [28.实现strStr **(opens new window)**](https://programmercarl.com/0028.%E5%AE%9E%E7%8E%B0strStr.html)题目的话，其实就知道，**实现一个 高效的算法来判断 一个字符串中是否出现另一个字符串是很复杂的**，这里就涉及到了KMP算法。

### KMP

#### 为什么会使用KMP

以下使用KMP方式讲解，强烈建议大家先把以下两个视频看了，理解KMP算法，再来看下面讲解，否则会很懵。

* [视频讲解版：帮你把KMP算法学个通透！（理论篇）(opens new window)](https://www.bilibili.com/video/BV1PD4y1o7nd/)
* [视频讲解版：帮你把KMP算法学个通透！（求next数组代码篇）(opens new window)](https://www.bilibili.com/video/BV1M5411j7Xx)
* [文字讲解版：KMP算法(opens new window)](https://programmercarl.com/0028.%E5%AE%9E%E7%8E%B0strStr.html)

在一个串中查找是否出现过另一个串，这是KMP的看家本领。那么寻找重复子串怎么也涉及到KMP算法了呢？

KMP算法中next数组为什么遇到字符不匹配的时候可以找到上一个匹配过的位置继续匹配，靠的是有计算好的前缀表。 前缀表里，统计了各个位置为终点字符串的最长相同前后缀的长度。

那么 最长相同前后缀和重复子串的关系又有什么关系呢。

可能很多录友又忘了 前缀和后缀的定义，再回顾一下：

* 前缀是指不包含最后一个字符的所有以第一个字符开头的连续子串；
* 后缀是指不包含第一个字符的所有以最后一个字符结尾的连续子串

在由重复子串组成的字符串中，最长相等前后缀不包含的子串就是最小重复子串，这里拿字符串s：abababab 来举例，ab就是最小重复单位，如图所示：

https://code-thinking-1253855093.file.myqcloud.com/pics/20220728205249.png（图像链接）

#### 如何找到最小重复子串

这里有同学就问了，为啥一定是开头的ab呢。 其实最关键还是要理解 最长相等前后缀，如图：

https://code-thinking-1253855093.file.myqcloud.com/pics/20220728212157.png（图像链接）

步骤一：因为 这是相等的前缀和后缀，t[0] 与 k[0]相同， t[1] 与 k[1]相同，所以 s[0] 一定和 s[2]相同，s[1] 一定和 s[3]相同，即：，s[0]s[1]与s[2]s[3]相同 。

步骤二： 因为在同一个字符串位置，所以 t[2] 与 k[0]相同，t[3] 与 k[1]相同。

步骤三： 因为 这是相等的前缀和后缀，t[2] 与 k[2]相同 ，t[3]与k[3] 相同，所以，s[2]一定和s[4]相同，s[3]一定和s[5]相同，即：s[2]s[3] 与 s[4]s[5]相同。

步骤四：循环往复。

所以字符串s，s[0]s[1]与s[2]s[3]相同， s[2]s[3] 与 s[4]s[5]相同，s[4]s[5] 与 s[6]s[7] 相同。

正是因为 最长相等前后缀的规则，当一个字符串由重复子串组成的，最长相等前后缀不包含的子串就是最小重复子串。

#### 简单推理

这里再给出一个数学推导，就容易理解很多。

假设字符串s使用多个重复子串构成（这个子串是最小重复单位），重复出现的子字符串长度是x，所以s是由n \* x组成。

因为字符串s的最长相同前后缀的长度一定是不包含s本身，所以 最长相同前后缀长度必然是m \* x，而且 n - m = 1，（这里如果不懂，看上面的推理）

所以如果 nx % (n - m)x = 0，就可以判定有重复出现的子字符串。

next 数组记录的就是最长相同前后缀 [字符串：KMP算法精讲 **(opens new window)**](https://programmercarl.com/0028.%E5%AE%9E%E7%8E%B0strStr.html)这里介绍了什么是前缀，什么是后缀，什么又是最长相同前后缀)， 如果 next[len - 1] != -1，则说明字符串有最长相同的前后缀（就是字符串里的前缀子串和后缀子串相同的最长长度）。

最长相等前后缀的长度为：next[len - 1] + 1。(这里的next数组是以统一减一的方式计算的，因此需要+1，两种计算next数组的具体区别看这里：[字符串：KMP算法精讲 **(opens new window)**](https://programmercarl.com/0028.%E5%AE%9E%E7%8E%B0strStr.html))

数组长度为：len。

如果len % (len - (next[len - 1] + 1)) == 0 ，则说明数组的长度正好可以被 (数组长度-最长相等前后缀的长度) 整除 ，说明该字符串有重复的子字符串。

**数组长度减去最长相同前后缀的长度相当于是第一个周期的长度，也就是一个周期的长度，如果这个周期可以被整除，就说明整个数组就是这个周期的循环。**

**强烈建议大家把next数组打印出来，看看next数组里的规律，有助于理解KMP算法**

如图：

https://code-thinking.cdn.bcebos.com/pics/459.%E9%87%8D%E5%A4%8D%E7%9A%84%E5%AD%90%E5%AD%97%E7%AC%A6%E4%B8%B2_1.png（图像链接）

next[len - 1] = 7，next[len - 1] + 1 = 8，8就是此时字符串asdfasdfasdf的最长相同前后缀的长度。

(len - (next[len - 1] + 1)) 也就是： 12(字符串的长度) - 8(最长公共前后缀的长度) = 4， 4正好可以被 12(字符串的长度) 整除，所以说明有重复的子字符串（asdf）。

C++代码如下：（这里使用了前缀表统一减一的实现方式）

```cpp
class Solution {
public:
    void getNext (int* next, const string& s){
        next[0] = -1;
        int j = -1;
        for(int i = 1;i < s.size(); i++){
            while(j >= 0 && s[i] != s[j + 1]) {
                j = next[j];
            }
            if(s[i] == s[j + 1]) {
                j++;
            }
            next[i] = j;
        }
    }
    bool repeatedSubstringPattern (string s) {
        if (s.size() == 0) {
            return false;
        }
        int next[s.size()];
        getNext(next, s);
        int len = s.size();
        if (next[len - 1] != -1 && len % (len - (next[len - 1] + 1)) == 0) {
            return true;
        }
        return false;
    }
};
```

* 时间复杂度: O(n)
* 空间复杂度: O(n)

前缀表（不减一）的C++代码实现：

```cpp
class Solution {
public:
    void getNext (int* next, const string& s){
        next[0] = 0;
        int j = 0;
        for(int i = 1;i < s.size(); i++){
            while(j > 0 && s[i] != s[j]) {
                j = next[j - 1];
            }
            if(s[i] == s[j]) {
                j++;
            }
            next[i] = j;
        }
    }
    bool repeatedSubstringPattern (string s) {
        if (s.size() == 0) {
            return false;
        }
        int next[s.size()];
        getNext(next, s);
        int len = s.size();
        if (next[len - 1] != 0 && len % (len - (next[len - 1] )) == 0) {
            return true;
        }
        return false;
    }
};
```

* 时间复杂度: O(n)
* 空间复杂度: O(n)

## 其他语言版本

### Python：

（版本一） 前缀表 减一

```python
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:  
        if len(s) == 0:
            return False
        nxt = [0] * len(s)
        self.getNext(nxt, s)
        if nxt[-1] != -1 and len(s) % (len(s) - (nxt[-1] + 1)) == 0:
            return True
        return False
  
    def getNext(self, nxt, s):
        nxt[0] = -1
        j = -1
        for i in range(1, len(s)):
            while j >= 0 and s[i] != s[j+1]:
                j = nxt[j]
            if s[i] == s[j+1]:
                j += 1
            nxt[i] = j
        return nxt
```

（版本二） 前缀表 不减一

```python
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:  
        if len(s) == 0:
            return False
        nxt = [0] * len(s)
        self.getNext(nxt, s)
        if nxt[-1] != 0 and len(s) % (len(s) - nxt[-1]) == 0:
            return True
        return False
  
    def getNext(self, nxt, s):
        nxt[0] = 0
        j = 0
        for i in range(1, len(s)):
            while j > 0 and s[i] != s[j]:
                j = nxt[j - 1]
            if s[i] == s[j]:
                j += 1
            nxt[i] = j
        return nxt
```

（版本三） 使用 find

```python
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        if n <= 1:
            return False
        ss = s[1:] + s[:-1] 
        print(ss.find(s))            
        return ss.find(s) != -1
```

（版本四） 暴力法

```python
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        if n <= 1:
            return False
      
        substr = ""
        for i in range(1, n//2 + 1):
            if n % i == 0:
                substr = s[:i]
                if substr * (n//i) == s:
                    return True
              
        return False
```

# 八、字符串：总结篇

其实我们已经学习了十天的字符串了，从字符串的定义到库函数的使用原则，从各种反转到KMP算法，相信大家应该对字符串有比较深刻的认识了。

那么这次我们来做一个总结。

## 什么是字符串

字符串是若干字符组成的有限序列，也可以理解为是一个字符数组，但是很多语言对字符串做了特殊的规定，接下来我来说一说C/C++中的字符串。

在C语言中，把一个字符串存入一个数组时，也把结束符 '\\0'存入数组，并以此作为该字符串是否结束的标志。

例如这段代码：

```text
char a[5] = "asd";
for (int i = 0; a[i] != '\0'; i++) {
}
```

在C++中，提供一个string类，string类会提供 size接口，可以用来判断string类字符串是否结束，就不用'\\0'来判断是否结束。

例如这段代码:

```text
string a = "asd";
for (int i = 0; i < a.size(); i++) {
}
```

那么vector< char > 和 string 又有什么区别呢？

其实在基本操作上没有区别，但是 string提供更多的字符串处理的相关接口，例如string 重载了+，而vector却没有。

所以想处理字符串，我们还是会定义一个string类型。

## 要不要使用库函数

在文章[344.反转字符串 **(opens new window)**](https://programmercarl.com/0344.%E5%8F%8D%E8%BD%AC%E5%AD%97%E7%AC%A6%E4%B8%B2.html)中强调了**打基础的时候，不要太迷恋于库函数。**

甚至一些同学习惯于调用substr，split，reverse之类的库函数，却不知道其实现原理，也不知道其时间复杂度，这样实现出来的代码，如果在面试现场，面试官问：“分析其时间复杂度”的话，一定会一脸懵逼！

所以建议**如果题目关键的部分直接用库函数就可以解决，建议不要使用库函数。**

**如果库函数仅仅是 解题过程中的一小部分，并且你已经很清楚这个库函数的内部实现原理的话，可以考虑使用库函数。**

## 双指针法

在[344.反转字符串 **(opens new window)**](https://programmercarl.com/0344.%E5%8F%8D%E8%BD%AC%E5%AD%97%E7%AC%A6%E4%B8%B2.html)，我们使用双指针法实现了反转字符串的操作，**双指针法在数组，链表和字符串中很常用。**

接着在[字符串：替换空格 **(opens new window)**](https://programmercarl.com/%E5%89%91%E6%8C%87Offer05.%E6%9B%BF%E6%8D%A2%E7%A9%BA%E6%A0%BC.html)，同样还是使用双指针法在时间复杂度O(n)的情况下完成替换空格。

**其实很多数组填充类的问题，都可以先预先给数组扩容带填充后的大小，然后在从后向前进行操作。**

那么针对数组删除操作的问题，其实在[27. 移除元素 **(opens new window)**](https://programmercarl.com/0027.%E7%A7%BB%E9%99%A4%E5%85%83%E7%B4%A0.html)中就已经提到了使用双指针法进行移除操作。

同样的道理在[151.翻转字符串里的单词 **(opens new window)**](https://programmercarl.com/0151.%E7%BF%BB%E8%BD%AC%E5%AD%97%E7%AC%A6%E4%B8%B2%E9%87%8C%E7%9A%84%E5%8D%95%E8%AF%8D.html)中我们使用O(n)的时间复杂度，完成了删除冗余空格。

一些同学会使用for循环里调用库函数erase来移除元素，这其实是O(n^2)的操作，因为erase就是O(n)的操作，所以这也是典型的不知道库函数的时间复杂度，上来就用的案例了。

## 反转系列

在反转上还可以在加一些玩法，其实考察的是对代码的掌控能力。

[541. 反转字符串II **(opens new window)**](https://programmercarl.com/0541.%E5%8F%8D%E8%BD%AC%E5%AD%97%E7%AC%A6%E4%B8%B2II.html)中，一些同学可能为了处理逻辑：每隔2k个字符的前k的字符，写了一堆逻辑代码或者再搞一个计数器，来统计2k，再统计前k个字符。

其实**当需要固定规律一段一段去处理字符串的时候，要想想在在for循环的表达式上做做文章**。

只要让 i += (2 \* k)，i 每次移动 2 \* k 就可以了，然后判断是否需要有反转的区间。

因为要找的也就是每2 \* k 区间的起点，这样写程序会高效很多。

在[151.翻转字符串里的单词 **(opens new window)**](https://programmercarl.com/0151.%E7%BF%BB%E8%BD%AC%E5%AD%97%E7%AC%A6%E4%B8%B2%E9%87%8C%E7%9A%84%E5%8D%95%E8%AF%8D.html)中要求翻转字符串里的单词，这道题目可以说是综合考察了字符串的多种操作。是考察字符串的好题。

这道题目通过 **先整体反转再局部反转**，实现了反转字符串里的单词。

后来发现反转字符串还有一个牛逼的用处，就是达到左旋的效果。

在[字符串：反转个字符串还有这个用处？ **(opens new window)**](https://programmercarl.com/%E5%89%91%E6%8C%87Offer58-II.%E5%B7%A6%E6%97%8B%E8%BD%AC%E5%AD%97%E7%AC%A6%E4%B8%B2.html)中，我们通过**先局部反转再整体反转**达到了左旋的效果。

## KMP

KMP的主要思想是**当出现字符串不匹配时，可以知道一部分之前已经匹配的文本内容，可以利用这些信息避免从头再去做匹配了。**

KMP的精髓所在就是前缀表，在[KMP精讲 **(opens new window)**](https://programmercarl.com/0028.%E5%AE%9E%E7%8E%B0strStr.html)中提到了，什么是KMP，什么是前缀表，以及为什么要用前缀表。

前缀表：起始位置到下标i之前（包括i）的子串中，有多大长度的相同前缀后缀。

那么使用KMP可以解决两类经典问题：

1. 匹配问题：[28. 实现 strStr()(opens new window)](https://programmercarl.com/0028.%E5%AE%9E%E7%8E%B0strStr.html)
2. 重复子串问题：[459.重复的子字符串(opens new window)](https://programmercarl.com/0459.%E9%87%8D%E5%A4%8D%E7%9A%84%E5%AD%90%E5%AD%97%E7%AC%A6%E4%B8%B2.html)

再一次强调了什么是前缀，什么是后缀，什么又是最长相等前后缀。

前缀：指不包含最后一个字符的所有以第一个字符开头的连续子串。

后缀：指不包含第一个字符的所有以最后一个字符结尾的连续子串。

然后**针对前缀表到底要不要减一，这其实是不同KMP实现的方式**，我们在[KMP精讲 **(opens new window)**](https://programmercarl.com/0028.%E5%AE%9E%E7%8E%B0strStr.html)中针对之前两个问题，分别给出了两个不同版本的的KMP实现。

其中主要**理解j=next[x]这一步最为关键！**

## 总结

字符串类类型的题目，往往想法比较简单，但是实现起来并不容易，复杂的字符串题目非常考验对代码的掌控能力。

双指针法是字符串处理的常客。

KMP算法是字符串查找最重要的算法，但彻底理解KMP并不容易，我们已经写了五篇KMP的文章，不断总结和完善，最终才把KMP讲清楚。

好了字符串相关的算法知识就介绍到了这里了，明天开始新的征程，大家加油！
