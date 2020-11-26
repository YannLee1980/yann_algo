# 212. 单词搜索 II
# https://leetcode-cn.com/problems/word-search-ii/

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def dfs(board, i, j, cur_word, cur_dict):
            cur_word += board[i][j]
            cur_dict = cur_dict[board[i][j]]
            if END_OF_WORD in cur_dict:
                res.add(cur_word)
            tmp, board[i][j] = board[i][j], '@'
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                x, y = dx + i, dy + j
                if 0<=x<m and 0<=y<n and board[x][y] != '@' and board[x][y] in cur_dict:
                    dfs(board, x, y, cur_word, cur_dict)
            board[i][j] = tmp
            
        
        if not board or not words: return []
        END_OF_WORD = '#'
        m, n, res, root = len(board), len(board[0]), set(), {}
        
        for word in words:
            node = root
            for char in word:
                node = node.setdefault(char, {})
            node[END_OF_WORD] = True
            
        for i in range(m):
            for j in range(n):
                if board[i][j] in root:
                    dfs(board, i, j, '', root)
                    
        return list(res)