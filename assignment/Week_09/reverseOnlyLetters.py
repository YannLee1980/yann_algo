# 917. 仅仅反转字母
# 给定一个字符串 S，返回 “反转后的” 字符串，其中不是字母的字符都保留在原地，而所有字母的位置发生反转。
# https://leetcode-cn.com/problems/reverse-only-letters/

class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        if not S: return ""
        i, j = 0, len(S) - 1
        ls = list(S)
        while i < j:
            if ls[i].isupper() or ls[i].islower():
                if ls[j].isupper() or ls[j].islower():
                    ls[i], ls[j] = ls[j], ls[i]
                    i += 1
                    j -= 1
                else:
                    j -= 1
            else:
                i += 1
        return "".join(ls)