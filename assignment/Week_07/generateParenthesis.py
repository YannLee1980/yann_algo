# 22. 括号生成
# https://leetcode-cn.com/problems/generate-parentheses/

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def dfs(left, right, path):
            if len(path) == 2 * n:
                res.append(path)
                return None
            if left < n:
                dfs(left + 1, right, path + '(')
            if right < left:
                dfs(left, right + 1, path + ')')
        
        res = []
        dfs(0, 0, '')
        return res