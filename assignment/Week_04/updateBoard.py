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