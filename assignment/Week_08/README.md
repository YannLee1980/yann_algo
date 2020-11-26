# 算法训练营
---
## 第8周：
---
### **本周内容一览：**
### 第16课 位运算：
1. 位运算基础及实战要点:
   * 位运算符：

                >> : 右移
                << : 左移
                ^ : 按位异或
                ~ : 按位取反
                & : 按位与
                | : 按位或
    * XOR-异或：

                异或:相同为 0，不同为 1。也可用“不进位加法”来理解。 异或操作的一些特点:
                x^0=x
                x^1s=~x //注意 1s = ~0
                x^(~x)=1s
                x^x=0
                c=a^b => a^c=b,b^c=a //交换两个数 a^b^c=a^(b^c)=(a^b)^c //associative
    * 指定位置的位运算：

                 1. 将x最右边的n位清零:x&(~0<<n)
                 2. 获取x的第n位值(0或者1):(x>>n)&1
                 3. 获取x的第n位的幂值:x&(1<<n)
                 4. 仅将第n位置为1:x|(1<<n)
                 5. 仅将第n位置为0:x&(~(1<<n))
                 6. 将x最高位至第n位(含)清零:x&((1<<n)-1)
    * 实战位运算：

                • 判断奇偶:
                x%2==1 —>(x&1)==1 x%2==0 —>(x&1)==0
                • x>>1—>x/2.
                即: x=x/2; —> x=x>>1;
                mid=(left+right)/2; —> mid=(left+right)>>1;
                • X=X&(X-1)清零最低位的1  # 常用
                • X&-X=>得到最低位的1  # 常用
                • X&~X=>0
2. 位运算实战题目解析:
    >参考链接
    N 皇后位运算代码示例:https://shimo.im/docs/YzWa5ZZrZPYWahK2
    实战题目 / 课后作业
    位 1 的个数（Facebook、苹果在半年内面试中考过）:https://leetcode-cn.com/problems/number-of-1-bits/
    2 的幂（谷歌、亚马逊、苹果在半年内面试中考过）:https://leetcode-cn.com/problems/power-of-two/
    颠倒二进制位（苹果在半年内面试中考过）:https://leetcode-cn.com/problems/reverse-bits/
    N 皇后（字节跳动、亚马逊、百度在半年内面试中考过）:https://leetcode-cn.com/problems/n-queens/description/
    N 皇后 II （亚马逊在半年内面试中考过）:https://leetcode-cn.com/problems/n-queens-ii/description/
    比特位计数（字节跳动、Facebook、MathWorks 在半年内面试中考过）:https://leetcode-cn.com/problems/counting-bits/description/

### 第17课 布隆过滤和LRU缓存：
1. 布隆过滤器的实现及应用：
    * Bloom Filter:一个很长的二进制向量和一系列随机映射函数。布隆过滤器可以用于检索 一个元素是否在一个集合中。
    * 查询结果：不存在----一定不存在；存在----不一定存在；
    * 应用：
        1. 比特币网络
        2. 分布式系统(Map-Reduce) — Hadoop、search engine
        3. Redis 缓存
        4. 垃圾邮件、评论等的过滤
    * 简单的BloomFilter：

                from bitarray import bitarray
                import mmh3
                class BloomFilter:
                    def __init__(self, size, hash_num):
                        self.size = size
                        self.hash_num = hash_num
                        self.bit_array = bitarray(size)
                        self.bit_array.setall(0)
                    
                    def add(self, s):
                        for seed in range(self.hash_num):
                            result = mmh3.hash(s, seed) % self.size
                            self.bit_array[result] = 1
                    
                    def lookup(self, s):
                        for seed in range(self.hash_num):
                            result = mmh3.hash(s, seed) % self.size
                            if self.bit_array[result] == 0:
                                return 'Nope'
                        return 'Probably'
                bf = BloomFilter(500000, 7)
                bf.add("dantezhao")
                bf.lookup("dantezhao")
    >参考链接
    布隆过滤器的原理和实现: https://www.cnblogs.com/cpselvis/p/6265825.html
    使用布隆过滤器解决缓存击穿、垃圾邮件识别、集合判重: https://blog.csdn.net/tianyaleixiaowu/article/details/74721877
    布隆过滤器 Python 代码示例:https://shimo.im/docs/UITYMj1eK88JCJTH
    布隆过滤器 Python 实现示例: https://www.geeksforgeeks.org/bloom-filters-introduction-and-python-implementation/
    高性能布隆过滤器 Python 实现示例:https://github.com/jhgg/pybloof
    布隆过滤器 Java 实现示例 1: https://github.com/lovasoa/bloomfilter/blob/master/src/main/java/BloomFilter.java
    布隆过滤器 Java 实现示例 2:https://github.com/Baqend/Orestes-Bloomfilter
2. LRU Cache的实现、应用和题解:
    * LRU Cache：
        • 两个要素: 大小 、替换策略
        • Hash Table + Double LinkedList
        • O(1) 查询
        O(1) 修改、更新
    * LFU - least frequently used LRU - least recently used
    * 实现：

                class LRUCache:

                    def __init__(self, capacity: int):
                        self.dic = collections.OrderedDict()
                        self.remain = capacity

                    def get(self, key: int) -> int:
                        if key not in self.dic:
                            return -1
                        v = self.dic.pop(key)
                        self.dic[key] = v
                        return v

                    def put(self, key: int, value: int) -> None:
                        if key in self.dic:
                            self.dic.pop(key)
                        else:
                            if self.remain > 0:
                                self.remain -= 1
                            else:
                                self.dic.popitem(last = False)
                        self.dic[key] = value
    >参考链接
    Understanding the Meltdown exploit: https://www.sqlpassion.at/archive/2018/01/06/understanding-the-meltdown-exploit-in-my-own-simple-words/
    替换算法总揽: https://en.wikipedia.org/wiki/Cache_replacement_policies
    LRU Cache Python 代码示例:https://shimo.im/docs/CoyPAyXooGcDuLQo
    实战题目 / 课后作业
    LRU 缓存机制（亚马逊、字节跳动、Facebook、微软在半年内面试中常考）: https://leetcode-cn.com/problems/lru-cache/#/


### 第18课 排序算法：
1. 初级排序和高级排序的实现和特性
   * 快速排序：

                # 代码模版：
                class QuickSort:
                    def quickSort(self, begin, end, nums):
                        if begin >= end:
                            return
                        pivot = self._partition(begin, end, nums)
                        self.quickSort(begin, pivot - 1, nums)
                        self.quickSort(pivot + 1, end, nums)

                    def _partition(self, begin, end, nums):
                        pivot, counter = end, begin
                        for i in range(begin, end):
                            if nums[i] < nums[pivot]:
                                # 保持位置counter的值是第一个大于nums[pivot]的，counter左边的值都小于nums[pivot]
                                nums[i], nums[counter] = nums[counter], nums[i]
                                counter += 1
                        nums[counter], nums[pivot] = nums[pivot], nums[counter]
                        return counter

                a = [3,5,63,71,834,9,-34,5,-6,-7]
                q = QuickSort()
                q.quickSort(0, len(a)-1, a)
                print(a)
    * 归并排序：

                # 代码：
                class MergeSort:
                    def mergesort(self, nums, left, right):
                        if left >= right:
                            return None
                        mid = (left + right) >> 1
                        self.mergesort(nums, left, mid)
                        self.mergesort(nums, mid+1, right)
                        self._merge(nums, left, mid, right)

                    def _merge(self, nums, left, mid, right):
                        tmp = []
                        i, j = left, mid + 1
                        
                        while i <= mid and j <= right:
                            if nums[i] <= nums[j]:
                                tmp.append(nums[i])
                                i += 1
                            else:
                                tmp.append(nums[j])
                                j += 1
                        while i <= mid:
                            tmp.append(nums[i])
                            i += 1
                        while j <= right:
                            tmp.append(nums[j])
                            j += 1

                        nums[left:right+1] = tmp


                a = [3,5,4464,7,0,-498,9,4,-5,6,7]
                q = MergeSort()
                q.mergesort(a, 0, len(a)-1)
                print(a)
    * 堆排序：
  
                # 堆排序：
                import heapq
                class HeapSort:
                    def heapSort(self, nums):
                        heap = []
                        for n in nums:
                            heapq.heappush(heap, n)
                        for i in range(len(nums)):
                            nums[i] = heapq.heappop(heap)

                a = [3,5,6,-897,38,-9,4,5,633,7]
                q = HeapSort()
                q.heapSort(a)
                print(a)

    * 初级排序代码：

                # 冒泡排序：
                class BubbleSort:
                    def bubbleSort(self, nums):
                        n = len(nums)
                        for i in range(n):
                            for j in range(n-i-1):
                                if nums[j] > nums[j+1]:
                                    nums[j], nums[j+1] = nums[j+1], nums[j]

                # 选择排序：
                class SelectionSort:
                    def selectionSort(self, nums):
                        n = len(nums)
                        for i in range(n):
                            min_index = i
                            for j in range(i+1, n):
                                if nums[j] < nums[min_index]:
                                    min_index = j
                            nums[i], nums[min_index] = nums[min_index], nums[i]

                # 插入排序：
                class InsertionSort:
                    def insertionSort(self, nums):
                        n = len(nums)
                        pre_index = 0
                        current = 0
                        for i in range(1, n):
                            pre_index = i-1
                            current = nums[i]
                            while pre_index >= 0 and nums[pre_index] > current:
                                nums[pre_index+1] = nums[pre_index]
                                pre_index -= 1
                            nums[pre_index+1] = current

    >参考链接
    十大经典排序算法: https://www.cnblogs.com/onepixel/p/7674659.html
    快速排序代码示例:https://shimo.im/docs/TX9bDbSC7C0CR5XO
    归并排序代码示例:https://shimo.im/docs/sDXxjjiKf3gLVVAU
    堆排序代码示例:https://shimo.im/docs/M2xfacKvwzAykhz6
2. 特殊排序及实战题目详解:
    * 特殊排序:
        • 计数排序(Counting Sort) 计数排序要求输入的数据必须是有确定范围的整数。将输入的数据值转化为键存 储在额外开辟的数组空间中;然后依次把计数大于 1 的填充回原数组
        • 桶排序(Bucket Sort)
        桶排序 (Bucket sort)的工作的原理:假设输入数据服从均匀分布，将数据分到 有限数量的桶里，每个桶再分别排序(有可能再使用别的排序算法或是以递归方 式继续使用桶排序进行排)。
        • 基数排序(Radix Sort) 基数排序是按照低位先排序，然后收集;再按照高位排序，然后再收集;依次类 推，直到最高位。有时候有些属性是有优先级顺序的，先按低优先级排序，再按 高优先级排序。
    * 逆数对和翻转对：
        * 翻转对、逆数对： 493. 翻转对：https://leetcode-cn.com/problems/reverse-pairs/
        * 剑指 Offer 51. 数组中的逆序对： https://leetcode-cn.com/problems/shu-zu-zhong-de-ni-xu-dui-lcof/

    >参考链接
    十大经典排序算法:https://www.cnblogs.com/onepixel/p/7674659.html
    9 种经典排序算法可视化动画:https://www.bilibili.com/video/av25136272
    6 分钟看完 15 种排序算法动画展示:https://www.bilibili.com/video/av63851336
    实战题目 / 课后作业
    数组的相对排序（谷歌在半年内面试中考过）:https://leetcode-cn.com/problems/relative-sort-array/
    有效的字母异位词（Facebook、亚马逊、谷歌在半年内面试中考过）:https://leetcode-cn.com/problems/valid-anagram/
    力扣排行榜（此题选做；Bloomberg 在半年内面试中考过）:https://leetcode-cn.com/problems/design-a-leaderboard/
    合并区间（Facebook、字节跳动、亚马逊在半年内面试中常考）:https://leetcode-cn.com/problems/merge-intervals/
    翻转对（字节跳动在半年内面试中考过）:https://leetcode-cn.com/problems/reverse-pairs/
#### **漂亮代码收集：**



#### **Python语法注意：**

#### **对代码对一些理解：**


#### **需要理解的地方：**

