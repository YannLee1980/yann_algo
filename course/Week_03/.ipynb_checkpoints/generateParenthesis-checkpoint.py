# 22. 括号生成
# https://leetcode-cn.com/problems/generate-parentheses/

# 数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。

# 示例：

# 输入：n = 3
# 输出：[
#        "((()))",
#        "(()())",
#        "(())()",
#        "()(())",
#        "()()()"
#      ]

class Solution:
    result = []
    def _generate(self, left, right, n, s):
        # recursion terminator:
        if  left == n and right == n:
            self.result.append(s)
            return None

        # process logic in current level:
        # s1 = s + '('
        # s2 = s + ')'

        # drill down to next level:
        # 判断括号逻辑合理才能加入：
        if left < n: # 左括号数不能超过n
            self._generate(left + 1, right, n, s + '(')
        if right < left: # 右括号数小于左括号时就可以加入
            self._generate(left, right + 1, n, s + ')')

        # reverse the current level status if needed

    def generateParenthesis(self, n: int):
        self._generate(0, 0, n, '')
        return self.result

s = Solution()
print(s.generateParenthesis(1))