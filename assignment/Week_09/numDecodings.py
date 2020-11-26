# 91. 解码方法
# 一条包含字母 A-Z 的消息通过以下方式进行了编码：
# https://leetcode-cn.com/problems/decode-ways/

class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0': return 0
        
        pre, cur = 1, 1
        
        for i in range(1, len(s)):
            tmp = cur
            if s[i] == '0':
                if s[i-1] == '1' or s[i-1] == '2':
                    cur = pre
                else:
                    return 0
            elif s[i-1] == '1' or (s[i-1] == '2' and 0 < int(s[i]) <= 6):
                cur += pre
            pre = tmp
            
        return cur