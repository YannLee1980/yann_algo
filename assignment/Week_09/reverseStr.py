# 541. 反转字符串 II
# 给定一个字符串 s 和一个整数 k，你需要对从字符串开头算起的每隔 2k 个字符的前 k 个字符进行反转。
# https://leetcode-cn.com/problems/reverse-string-ii/

class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        if not s: return ''
        ls = list(s)
        for i in range(0, len(ls), 2*k):
            ls[i: i+k] = reversed(ls[i: i+k])
        return ''.join(ls)