# 455. 分发饼干
# https://leetcode-cn.com/problems/assign-cookies/
# 假设你是一位很棒的家长，想要给你的孩子们一些小饼干。但是，每个孩子最多只能给一块饼干。对每个孩子 i ，都有一个胃口值 gi ，这是能让孩子们满足胃口的饼干的最小尺寸；并且每块饼干 j ，都有一个尺寸 sj 。如果 sj >= gi ，我们可以将这个饼干 j 分配给孩子 i ，这个孩子会得到满足。你的目标是尽可能满足越多数量的孩子，并输出这个最大数值。

# 注意：

# 你可以假设胃口值为正。
# 一个小朋友最多只能拥有一块饼干。

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        res = 0
        i, j = 0, 0
        g_lenght, s_lenght = len(g), len(s)
        
        while i < g_lenght and j < s_lenght:
            if g[i] <= s[j]:
                i += 1
                j += 1
                res += 1
            else:
                j += 1
                
        return res
                