# 算法训练营
---
## 第0周：预备周
### **本周内容一览：**
### 1.如何高效学习算法训练营课程与纵览
* 三分看视频理解，七分做练习：
  * 不要死磕； 
  * 敢于放手，敢于死记硬背代码；
  * 不懒于看高手代码；
  * LeetCode题目做5遍。
  
* 数据结构：
  * 一维:
    • 基础:数组 array (string), 链表 linked list
    • 高级:栈 stack, 队列 queue, 双端队列 deque, 集合 set, 映射 map (hash or map), etc
  * 二维:
    • 基础:树 tree, 图 graph
    • 高级:二叉搜索树 binary search tree (red-black tree, AVL), 堆 heap, 并查集 disjoint set, 字典树 Trie, etc
  * 特殊:
    • 位运算 Bitwise, 布隆过滤器 BloomFilter 
    • LRU Cache（缓存）
  
* 算法：
  • If-else, switch —> branch
  • for, while loop —> Iteration
  • 递归 Recursion (Divide & Conquer, Backtrace)
  **以上三条为基本**
  • 搜索 Search: 深度优先搜索 Depth first search, 广度优先搜索 Breadth first search, A*, etc
  • 动态规划 Dynamic Programming
  • 二分查找 Binary Search
  • 贪心 Greedy
  • 数学 Math , 几何 Geometry
  注意:在头脑中回忆上面每种算法的思想和代码模板
  **以上算法的根本是找到重复单元**

* 刻意练习：
  * 刻意练习 — 过遍数(五毒神掌)
  * 练习缺陷、弱点地方
  * 不舒服、不爽、枯燥
  * 训练基本动作

* 反馈：
  • 即时反馈
  • 主动型反馈(自己去找)
    • 高手代码 (GitHub, LeetCode, etc.)
  • 被动式反馈(高手给你指点)
    • code review

* 切题四件套：
  • Clarification（交流明确题目的用意）
  • Possible solutions（所有可能的方法）
    • compare (time/space)
    • optimal(加强) 
  • Coding(多写)
  • Test cases

* 五步刷题法（五毒神掌）：
  1. 第一遍：
     * 5分钟:读题 + 思考
     * 直接看解法:注意!多解法，比较解法优劣 
     * 背诵、默写好的解法
  2. 第二遍：
     * 马上自己写 —> LeetCode 提交
     * 多种解法比较、体会 —> 优化!
  3. 第三遍：
  • 过了一天后，再重复做题
  • 不同解法的熟练程度 —> 专项练习
  4. 第四遍：
  • 过了一周:反复回来练习相同题目
  5. 第五遍：
  • 面试前一周恢复性训练

### 2.训练准备和复制度分析：
* 时间复杂度： Big O notation
  O(1): Constant Complexity 常数复杂度
  O(log n): Logarithmic Complexity 对数复杂度 
  O(n): Linear Complexity 线性时间复杂度
  O(n^2): N square Complexity 平方
  O(n^3): N cubic Complexity 立方
  O(2^n): Exponential Growth 指数
  O(n!): Factorial 阶乘
* 例子：

      O(log(n)):
      for (int i = 1; i < n; i = i * 2) {
        System.out.println("Hey - I'm busy looking at: " + i);
      }
      O(k^n):
      int fib(int n) {
        if (n < 2) return n;
        return fib(n - 1) + fib(n - 2);
      }
*  Master Theorem：

* 以下各算法的时间复杂度：
  二叉树遍历 - 前序、中序、后序:O(N) 
  图的遍历:O(N)
  搜索算法:DFS、BFS - O(N) 
  二分查找:O(logN)
* 空间复杂度：
  1. 数组的长度
  2. 递归的深度(特殊说明)
  实例分析: https://leetcode-cn.com/problems/climbing- stairs/solution/pa-lou-ti-by-leetcode/
* 参考资料：
  >Windows Microsoft New Terminal:https://github.com/microsoft/terminal
  >VS Code Themes:https://vscodethemes.com/
  >教你打造一款颜值逆天的 VS Code:https://toutiao.io/posts/7w5ixl/preview
  >炫酷的 VS Code 毛玻璃效果:https://juejin.im/post/6844903846871842823
  >自顶向下的编程方式:http://markhneedham.com/blog/2008/09/15/clean-code-book-review/c
  >自顶向下编程的 LeetCode 例题:https://leetcode-cn.com/problems/valid-palindrome/

## 第1周：
### **本周内容一览：**
### 第3课：数组、链表、跳表
1. 数组、链表、跳表的基本实现和特性
* Array： 

  | 操作 | 时间复杂度 | 备注 |
  | :---: | :---: | :--- |
  | prepend | O(1) | 在最前面添加，正常情况是O(n)，但现在做了优化，申请的时候会预留较大的区域。
  | append | O(1) |
  | lookup | O(1) |
  | insert | O(n) |
  | delect | O(n) |
  
* Linked List：
    | 操作 | 时间复杂度 | 备注 |
  | :---: | :---: | :--- |
  | prepend | O(1) | 
  | append | O(1) |
  | lookup | O(n) |
  | insert | O(1) |
  | delect | O(1) |
* Skip List:
  注意:只能用于元素有序的情况。
  所以，跳表(skip list)对标的是平衡树(AVL Tree)和二分查找， 是一种 插入/删除/搜索 都是 O(log n) 的数据结构。1989 年出现。
  它最大的优势是原理简单、容易实现、方便扩展、效率更高。因此 在一些热门的项目里用来替代平衡树，如 Redis、LevelDB 等。
  | 操作 | 时间复杂度 | 备注 |
  | :---: | :---: | :--- |
  | prepend | O(1) | 
  | append | O(1) |
  | lookup | O(log n) |
  | insert | O(log n) |
  | delect | O(log n) |
  空间复杂度：O(n)
* 工程中的应用：
  >LRU Cache - Linked list
  https://www.jianshu.com/p/b1ab4a170c3c https://leetcode-cn.com/problems/lru-cache
  Redis - Skip List
  https://redisbook.readthedocs.io/en/latest/internal- datastruct/skiplist.html https://www.zhihu.com/question/20202931
  LevelDB - Skip List
* 小结：
  * 数组、链表、跳表的原理和实现 
  * 三者的时间复杂度、空间复杂度 
  * 工程运用
  * 跳表:升维思想 + 空间换时间
* 参考链接：
  >Java 源码分析（ArrayList）：http://developer.classpath.org/doc/java/util/ArrayList-source.html
  >Linked List 的标准实现代码：https://www.geeksforgeeks.org/implementing-a-linked-list-in-java-using-class/
  >Linked List 示例代码：http://www.cs.cmu.edu/~adamchik/15-121/lectures/Linked%20Lists/code/LinkedList.java
  >Java 源码分析（LinkedList）：http://developer.classpath.org/doc/java/util/LinkedList-source.html
  >LRU Cache - Linked list： LRU 缓存机制：https://leetcode-cn.com/problems/lru-cache/
  >Redis - Skip List：跳跃表、为啥 Redis 使用跳表（Skip List）而不是使用 Red-Black？：https://www.zhihu.com/question/20202931

* 疑惑：
  1. java的内部类，Python有内部类吗？

2. 实战题目解析：移动零
   * 给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
   * **双指针操作**：

          class Solution:
          def moveZeroes(self, nums: list) -> None:
              """
              Do not return anything, modify nums in-place instead.
              """
              j = 0 
              for i in range(len(nums)):
                  if nums[i] is not 0:
                      nums[j], nums[i] = nums[i], nums[j]
                      j += 1
   * 参考资料：
    >Array 实战题目
    >盛最多水的容器（腾讯、百度、字节跳动在近半年内面试常考）:https://leetcode-cn.com/problems/container-with-most-water/
    >移动零（华为、字节跳动在近半年内面试常考）:https://leetcode-cn.com/problems/move-zeroes/
    >爬楼梯（阿里巴巴、腾讯、字节跳动在半年内面试常考）:https://leetcode-cn.com/problems/climbing-stairs/
    >三数之和（国内、国际大厂历年面试高频老题）:https://leetcode-cn.com/problems/3sum/         
3. 实战题目解析：盛水最多的容器、爬楼梯
   * 给你 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
   * **穷举数列中各数二元组合**：

                for i in range(len(height)-1):
                    for j in range(i+1, len(height)):
                        area = min(height[i], height[j]) * (j - i)
   * **夹逼法向中间靠近**：

        #java:
        class Solution {
            public int maxArea(int[] height) {
                int max = 0;
                for(int i = 0, j = height.length - 1; i < j ; ) {
                    int min_height = height[i] < height[j] ? height[i ++] : height[j --];
                    int area = min_height * (j - i + 1);
                    max = Math.max(area, max);
                }
                return max;
            }
        }
   * 假设你正在爬楼梯。需要 n 阶你才能到达楼顶。每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？注意：给定 n 是一个正整数。(**Fibonacci数列**)
   * **逆向思维（自顶向下）**：

        class Solution:
            def climbStairs(self, n: int) -> int:
                if n <= 2 :
                    return n
                if n > 2:
                    f1, f2, f3 = 1, 2, 3
                    for _ in range(3, n+1):
                        f3 = f1 + f2
                        f1 = f2
                        f2 = f3
                    return f3
   * 三数之和：
    **两边夹逼法(三指针的操作，先固定一指针，再夹逼另外两指针)**
   * 强调：
      * 做题一题做5遍；
      * 优化思想：空间换时间，可把一维升为两维；
      * 泛化思维：找最近重复的子问题。
      * 递归思维：递归的时间复杂度是O(2^n)
      * 逆向思维：自顶向下的思维
      * 动态规划
   * Python注意：
      list 的 sorted(): sorted(l) -- 不改变l本身，返回数列；
      list 的 sort(): l.sort() -- 改变l本身，返回None.

    * 参考资料：
    >Linked List 实战题目:
    >反转链表（字节跳动、亚马逊在半年内面试常考）:https://leetcode-cn.com/problems/reverse-linked-list/
    >两两交换链表中的节点（阿里巴巴、字节跳动在半年内面试常考）:https://leetcode-cn.com/problems/swap-nodes-in-pairs/
    >环形链表（阿里巴巴、字节跳动、腾讯在半年内面试常考）:https://leetcode-cn.com/problems/linked-list-cycle/
    >环形链表 II:https://leetcode-cn.com/problems/linked-list-cycle-ii/
    >K 个一组翻转链表（字节跳动、猿辅导在半年内面试常考）:https://leetcode-cn.com/problems/reverse-nodes-in-k-group/

### 第4课. 栈、队列、优先队列、双端队列：
1. 栈和队列的实现与特性：
  * Stack:先入后出;添加、删除皆为 O(1)
  * Queue:先入先出;添加、删除皆为 O(1)
  * Deque:简单理解:- double ended queue(两端可以进出Queue),插入和删除都是 O(1) 操作.
  * python 的 deque： collections包

* 参考链接
  >Java 的 PriorityQueue 文档:https://docs.oracle.com/javase/10/docs/api/java/util/PriorityQueue.html
  >Java 的 Stack 源码:http://developer.classpath.org/doc/java/util/Stack-source.html
  >Java 的 Queue :(http://fuseyism.com/classpath/doc/java/util/Queue-source.html)
  >Python 的 heapq:https://docs.python.org/2/library/heapq.html
  >高性能的 container 库:https://docs.python.org/2/library/collections.html

2. 实战题目解析：有效的括号、最小栈等问题
  * **用栈解决问题**：有效的括号、柱状图中最大的矩形
  * **双栈解决问题**，减少使用空间：最小栈
  * 预习题目
  有效的括号（亚马逊、JPMorgan 在半年内面试常考）
  最小栈（亚马逊在半年内面试常考）
  * 实战题目
  柱状图中最大的矩形（亚马逊、微软、字节跳动在半年内面试中考过）
  滑动窗口最大值（亚马逊在半年内面试常考）
  * 课后作业
  用 add first 或 add last 这套新的 API 改写 Deque 的代码
  分析 Queue 和 Priority Queue 的源码
  设计循环双端队列（Facebook 在 1 年内面试中考过）
  接雨水（亚马逊、字节跳动、高盛集团、Facebook 在半年内面试常考）

### 疑问：
   1.   滑动窗口最大值：https://leetcode-cn.com/problems/sliding-window-maximum/
   2.   环形链表 II: https://leetcode-cn.com/problems/linked-list-cycle-ii/
   3.   K 个一组翻转链表: https://leetcode-cn.com/problems/reverse-nodes-in-k-group/