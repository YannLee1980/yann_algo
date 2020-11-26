# 8. 字符串转换整数 (atoi)
# 请你来实现一个 atoi 函数，使其能将字符串转换成整数。
# https://leetcode-cn.com/problems/string-to-integer-atoi/

class Solution:
    def myAtoi(self, s: str) -> int:
        ls = list(s.strip())
        if len(ls) == 0: return 0
        
        sign = -1 if ls[0] == '-' else 1
        
        if ls[0] in ['-', '+']: del ls[0]
        
        i, res = 0, 0
        while i < len(ls) and ls[i].isdigit():
            res = 10 * res + (ord(ls[i]) - ord('0'))
            i += 1
            
        return min(2**31 - 1, max(res*sign, -2**31))