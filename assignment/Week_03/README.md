# 算法训练营
---
## 第3周：
### **本周内容一览：**
### 第7课.泛型递归、树的递归：
1. 递归的实现、特性以及思维要点：
   * 递归与盗梦空间：
      * 向下进入到不同梦境中;
      * 向上又回到原来一层 通过声音同步回到上一层：
      * 每一层的环境和周围的人都是一份拷贝、 主角等几个人穿越不同层级的梦境(发生和携带变化)。
   * 递归的代码模版：

        def recursion(level, param1, param2, ...):
          # recursion terminator:------递归终止条件
          if level > MAX_LEVEL:
            process_result
            return
          
          # process logic in current level:------处理当前层，注意此处可设置处理后的返回值
          process(level, data)

          # drill down to next level:------下探到下一层
          self.recursion(level+1, param1, param2, ...)

          # reverse the current level status if needed------清理当前层，如果有必要
   * 递归注意点：
      * 不要人肉进行递归(最大误区) -- 熟悉递归结构
      * 找到最近最简方法，将其拆解成可重复解决的问题(重复子问题)--**最近重复子问题**
      * 数学归纳法思维：`n = 1, n= 2 成立` -> `n = k 成立`
   * 参考资料：
      >实战题目
      爬楼梯（阿里巴巴、腾讯、字节跳动在半年内面试常考）
      括号生成 (字节跳动在半年内面试中考过)
      翻转二叉树 (谷歌、字节跳动、Facebook 在半年内面试中考过)
      验证二叉搜索树（亚马逊、微软、Facebook 在半年内面试中考过）
      二叉树的最大深度（亚马逊、微软、字节跳动在半年内面试中考过）
      二叉树的最小深度（Facebook、字节跳动、谷歌在半年内面试中考过）
      二叉树的序列化与反序列化（Facebook、亚马逊在半年内面试常考）
      课后作业
      二叉树的最近公共祖先（Facebook 在半年内面试常考）
      从前序与中序遍历序列构造二叉树（字节跳动、亚马逊、微软在半年内面试中考过）
      组合（微软、亚马逊、谷歌在半年内面试中考过）
      全排列（字节跳动在半年内面试常考）
      全排列 II （亚马逊、字节跳动、Facebook 在半年内面试中考过）

### 第8课.分治、回溯：
1. 分治、回溯的实现和特性:
   * 重复性：
      最近重复性--分治、回溯；
      最优重复性--动态规划；
   * 分治：分成子问题->分别处理—>问题合并  
      当层只做当层的事情，不插足下一层的事情

            def divide_conquer(problem, param1, param2, ...): 
            # recursion terminator 
            if problem is None: 
               print_result 
               return 

            # prepare data 
            data = prepare_data(problem) 
            subproblems = split_problem(problem, data) 

            # conquer subproblems 
            subresult1 = self.divide_conquer(subproblems[0], p1, ...) 
            subresult2 = self.divide_conquer(subproblems[1], p1, ...) 
            subresult3 = self.divide_conquer(subproblems[2], p1, ...) 
            …

            # process and generate the final result 
            result = process_result(subresult1, subresult2, subresult3, …)
               
            # revert the current level states
   * 回溯：  回到之前<-不成功<-尝试->成功->继续
2. 实战题目解析：Pow(x,n)、子集:
   * 实战题目
   Pow(x, n) （Facebook 在半年内面试常考）
   子集（Facebook、字节跳动、亚马逊在半年内面试中考过）
   >参考链接
   牛顿迭代法原理: http://www.matrix67.com/blog/archives/361
   牛顿迭代法代码: http://www.voidcn.com/article/p-eudisdmk-zm.html
3. 实战题目解析：电话号码的字母组合、N皇后:
         实战题目
      多数元素 （亚马逊、字节跳动、Facebook 在半年内面试中考过）:https://leetcode-cn.com/problems/majority-element/description/
      电话号码的字母组合（亚马逊在半年内面试常考）:https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number/
      N 皇后（字节跳动、苹果、谷歌在半年内面试中考过）:https://leetcode-cn.com/problems/n-queens/


#### **漂亮代码收集：**
   *  >297. 二叉树的序列化与反序列化序列化是将一个数据结构或者对象转换为连续的比特位的操作，进而可以将转换后的数据存储在一个文件或者内存中，同时也可以通过网络传输到另一个计算机环境，采取相反方式重构得到原数据。请设计一个算法来实现二叉树的序列化与反序列化。这里不限定你的序列 / 反序列化算法执行逻辑，你只需要保证一个二叉树可以被序列化为一个字符串并且将这个字符串反序列化为原始的树结构。(https://leetcode-cn.com/problems/serialize-and-deserialize-binary-tree/)

               # Definition for a binary tree node.
               # class TreeNode(object):
               #     def __init__(self, x):
               #         self.val = x
               #         self.left = None
               #         self.right = None

               class Codec:

                  def serialize(self, root):
                     """Encodes a tree to a single string.
                     
                     :type root: TreeNode
                     :rtype: str
                     """
                     def doit(node):
                           if node:
                              vals.append(str(node.val))
                              doit(node.left)
                              doit(node.right)
                           else:
                              vals.append('#')
                     
                     vals = []
                     doit(root)
                     return ' '.join(vals)

                  def deserialize(self, data):
                     """Decodes your encoded data to tree.
                     
                     :type data: str
                     :rtype: TreeNode
                     """
                     def doit():
                           val = next(vals)  ##使用了迭代器，漂亮！！
                           if val == '#':
                              return None
                           node = TreeNode(int(val))
                           node.left = doit()
                           node.right = doit()
                           return node
                     
                     vals = iter(data.split())
                     return doit()
                     

               # Your Codec object will be instantiated and called as such:
               # ser = Codec()
               # deser = Codec()
               # ans = deser.deserialize(ser.serialize(root))
   *  >236. 二叉树的最近公共祖先
      给定一个二叉树, 找到该树中两个指定节点的最近公共祖先.百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”例如，给定如下二叉树:  root = [3,5,1,6,2,0,8,null,null,7,4]::https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree/
      
               # Definition for a binary tree node.
               # class TreeNode:
               #     def __init__(self, x):
               #         self.val = x
               #         self.left = None
               #         self.right = None

               class Solution:
                  def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
                     if root in (None, p, q):
                           return root
                     left , right = (self.lowestCommonAncestor(kid, p, q)
                                       for kid in (root.left, root.right))
                     return root if left and right else left or right
   * >77. 组合,给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。

            class Solution:
               def combine(self, n: int, k: int) -> List[List[int]]:
                  res = []
                  self.dfs([i for i in range(1, n+1)], k, [], res)
                  return res
               
               def dfs(self, nums, k, path, res):
                  if len(path) == k:
                        res.append(path)
                        return
                  
                  # 组合：
                  for i in range(len(nums)):
                        dfs(nums[i+1:], k, path+[nums[i]], res)  ## dfs-深度优先，也就是递归
                        ## 技术要点是`path+[nums[i]]`和`nums[i+1:]`
                  
                  ## 全排列：
                  for i in range(len(nums)):
                     if nums[i] not in path:
                        self.dfs(nums, n, path+[nums[i]], res)
   * 78. 子集给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。说明：解集不能包含重复的子集。
   可用：递归、组合的思路、迭代

            class Solution:
               def subsets(self, nums: list) -> list:
                  res = []
                  self.dfs(nums, [], 0, res)
                  return res
               
               def dfs(self, nums, path, index, res):
                  if index == len(nums):
                        res.append(path)
                        return
                  
                  self.dfs(nums, path.copy(), index+1, res)
                  
                  path.append(nums[index])
                  
                  self.dfs(nums, path.copy(), index+1, res)
                  
            s = Solution()
            print(s.subsets([1,2,3]))
      >##### 可以理解为三个格子，分别各自放1，2，3还是空格的组合
      >##### path.copy():表示只传path的各自复制引用，否则path的所有改变最终都只res.append(path)中显现。
   * 51.  n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击上图为 8 皇后问题的一种解法。给定一个整数 n，返回所有不同的 n 皇后问题的解决方案。每一种解法包含一个明确的 n 皇后问题的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。链接：https://leetcode-cn.com/problems/n-queens

               class Solution:
                  def solveNQueens(self, n: int) -> List[List[str]]:
                     def DFS(queens: list, pie: list, na: list):
                           '''
                           queens: 各行queens所在的位置组成的数列；
                           pie: 撇，存放左斜位置的数列；
                           na: 捺， 存放右斜位置的数列。
                           '''
                           
                           # 当前行数：
                           row = len(queens)
                           if row == n:
                              results.append(queens)
                              return None
                           for col in range(n):
                              if col not in queens and row+col not in pie and row-col not in na:
                                 DFS(queens+[col], pie+[row+col], na+[row-col])
                     
                     results = []
                     DFS([], [], [])
                     return [[f'{"."*i}Q{"."*(n-i-1)}' for i in res] for res in results]

#### **Python语法注意：**
* list中的append() VS. extend():
      append():添加成员；
      extend():两数列合并。
* 数列的下标：


            a = [1]
            a[:0] -> []
            a[1:] -> []
            a[1] -> Exception
            a[2:] -> []
#### **对代码对一些理解：**
* 递归里对全排列：

            class Solution:
               def _generate(self, level, max, s):
                  if level >= max:
                        print(s)
                        return None
                  self._generate(level+1, max, s + '(') # （1）
                  self._generate(level+1, max, s + ')') # （2）

               def generateParenthesis(self, n: int):
                  self._generate(0, n, '')
                  
            s = Solution()
            s.generateParenthesis(2)
   >理解：self._generate(0, n, '')中的n可理解为n个格子，每个格子存放'('或')',共有多少种放法。
   >(1)(2)两行代码共计算2^n次。