# 874. 模拟行走机器人
# https://leetcode-cn.com/problems/walking-robot-simulation/

# 机器人在一个无限大小的网格上行走，从点 (0, 0) 处开始出发，面向北方。该机器人可以接收以下三种类型的命令：

# -2：向左转 90 度
# -1：向右转 90 度
# 1 <= x <= 9：向前移动 x 个单位长度
# 在网格上有一些格子被视为障碍物。

# 第 i 个障碍物位于网格点  (obstacles[i][0], obstacles[i][1])

# 机器人无法走到障碍物上，它将会停留在障碍物的前一个网格方块上，但仍然可以继续该路线的其余部分。

# 返回从原点到机器人所有经过的路径点（坐标为整数）的最大欧式距离的平方

class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        i = j = mx = d = 0
        move = ((0, 1), (-1, 0), (0, -1), (1, 0))
        obstacles = set(map(tuple, obstacles))
        
        for command in commands:
            if command == -1: d = (d - 1) % 4
            elif command == -2: d = (d + 1) % 4
            else:
                x, y = move[d]
                while command and (i+x, j+y) not in obstacles:
                    i += x
                    j += y
                    command -= 1
            mx = max(mx, i**2+j**2)
        
        return mx