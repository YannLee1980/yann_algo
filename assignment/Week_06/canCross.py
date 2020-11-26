# 403. 青蛙过河
# https://leetcode-cn.com/problems/frog-jump/
# 一只青蛙想要过河。 假定河流被等分为 x 个单元格，并且在每一个单元格内都有可能放有一石子（也有可能没有）。 青蛙可以跳上石头，但是不可以跳入水中。

# 给定石子的位置列表（用单元格序号升序表示）， 请判定青蛙能否成功过河（即能否在最后一步跳至最后一个石子上）。 开始时， 青蛙默认已站在第一个石子上，并可以假定它第一步只能跳跃一个单位（即只能从单元格1跳至单元格2）。

# 如果青蛙上一步跳跃了 k 个单位，那么它接下来的跳跃距离只能选择为 k - 1、k 或 k + 1个单位。 另请注意，青蛙只能向前方（终点的方向）跳跃。


class Solution:
    def canCross(self, stones: List[int]) -> bool:
        dp_dict = {} # 记录当前位置是从上一位置跳了多少过来，有多种情况。
        
        for stone in stones:
            dp_dict[stone] = set()
            
        dp_dict[stones[0]].add(0)
        
        for stone in stones:
            for k in dp_dict[stone]:
                for step in [k-1, k, k+1]:
                    if step > 0 and step+stone in dp_dict:
                        dp_dict[step+stone].add(step)
                        
        return len(dp_dict[stones[-1]]) > 0