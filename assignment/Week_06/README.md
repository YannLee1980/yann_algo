# 算法训练营
---
## 第6周：
---
### **本周内容一览：**
### 第12课 动态规划：
1. 动态规划的实现及关键点：
   * 改变习惯：
      1. 人肉递归低效、很累
      2. 找到最近最简方法，将其拆解成可重复解决的问题 
      3. 数学归纳法思维(抵制人肉递归的诱惑)
   * 动态规划（Dynamic Programming）----直译：动态递推编程
      1.Wiki 定义: https://en.wikipedia.org/wiki/Dynamic_programming
      2.“Simplifying a complicated problem by breaking it down into simpler sub-problems”(in a recursive manner)
      3.Divide & Conquer + Optimal substructure 分治 + 最优子结构
   * 关键点：
      动态规划 和 递归或者分治 没有根本上的区别(关键看有无最优的子结构)
      共性:找到重复子问题 差异性:最优子结构、中途可以淘汰次优解
2. DP例题解析：Fibonacci数列、路径计数:
   * Fibonacci数列：

            # 递归：
            def fib(n):
               reutrn n if n <= 1 else fib(n-1)+fib(n-2)

            # 记忆化搜索：（自顶向下）
            def fib(n, mome):
               if n <= 1:
                  return n
               if mome[n] == 0:
                  mome[n] = fib(n-1) + fib(n-2)
               return mome[n]

            # 动态递推（自底向上）：----最好习惯于这种
            def fib(n):
               a = [0] * (n+1)
               a[0], a[1] = 0, 1
               for i in range(len(a)):
                  a[i] = a[i-1] + a[i-2]
               return a[n]
      最好习惯于：**动态递推（自底向上）----动态规划**
   * 动态规划关键点：
      1. 最优子结构：`opt[n] = best_of(opt[n-1],opt[n-2],...)`
      2. 存储中间状态：`opt[i]`
      3. 递归方程(状态转移方程、动态规划方程、DP方程）
         如：`Fib: opt[n] = opt[n-1] + opt[n-2]`
            `二维路径：opt[i,j] = opt[i,j+1] + opt[i+1,j]( 且判断a[i,j]是否为空地)`

            # 完整逻辑：
            if opt[i,j] == '空地':
               opt[i,j] = opt[i,j+1] + opt[i+1,j]
            else:
               opt[i,j] = 0
3. DP例题解析：最长公共子序列：
   * 五步解决DP问题：
      1. 定义子问题；
      2. 猜想递归方程；
      3. 解决最近子问题；
      4. 记忆递归或自底向上的递推；
      5. 解决总体问题。
   * 优化3步：
      1. 找最近重复性（即最近子问题）；
      2. 定义状态数组；
      3. DP方程。
4. 实战题目解析：三角形最小路径和:
   * 爬楼梯的变形：
      1. 每步可以走1、2、3级；
      2. 相邻的两步的步伐不一样。
   * 120. 三角形最小路径和给定一个三角形，找出自顶向下的最小路径和。每一步只能移动到下一行中相邻的结点上。相邻的结点 在这里指的是 下标 与 上一层结点下标 相同或者等于 上一层结点下标 + 1 的两个结点。
      分析：
      * 最近子问题：problem[i,j] = min(sub[i+1, j] , sub[i+1, j+1]) + a[i,j]
      * 状态数组：自底向上记录最小路径：f[i,j]
      * DP方程：自底向上：f[i,j] = min(f[i+1,j], f[i+1, j+1]) + a[i,j]


5. 实战题目解析：最大子序列和
   * 最大子序和,给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
   示例:
   输入: [-2,1,-3,4,-1,2,1,-5,4]
   输出: 6
   解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
   分析：
     * 暴力：2^n;
     * DP:
      a. 子问题：max_sum(i) = max(a(i), max_sum(i-1)+a(i))
      b. 存储状态定义：f(i):记录包括第i个元素后第最大子序列和 -> 所以题目的最终值是max(f)
      c. DP方程：f(i) = max(a(i), f(i-1)+a(i))

   * 322. 零钱兑换----给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1。你可以认为每种硬币的数量是无限的。
   DP方程：f(n) = min(f(n - k) for k in [1, 2, 5]) + 1 或 f(n) = min(f(n - k)+1 for k in [1, 2, 5])

6. 实战题目解析：打家劫舍:
* 198. 打家劫舍--你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。给定一个代表每个房屋存放金额的非负整数数组，计算你 不触动警报装置的情况下 ，一夜之内能够偷窃到的最高金额。
  存储状态：a[i][0,1]:到第i个房子偷盗的最大金额数,该房被偷：a[i][1]，该房没被偷:a[i][0]；初始值：a[0][0]=0, a[0][1]=nums[0]
  DP方程：

            # DP+2维数组：
            a[i][0] = max(a[i-1][0], a[i-1][1])
            a[i][1] = a[i-1][0] + nums[i]

            # DP + 1维数组：
            # a[i] 存储到第i个房子第最大偷取金钱，并不管它有没有被偷。
            a[i] = max(a[i-1], a[i-2]+nums[i])
            # 初始值：
            a[0] = 0
            a[1] = max(nums[0], nums[1])

            # DP + 2数值：
            pre = 0
            now = 0
            now, pre = max(now, pre+nums[i]), now
* 213. 打家劫舍 II----你是一个专业的小偷，计划偷窃沿街的房屋，每间房内都藏有一定的现金。这个地方所有的房屋都围成一圈，这意味着第一个房屋和最后一个房屋是紧挨着的。同时，相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。给定一个代表每个房屋存放金额的非负整数数组，计算你在不触动警报装置的情况下，能够偷窃到的最高金额。
  **转化成上一问题：把nums分成nums[1:]和nums[:-1]并分别用上面第方法解决，然后取两个结果的最大值。**
#### **漂亮代码收集：**

#### **Python语法注意：**
   * 嵌套列表的创建一定要用推导式：

            # 错误写法：
            a = [[0]*2] * 3

            # 正确写法：
            a = [[0]*2 for _ in range(3)]

            # 验证：
            a[0][0] = 9
            b[0][0] = 9
            #  a： [[9, 0], [0, 0], [0, 0]], 
            #  b:  [[9, 0], [9, 0], [9, 0]]

            # 一维的时候，可以：
            a = [0] * 10
   * lru_cache的使用：

# DFS + 记忆 + LRU_cache
      from functools import lru_cache
      class Solution:
         def minimumTotal(self, triangle: List[List[int]]) -> int:
            @lru_cache(maxsize=None)
            def dfs(i, j):
                  if i == len(triangle) - 1:
                     return triangle[i][j]
                  left = dfs(i+1, j)
                  right = dfs(i+1, j+1)
                  return min(left, right) + triangle[i][j]
            
            return dfs(0, 0)
#### **对代码对一些理解：**
* 123. 买卖股票的最佳时机 III----给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。设计一个算法来计算你所能获取的最大利润。你最多可以完成 两笔 交易。注意: 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

            # DP + 二维数组存储状态
            class Solution:
               def maxProfit(self, prices: List[int]) -> int:
                  n = len(prices)
                  if n < 2: return 0
                  dp = [[0] * 5 for _ in range(n)] # 记录每天五种状态下的最大获利
                  dp[0][0] = 0 # 不操作
                  dp[0][1] = -prices[0] # 第一次买入
                  dp[0][2] = 0 # 第一次卖出
                  dp[0][3] = -prices[0] # 第二次买入
                  dp[0][4] = 0 # 第二次卖出
                  for i in range(1, n):
                        dp[i][0] = dp[i-1][0] # 不操作
                        dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i]) 
                        dp[i][2] = max(dp[i-1][2], dp[i-1][1] + prices[i])
                        dp[i][3] = max(dp[i-1][3], dp[i-1][2] - prices[i])
                        dp[i][4] = max(dp[i-1][4], dp[i-1][3] + prices[i])
                        
                  # 最大值只发生在不持股的时候，因此来源有 3 个：j = 0 ,j = 2, j = 4
                  return max(dp[-1][0], dp[-1][2], dp[-1][4])
   **注意：各状态的存储**

            # DP + 一维数组存储状态
            class Solution:
               def maxProfit(self, prices: List[int]) -> int:
                  n = len(prices)
                  if n < 2: return 0
                  dp = [0] * 5 # 记录当天五种状态下的最大获利
                  # 初始化：
                  dp[0] = 0 # 不操作
                  dp[1] = -prices[0] # 第一次买入
                  dp[2] = 0 # 第一次卖出
                  dp[3] = -prices[0] # 第二次买入
                  dp[4] = 0 # 第二次卖出
                  
                  for i in range(1, n):
                        dp[0] = 0 # 不操作
                        dp[1] = max(dp[1], dp[0] - prices[i]) 
                        dp[2] = max(dp[2], dp[1] + prices[i])
                        dp[3] = max(dp[3], dp[2] - prices[i])
                        dp[4] = max(dp[4], dp[3] + prices[i])
                        
                  # 最大值只发生在不持股的时候，因此来源有 3 个：j = 0 ,j = 2, j = 4
                  return max(dp)

#### **需要理解的地方：**

