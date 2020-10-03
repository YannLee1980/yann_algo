# 算法训练营
---
## 第4周：
### **本周内容一览：**
### 第9课 深度优先和广度优先搜索：
1. 深度优先搜索、广度优先搜索的实现和特性：
   * 对于节点的访问顺序不限
     - 深度优先:depth first search
     - 广度优先:breadth first search
     - 优先级优先： 启发式搜索（估价函数）
   * DFS代码模版：

            # 递归写法v1.0:
            visited = set()
            def dfs(node, visited):
               if node in visited: # terminator
                  # node already visited
                  return
               visited.add(node)
               # process current node here
               ...
               for next_node in node.children:
                  if next_node not in visited:
                     dfs(next_node, visited)

            # 递归写法v2.0:
            visted = set()
            def dfs(node, visited):
               visited.add(node)
               # process current node here
               for next_node in node.children:
                  if next_node not in visited:
                     dfs(next_node, visited)
                  
            # 非递归写法：
            def DFS(self, tree):
               if tree is None:
                  return None
               visited, stack = [], [tree.root]
               while stack:
                  node = stack.pop()
                  visited.add(node)
                  process(node)
                  nodes = generate_related_nodes(node)
                  stack.push(nodes)
               # orther processing work
               
   * BFS代码模版：

            def BFS(graph, start, end):
               queue = []
               visited = set()
               queue.push([start])
               while queue:
                  node = queue.pop()
                  visited.add(node)
                  process(node)
                  nodes = generate_related_nodes(node)
                  queue.push(nodes)
               # orther processing work
   * 参考资料：
      实战题目
      二叉树的层序遍历（字节跳动、亚马逊、微软在半年内面试中考过）
      最小基因变化 # 
      括号生成（字节跳动、亚马逊、Facebook 在半年内面试中考过）
      在每个树行中找最大值（微软、亚马逊、Facebook 在半年内面试中考过）
      课后作业
      单词接龙（亚马逊在半年内面试常考）# **未完成**
      单词接龙 II （微软、亚马逊、Facebook 在半年内面试中考过）# **未完成**
      岛屿数量（近半年内，亚马逊在面试中考查此题达到 350 次）
      扫雷游戏（亚马逊、Facebook 在半年内面试中考过）# 未完成 **未完成**
### 第10课 贪心算法 ：
1.贪心的实现、特性及实战题目解析：
   * 贪心算法 VS.回溯 VS.动态规划：
     贪心算法：当下局部最优，不可回退；
     回溯：可回退；
     动态规划：最优判断+回退（保存当前的结果）
   * 贪心算法的使用场景：
     简单地说，问题能够分解成子问题来解决，子问题的最优解能递推到最终 问题的最优解。这种子问题最优解称为最优子结构。
### 第11课 二分查找：
* 二分查找的实现、特性及实战题目解析：
   * 二分查找的前提：
    1. 目标函数单调性(单调递增或者递减) 
    2. 存在上下界(bounded)
    3. 能够通过索引访问(index accessible)
   * 代码模版：

         left , right = 0 , len(arr) - 1
         while left <= right:
            mid = (left + right) / 2
            if arr[mid] == target:
               # find the target!!
               break or return
            elif arr[mid] < target:
               left = mid + 1
            else:
               right = mid - 1
  
> 参考链接
二分查找代码模板
Fast InvSqrt() 扩展阅读
实战题目
x 的平方根（字节跳动、微软、亚马逊在半年内面试中考过）
有效的完全平方数（亚马逊在半年内面试中考过）
课后作业
搜索旋转排序数组（Facebook、字节跳动、亚马逊在半年内面试常考）
搜索二维矩阵（亚马逊、微软、Facebook 在半年内面试中考过）
寻找旋转排序数组中的最小值（亚马逊、微软、字节跳动在半年内面试中考过）
使用二分查找，寻找一个半有序数组 [4, 5, 6, 7, 0, 1, 2] 中间无序的地方
说明：同学们可以将自己的思路、代码写在学习总结中
参考链接
牛顿迭代法原理： http://www.matrix67.com/blog/archives/361
牛顿迭代法代码： http://www.voidcn.com/article/p-eudisdmk-zm.html

#### **漂亮代码收集：**
* 55. 跳跃游戏
   给定一个非负整数数组，你最初位于数组的第一个位置。数组中的每个元素代表你在该位置可以跳跃的最大长度。判断你是否能够到达最后一个位置。示例 1:
   输入: [2,3,1,1,4]
   输出: true
   解释: 我们可以先跳 1 步，从位置 0 到达 位置 1, 然后再从位置 1 跳 3 步到达最后一个位置。

            # 使用贪心算法：
            class Solution:
               def canJump(self, nums: List[int]) -> bool:
                  if not nums:
                        return False
                  reachable_end = len(nums) - 1
                  for i in range(len(nums)-1, -1, -1):
                        if nums[i] + i >= reachable_end:
                           reachable_end = i
                  if reachable_end == 0:
                        return True
                  else:
                        return False
 * 127. 单词接龙给定两个单词（beginWord 和 endWord）和一个字典，找到从 beginWord 到 endWord 的最短转换序列的长度。转换需遵循如下规则：每次转换只能改变一个字母。转换过程中的中间单词必须是字典中的单词。

            # BFS:
            from collections import defaultdict
            class Solution:
               def ladderLength(self, beginWord: str, endWord: str, wordList: list) -> int:
                  if endWord not in wordList or not beginWord or not wordList:
                        return 0
                  
                  L = len(beginWord)
                  all_combo_dict = defaultdict(list)

                  for word in wordList:
                        for i in range(L):
                           all_combo_dict[word[:i]+'*'+word[i+1:]].append(word)

                  queue = [(beginWord, 1)]
                  visited = set()
                  visited.add(beginWord)

                  while queue:
                        current_word , level = queue.pop(0)
                        for i in range(L):
                           intermediate_word = current_word[:i]+'*'+current_word[i+1:]
                           for word in all_combo_dict[intermediate_word]:
                              if word == endWord:
                                    return level + 1
                              if word not in visited:
                                    visited.add(word)
                                    queue.append((word, level+1))
                           all_combo_dict[intermediate_word] = []

                  return 0
#### **Python语法注意：**

#### **对代码对一些理解：**

