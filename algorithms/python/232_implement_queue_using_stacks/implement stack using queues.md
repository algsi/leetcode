# implement stack using queues

LeetCode 225

[implement stack using queues](https://leetcode-cn.com/problems/implement-stack-using-queues/)

[用队列实现栈](https://leetcode-cn.com/problems/implement-stack-using-queues/)

## 方法一 （两个队列，压入 - O(1)， 弹出 - O(n)）

栈是一种 后进先出（last in - first out， LIFO）的数据结构，栈内元素从顶端压入（push），从顶端弹出（pop）。一般我们用数组或者链表来实现栈，但是这篇文章会来介绍如何用队列来实现栈。队列是一种与栈相反的 先进先出（first in - first out， FIFO）的数据结构，队列中元素只能从 后端（rear）入队（push），然后从 前端（front）端出队（pop）。为了满足栈的特性，我们需要维护两个队列 q1 和 q2，另外，为了提高队列的 top 操作，我们额外使用一个变量来保存栈顶元素。

- push操作：
    元素入栈时，我们把它直接放入 q1 队列，并更新 top 栈顶元素

- pop操作：
    出栈时，我们先将队列 q1 的前 n-1 个元素都出队并入 q2 队列，这时 q1 还剩一个元素，也就是栈顶元素，我们只管将栈顶元素从 q1 出队即可。随后，我们通过将 q1，q2 互相交换的方式来避免把 q2 中的元素往 q1 中拷贝。

- top操作：
    因为我保存了栈顶元素，因此可以直接返回，否则，我们就还要像 pop 操作一样先出队再入队然后再获取栈顶元素。

Java实现如下：

```java
package leetcode;

import java.util.LinkedList;
import java.util.Queue;

/**
 * implement ctack using queues
 */
public class Solution {

    static class MyStack {

        private Queue<Integer> q1 = new LinkedList<>();
        private Queue<Integer> q2 = new LinkedList<>();

        // 保存栈顶元素，提高 top 效率
        int top;

        /**
         * Initialize your data structure here.
         */
        public MyStack() {

        }

        /**
         * Push element x onto stack.
         */
        public void push(int x) {
            q1.add(x);
            top = x;
        }

        /**
         * Removes the element on top of the stack and returns that element.
         */
        public int pop() {
            while (q1.size() > 1) {
                // 数据迁移
                top = q1.remove();
                q2.add(top);
            }
            int result = q1.remove();

            // 通过交换引用的方式来避免数据拷贝
            Queue<Integer> temp = q1;
            q1 = q2;
            q2 = temp;
            return result;
        }

        /**
         * Get the top element.
         */
        public int top() {
            // 直接返回栈顶元素
            return top;
        }

        /**
         * Returns whether the stack is empty.
         */
        public boolean empty() {
            return q1.isEmpty() && q2.isEmpty();
        }
    }
}
```

## 方法二 （两个队列， 压入 - O(n)， 弹出 - O(1)）

### push

接下来介绍的算法让每一个新元素从 q2 入队，同时把这个元素作为栈顶元素保存。当 q1 非空（也就是栈非空），我们让 q1 中所有的元素全部出队，再将出队的元素从 q2 入队。通过这样的方式，新元素（栈中的栈顶元素）将会在 q2 的前端。我们通过将 q1，q2 互相交换的方式来避免把 q2 中的元素往 q1 中拷贝。

### pop

直接让 q1 中元素出队，同时将出队后的 q1 中的队首元素作为栈顶元素保存。

## 方法三 （一个队列， 压入 - O(n)， 弹出 - O(1)）

上面介绍的两个方法都有一个缺点，它们都用到了两个队列。下面介绍的方法只需要使用一个队列。

当我们将一个元素从队列入队的时候，根据队列的性质这个元素会存在队列的后端。

但当我们实现一个栈的时候，最后入队的元素应该在前端，而不是在后端。为了实现这个目的，每当入队一个新元素的时候，我们可以把队列的顺序反转过来，以此来保证入栈的元素在队首。

Java实现

```java
package leetcode;

import java.util.LinkedList;
import java.util.NoSuchElementException;
import java.util.Queue;

/**
 * implement ctack using queues
 */
public class Solution {

    static class MyStack {

        private final Queue<Integer> queue = new LinkedList<>();

        /**
         * Initialize your data structure here.
         */
        public MyStack() {

        }

        /**
         * Push element x onto stack.
         */
        public void push(int x) {
            queue.add(x);
            int size = queue.size();
            while (size > 1) {
                // 队列反转，让新元素位于队首
                queue.add(queue.remove());
                size--;
            }
        }

        /**
         * Removes the element on top of the stack and returns that element.
         */
        public int pop() {
            if (queue.isEmpty()) {
                throw new NoSuchElementException();
            }
            return queue.remove();
        }

        /**
         * Get the top element.
         */
        public int top() {
            if (queue.isEmpty()) {
                throw new NoSuchElementException();
            }
            return queue.element();
        }

        /**
         * Returns whether the stack is empty.
         */
        public boolean empty() {
            return queue.isEmpty();
        }
    }
}
```
