# 算法训练营
---
## 第4周：
---
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
         while left <= right:    ####注意<=
            mid = (left + right) / 2
            if arr[mid] == target:
               # find the target!!
               break or return
            elif arr[mid] < target:
               left = mid + 1
            else:
               right = mid - 1
     **注意<=**
  
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

 * 45. 跳跃游戏 II 给定一个非负整数数组，你最初位于数组的第一个位置。数组中的每个元素代表你在该位置可以跳跃的最大长度。你的目标是使用最少的跳跃次数到达数组的最后一个位置。

            class Solution:
               def jump(self, nums: List[int]) -> int:
                  maxPos, step, end = 0, 0, 0
                  for i in range(len(nums)-1): # 注意:len(nums)-1
                        if maxPos >= i:
                           maxPos = max(nums[i]+i, maxPos)
                           if i == end:
                              step += 1
                              end = maxPos
                  return step
   **注意:len(nums)-1**
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

 * 126. 单词接龙 II https://leetcode-cn.com/problems/word-ladder-ii/ ;给定两个单词（beginWord 和 endWord）和一个字典 wordList，找出所有从 beginWord 到 endWord 的最短转换序列。转换需遵循如下规则：每次转换只能改变一个字母.转换后得到的单词必须是字典中的单词。说明:如果不存在这样的转换序列，返回一个空列表。所有单词具有相同的长度。所有单词只由小写字母组成。字典中不存在重复的单词。你可以假设 beginWord 和 endWord 是非空的，且二者不相同。

            class Solution:
               def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
                  
                  if endWord not in  wordList or not beginWord or not wordList:
                        return []
                  
                  wordList = set(wordList)
                  res = []
                  layer = {}
                  layer[beginWord] = [[beginWord]]
                  
                  while layer:
                        newlayer = collections.defaultdict(list)
                        for w in layer:
                           if w == endWord:
                              res.extend(k for k in layer[w])
                           else:
                              for i in range(len(w)):
                                    for c in 'abcdefghijklmnopqrstuvwxyz':
                                       neww = w[:i] + c + w[i+1:]
                                       if neww in wordList:
                                          newlayer[neww] += [j + [neww] for j in layer[w]]
                        wordList -= set(newlayer.keys())
                        layer = newlayer
                        
                  return res

 * 529. 扫雷游戏 https://leetcode-cn.com/problems/minesweeper/ 让我们一起来玩扫雷游戏！

            # 529. 扫雷游戏
            # https://leetcode-cn.com/problems/minesweeper/
            # 让我们一起来玩扫雷游戏！

            # 给定一个代表游戏板的二维字符矩阵。 'M' 代表一个未挖出的地雷，'E' 代表一个未挖出的空方块，'B' 代表没有相邻（上，下，左，右，和所有4个对角线）地雷的已挖出的空白方块，数字（'1' 到 '8'）表示有多少地雷与这块已挖出的方块相邻，'X' 则表示一个已挖出的地雷。

            # 现在给出在所有未挖出的方块中（'M'或者'E'）的下一个点击位置（行和列索引），根据以下规则，返回相应位置被点击后对应的面板：

            # 如果一个地雷（'M'）被挖出，游戏就结束了- 把它改为 'X'。
            # 如果一个没有相邻地雷的空方块（'E'）被挖出，修改它为（'B'），并且所有和其相邻的未挖出方块都应该被递归地揭露。
            # 如果一个至少与一个地雷相邻的空方块（'E'）被挖出，修改它为数字（'1'到'8'），表示相邻地雷的数量。
            # 如果在此次点击中，若无更多方块可被揭露，则返回面板。

            class Solution:
               def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
                  if not board:
                        return []
                  
                  i, j = click[0], click[1]
                  
                  if board[i][j] == 'M':
                        board[i][j] = 'X'
                        return board
                  
                  self.dfs(board, i, j)
                  
                  return board
               
               def dfs(self, board, i, j):
                  if board[i][j] != 'E':
                        return None
                  
                  rows, cols = len(board), len(board[0])
                  directions = [(0,-1), (-1,-1), (-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1)]
                  mine_count = 0
                  
                  for d in directions:
                        ni, nj = i + d[0], j + d[1]
                        if 0 <= ni < rows and 0 <= nj < cols and board[ni][nj] == 'M':
                           mine_count += 1
                           
                  if mine_count == 0:
                        board[i][j] = 'B'
                        
                  else:
                        board[i][j] = str(mine_count)
                        return None
                  
                  for d in directions:
                        ni, nj = i + d[0], j + d[1]
                        if 0 <= ni < rows and 0 <= nj < cols:
                           self.dfs(board, ni, nj)
#### **Python语法注意：**
* for _ in range(len(queue)) 与 for _ in queue 的区别：
  （1）len(queue)是定值， for的循环次数固定； 
  （2）for _ in queue：循环次数随着queue的变化而变化。
#### **对代码对一些理解：**
* 牛顿法求C的算术平方根：
  $$x_{i+1}=\frac12(x_i+\frac{C}{x_i})$$
  x的初始值：一般取C

* 以下两个写法的区别：

            # 如果left、right很大时会溢出：
            mid = (left + right) // 2

            # 防止left、right很大时溢出：
            mid = left + (right - left) // 2

#### **需要理解的地方：**
* 二分查找中的left < right ，何时有=，何时没有=。
* 127、126单词接龙需要进一步理解:
   注意：1.return level是否加1；
      2.去掉visited；
      3.用queue与dict的区别。