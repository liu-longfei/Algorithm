# 一、232.用栈实现队列

[力扣题目链接(opens new window)](https://leetcode.cn/problems/implement-queue-using-stacks/)

使用栈实现队列的下列操作：

push(x) -- 将一个元素放入队列的尾部。
pop() -- 从队列首部移除元素。
peek() -- 返回队列首部的元素。
empty() -- 返回队列是否为空。

示例:

```cpp
MyQueue queue = new MyQueue();
queue.push(1);
queue.push(2);
queue.peek();  // 返回 1
queue.pop();   // 返回 1
queue.empty(); // 返回 false
```

说明:

* 你只能使用标准的栈操作 -- 也就是只有 push to top, peek/pop from top, size, 和 is empty 操作是合法的。
* 你所使用的语言也许不支持栈。你可以使用 list 或者 deque（双端队列）来模拟一个栈，只要是标准的栈操作即可。
* 假设所有操作都是有效的 （例如，一个空的队列不会调用 pop 或者 peek 操作）。

## 算法公开课

[《代码随想录》算法视频公开课 **(opens new window)**](https://programmercarl.com/other/gongkaike.html)：[栈的基本操作！ | LeetCode：232.用栈实现队列 **(opens new window)**](https://www.bilibili.com/video/BV1nY4y1w7VC)，**相信结合视频再看本篇题解，更有助于大家对本题的理解**。

## 思路

这是一道模拟题，不涉及到具体算法，考察的就是对栈和队列的掌握程度。

使用栈来模式队列的行为，如果仅仅用一个栈，是一定不行的，所以需要两个栈**一个输入栈，一个输出栈**，这里要注意输入栈和输出栈的关系。

下面动画模拟以下队列的执行过程：

执行语句：
queue.push(1);
queue.push(2);
queue.pop(); **注意此时的输出栈的操作**
queue.push(3);
queue.push(4);
queue.pop();
queue.pop();**注意此时的输出栈的操作**
queue.pop();
queue.empty();

https://code-thinking.cdn.bcebos.com/gifs/232.%E7%94%A8%E6%A0%88%E5%AE%9E%E7%8E%B0%E9%98%9F%E5%88%97%E7%89%88%E6%9C%AC2.gif（图像链接）

在push数据的时候，只要数据放进输入栈就好，**但在pop的时候，操作就复杂一些，输出栈如果为空，就把进栈数据全部导入进来（注意是全部导入**，再从出栈弹出数据，如果输出栈不为空，则直接从出栈弹出数据就可以了。

最后如何判断队列为空呢？**如果进栈和出栈都为空的话，说明模拟的队列为空了。**

在代码实现的时候，会发现pop() 和 peek()两个函数功能类似，代码实现上也是类似的，可以思考一下如何把代码抽象一下。

C++代码如下：

```cpp
class MyQueue {
public:
    stack<int> stIn;
    stack<int> stOut;
    /** Initialize your data structure here. */
    MyQueue() {

    }
    /** Push element x to the back of queue. */
    void push(int x) {
        stIn.push(x);
    }

    /** Removes the element from in front of queue and returns that element. */
    int pop() {
        // 只有当stOut为空的时候，再从stIn里导入数据（导入stIn全部数据）
        if (stOut.empty()) {
            // 从stIn导入数据直到stIn为空
            while(!stIn.empty()) {
                stOut.push(stIn.top());
                stIn.pop();
            }
        }
        int result = stOut.top();
        stOut.pop();
        return result;
    }

    /** Get the front element. */
    int peek() {
        int res = this->pop(); // 直接使用已有的pop函数
        stOut.push(res); // 因为pop函数弹出了元素res，所以再添加回去
        return res;
    }

    /** Returns whether the queue is empty. */
    bool empty() {
        return stIn.empty() && stOut.empty();
    }
};

```

* 时间复杂度: push和empty为O(1), pop和peek为O(n)
* 空间复杂度: O(n)

## 拓展

可以看出peek()的实现，直接复用了pop()， 要不然，对stOut判空的逻辑又要重写一遍。

再多说一些代码开发上的习惯问题，在工业级别代码开发中，最忌讳的就是 实现一个类似的函数，直接把代码粘过来改一改就完事了。

这样的项目代码会越来越乱，**一定要懂得复用，功能相近的函数要抽象出来，不要大量的复制粘贴，很容易出问题！（踩过坑的人自然懂）**

工作中如果发现某一个功能自己要经常用，同事们可能也会用到，自己就花点时间把这个功能抽象成一个好用的函数或者工具类，不仅自己方便，也方便了同事们。

同事们就会逐渐认可你的工作态度和工作能力，自己的口碑都是这么一点一点积累起来的！在同事圈里口碑起来了之后，你就发现自己走上了一个正循环，以后的升职加薪才少不了你！

## 其他语言版本

### Python：

```python
class MyQueue:

    def __init__(self):
        """
        in主要负责push，out主要负责pop
        """
        self.stack_in = []
        self.stack_out = []


    def push(self, x: int) -> None:
        """
        有新元素进来，就往in里面push
        """
        self.stack_in.append(x)


    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if self.empty():
            return None
    
        if self.stack_out:
            return self.stack_out.pop()
        else:
            for i in range(len(self.stack_in)):
                self.stack_out.append(self.stack_in.pop())
            return self.stack_out.pop()


    def peek(self) -> int:
        """
        Get the front element.
        """
        ans = self.pop()
        self.stack_out.append(ans)
        return ans


    def empty(self) -> bool:
        """
        只要in或者out有元素，说明队列不为空
        """
        return not (self.stack_in or self.stack_out)

```


# 二、225. 用队列实现栈

[力扣题目链接(opens new window)](https://leetcode.cn/problems/implement-stack-using-queues/)

使用队列实现栈的下列操作：

* push(x) -- 元素 x 入栈
* pop() -- 移除栈顶元素
* top() -- 获取栈顶元素
* empty() -- 返回栈是否为空

注意:

* 你只能使用队列的基本操作-- 也就是 push to back, peek/pop from front, size, 和 is empty 这些操作是合法的。
* 你所使用的语言也许不支持队列。 你可以使用 list 或者 deque（双端队列）来模拟一个队列 , 只要是标准的队列操作即可。
* 你可以假设所有操作都是有效的（例如, 对一个空的栈不会调用 pop 或者 top 操作）。

## 算法公开课

《代码随想录》算法视频公开课 **(opens new window)**](https://programmercarl.com/other/gongkaike.html)：[队列的基本操作！ | LeetCode：225. 用队列实现栈 **(opens new window)**](https://www.bilibili.com/video/BV1Fd4y1K7sm)，**[相信结合视频再看本篇题解，更有助于大家对本题的理解**。

## 思路

（这里要强调是单向队列）

有的同学可能疑惑这种题目有什么实际工程意义，**其实很多算法题目主要是对知识点的考察和教学意义远大于其工程实践的意义，所以面试题也是这样！**

刚刚做过[栈与队列：我用栈来实现队列怎么样？ **(opens new window)**](https://programmercarl.com/0232.%E7%94%A8%E6%A0%88%E5%AE%9E%E7%8E%B0%E9%98%9F%E5%88%97.html)的同学可能依然想着用一个输入队列，一个输出队列，就可以模拟栈的功能，仔细想一下还真不行！

**队列模拟栈，其实一个队列就够了**，那么我们先说一说两个队列来实现栈的思路。

**队列是先进先出的规则，把一个队列中的数据导入另一个队列中，数据的顺序并没有变，并没有变成先进后出的顺序。**

所以用栈实现队列， 和用队列实现栈的思路还是不一样的，这取决于这两个数据结构的性质。

但是依然还是要用两个队列来模拟栈，只不过没有输入和输出的关系，而是另一个队列完全用来备份的！

如下面动画所示，**用两个队列que1和que2实现队列的功能，que2其实完全就是一个备份的作用**，把que1最后面的元素以外的元素都备份到que2，然后弹出最后面的元素，再把其他元素从que2导回que1。

模拟的队列执行语句如下：

```cpp
queue.push(1);    
queue.push(2);    
queue.pop();   // 注意弹出的操作   
queue.push(3);    
queue.push(4);   
queue.pop();  // 注意弹出的操作  
queue.pop();  
queue.pop();  
queue.empty();  
```

https://code-thinking.cdn.bcebos.com/gifs/225.%E7%94%A8%E9%98%9F%E5%88%97%E5%AE%9E%E7%8E%B0%E6%A0%88.gif（图像链接）

详细如代码注释所示：

```cpp
class MyStack {
public:
    queue<int> que1;
    queue<int> que2; // 辅助队列，用来备份
    /** Initialize your data structure here. */
    MyStack() {

    }

    /** Push element x onto stack. */
    void push(int x) {
        que1.push(x);
    }

    /** Removes the element on top of the stack and returns that element. */
    int pop() {
        int size = que1.size();
        size--;
        while (size--) { // 将que1 导入que2，但要留下最后一个元素
            que2.push(que1.front());
            que1.pop();
        }

        int result = que1.front(); // 留下的最后一个元素就是要返回的值
        que1.pop();
        que1 = que2;            // 再将que2赋值给que1
        while (!que2.empty()) { // 清空que2
            que2.pop();
        }
        return result;
    }

    /** Get the top element. */
    int top() {
        return que1.back();
    }

    /** Returns whether the stack is empty. */
    bool empty() {
        return que1.empty();
    }
};
```

* 时间复杂度: pop为O(n)，其他为O(1)
* 空间复杂度: O(n)

## 优化

其实这道题目就是用一个队列就够了。

**一个队列在模拟栈弹出元素的时候只要将队列头部的元素（除了最后一个元素外） 重新添加到队列尾部，此时再去弹出元素就是栈的顺序了。**

C++优化代码

```cpp
class MyStack {
public:
    queue<int> que;
    /** Initialize your data structure here. */
    MyStack() {

    }
    /** Push element x onto stack. */
    void push(int x) {
        que.push(x);
    }
    /** Removes the element on top of the stack and returns that element. */
    int pop() {
        int size = que.size();
        size--;
        while (size--) { // 将队列头部的元素（除了最后一个元素外） 重新添加到队列尾部
            que.push(que.front());
            que.pop();
        }
        int result = que.front(); // 此时弹出的元素顺序就是栈的顺序了
        que.pop();
        return result;
    }

    /** Get the top element. */
    int top() {
        return que.back();
    }

    /** Returns whether the stack is empty. */
    bool empty() {
        return que.empty();
    }
};
```

* 时间复杂度: pop为O(n)，其他为O(1)
* 空间复杂度: O(n)

## 其他语言版本

### Python：

```python
from collections import deque

class MyStack:

    def __init__(self):
        """
        Python普通的Queue或SimpleQueue没有类似于peek的功能
        也无法用索引访问，在实现top的时候较为困难。

        用list可以，但是在使用pop(0)的时候时间复杂度为O(n)
        因此这里使用双向队列，我们保证只执行popleft()和append()，因为deque可以用索引访问，可以实现和peek相似的功能

        in - 存所有数据
        out - 仅在pop的时候会用到
        """
        self.queue_in = deque()
        self.queue_out = deque()

    def push(self, x: int) -> None:
        """
        直接append即可
        """
        self.queue_in.append(x)


    def pop(self) -> int:
        """
        1. 首先确认不空
        2. 因为队列的特殊性，FIFO，所以我们只有在pop()的时候才会使用queue_out
        3. 先把queue_in中的所有元素（除了最后一个），依次出列放进queue_out
        4. 交换in和out，此时out里只有一个元素
        5. 把out中的pop出来，即是原队列的最后一个
      
        tip：这不能像栈实现队列一样，因为另一个queue也是FIFO，如果执行pop()它不能像
        stack一样从另一个pop()，所以干脆in只用来存数据，pop()的时候两个进行交换
        """
        if self.empty():
            return None

        for i in range(len(self.queue_in) - 1):
            self.queue_out.append(self.queue_in.popleft())
      
        self.queue_in, self.queue_out = self.queue_out, self.queue_in    # 交换in和out，这也是为啥in只用来存
        return self.queue_out.popleft()

    def top(self) -> int:
        """
        写法一：
        1. 首先确认不空
        2. 我们仅有in会存放数据，所以返回第一个即可（这里实际上用到了栈）
        写法二：
        1. 首先确认不空
        2. 因为队列的特殊性，FIFO，所以我们只有在pop()的时候才会使用queue_out
        3. 先把queue_in中的所有元素（除了最后一个），依次出列放进queue_out
        4. 交换in和out，此时out里只有一个元素
        5. 把out中的pop出来，即是原队列的最后一个，并使用temp变量暂存
        6. 把temp追加到queue_in的末尾
        """
        # 写法一：
        # if self.empty():
        #     return None
      
        # return self.queue_in[-1]    # 这里实际上用到了栈，因为直接获取了queue_in的末尾元素

        # 写法二：
        if self.empty():
            return None

        for i in range(len(self.queue_in) - 1):
            self.queue_out.append(self.queue_in.popleft())
      
        self.queue_in, self.queue_out = self.queue_out, self.queue_in 
        temp = self.queue_out.popleft()   
        self.queue_in.append(temp)
        return temp


    def empty(self) -> bool:
        """
        因为只有in存了数据，只要判断in是不是有数即可
        """
        return len(self.queue_in) == 0

```

优化，使用一个队列实现

```python
class MyStack:

    def __init__(self):
        self.que = deque()

    def push(self, x: int) -> None:
        self.que.append(x)

    def pop(self) -> int:
        if self.empty():
            return None
        for i in range(len(self.que)-1):
            self.que.append(self.que.popleft())
        return self.que.popleft()

    def top(self) -> int:
        # 写法一：
        # if self.empty():
        #     return None
        # return self.que[-1]

        # 写法二：
        if self.empty():
            return None
        for i in range(len(self.que)-1):
            self.que.append(self.que.popleft())
        temp = self.que.popleft()
        self.que.append(temp)
        return temp

    def empty(self) -> bool:
        return not self.que
```
