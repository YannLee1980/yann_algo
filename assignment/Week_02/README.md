# 算法训练营
---
## 第2周：
### **本周内容一览：**
### 第5课.哈希表、映射、集合：
1. 哈希表、映射、集合的特性：
   * O(1)
   * 参考链接
  >Java Set 文档: https://docs.oracle.com/en/java/javase/12/docs/api/java.base/java/util/Set.html
  >Java Map 文档: https://docs.oracle.com/en/java/javase/12/docs/api/java.base/java/util/Map.html
2. 实战题目解析：有效的字母异位词等问题:
   * 排序的时间复杂度：O(NlogN)
   * collections.defaultdict(list)的使用--value为list
   * 实战题目 / 课后作业
    >有效的字母异位词（亚马逊、Facebook、谷歌在半年内面试中考过）
    >字母异位词分组（亚马逊在半年内面试中常考）
    >两数之和（亚马逊、字节跳动、谷歌、Facebook、苹果、微软、腾讯在半年内面试中常考）
    >参考链接
    >养成收藏精选代码的习惯（示例）:http://shimo.im/docs/R6g9WJV89QkHrDhr

### 第6课 树、二叉树、二叉搜索树的实现和特性：
1. 树、二叉树、二叉搜索树的实现和特性：
  * 二叉搜索树：左节点<根节点<右节点
  * 参考链接
  >二叉搜索树 Demo ： https://visualgo.net/zh/bst
  * 思考题
  >树的面试题解法一般都是递归，为什么？
  >说明：递归可简化代码的维护，并且处理得当并不会消耗比非递归方法太大的复杂度。

2. 实战题目解析：二叉树的中序遍历
   * 合理的使用递归其实效率并不会低下
   *  Linked List 是特殊化的 Tree Tree 是特殊化的Graph

          class TreeNode:
            def __init__(self, val=0, left=None, right=None):
              self.val = val
              self.left = left
              self.right = right
   * 1.前序(Pre-order):根-左-右 

          def preorder(self, root):
            if root:
              self.traverse_path.append(root.val)
              self.preorder(root.left)
              self.preorder(root.right)
   * 2.中序(In-order):左-根-右 

          def inorder(self, root):
            if root:
              self.inorder(root.left)
              self.traverse_path.append(root.val)
              self.inorder(root.right)
   * 3.后序(Post-order):左-右-根

          def postorder(self, root):
            if root:
              self.postorder(root.left)
              self.postorder(root.right)
              self.traverse_path.append(root.val)
   * 参考链接
      树的遍历 Demo
      实战题目 / 课后作业
      二叉树的中序遍历（亚马逊、微软、字节跳动在半年内面试中考过）
      二叉树的前序遍历（谷歌、微软、字节跳动在半年内面试中考过）
      N 叉树的后序遍历（亚马逊在半年内面试中考过）
      N 叉树的前序遍历（亚马逊在半年内面试中考过）
      N 叉树的层序遍历
3. 堆和二叉堆:
    * 二叉堆是由完全二叉树建成的，并通过数组来进行存储的，二叉堆堆效率在堆里是最低的。
    * priority_queue(优先队列)本质就是堆:
      `Python: queue.PriorityQueue、 asyncio.PriorityQueue`（底层是headpq）、 `heapq`
4. 实战题目解析：最小的k个数、滑动窗口最大值等问题：
  * 实战例题
    >最小的 k 个数（字节跳动在半年内面试中考过）
    >滑动窗口最大值（亚马逊在半年内面试中常考）
    >课后作业
    >HeapSort ：自学 https://www.geeksforgeeks.org/heap-sort/
    >丑数（字节跳动在半年内面试中考过）
    >前 K 个高频元素（亚马逊在半年内面试中常考）

5. 图的实现和特性:
   * 广度优先：

          # 代码模版：（用队列）
          def bfs(grid, start):
            queue = []
            visited = set()  ## 注意：要用集合，用了列表会重复遍历
            queue.append(start)
            visited.add(start)
            while queue:
              node = queue.pop(0)
              process(node)
              nodes = generate_related_nodes(node)
              for node in nodes:
                if node not in visited:
                  queue.append(node)
                  visited.add(node)

          # 优化(分层显示)-例子：
          # Definition for a Node.
          class Node:
              def __init__(self, val=None, children=None):
                  self.val = val
                  self.children = children
          """
          import collections
          class Solution:
              def levelOrder(self, root: 'Node') -> List[List[int]]:
                  if root is None:
                      return []
                  
                  result = []
                  deque = collections.deque([root])

                  while deque:
                      level = []
                      for _ in range(len(deque)):
                          node = deque.popleft()
                          level.append(node.val)
                          deque.extend(node.children)
                      result.append(level)

                  return result



   * 深度优先：

          # 代码模版：（用栈）
          def dfs(grid, start):
            stack = []
            visited = set()  ## 注意：要用集合，用了列表会重复遍历
            stack.append(start)
            visited.add(start)
            while stack:
              node = stack.pop()
              process(node)
              nodes = generate_related_nodes(node)
              for node in nodes:
                if node not in visited:
                  stack.append(node)
                  visited.add(node)
                
            # 代码模版：（递归）
            visited = set()
            def dfs(node, visited):
              if node in visited:
                return
              visited.add(node)
              for next_node in node.children():
                dfs(next_node, visited)
   * python heaqp（堆）的使用：小顶堆，可以用l = [], 初始化：`heap = []  heappush(heap, 1)`
   * 参考链接
      >连通图个数： https://leetcode-cn.com/problems/number-of-islands/
      >拓扑排序（Topological Sorting）： https://zhuanlan.zhihu.com/p/34871092
      >最短路径（Shortest Path）：Dijkstra https://www.bilibili.com/video/av25829980?from=search&seid=13391343514095937158
      >最小生成树（Minimum Spanning Tree）： https://www.bilibili.com/video/av84820276?from=search&seid=17476598104352152051