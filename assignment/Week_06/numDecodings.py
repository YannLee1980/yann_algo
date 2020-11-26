# 91. 解码方法
# https://leetcode-cn.com/problems/decode-ways/
# 一条包含字母 A-Z 的消息通过以下方式进行了编码：

# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
# 给定一个只包含数字的非空字符串，请计算解码方法的总数。

# 题目数据保证答案肯定是一个 32 位的整数。

class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0': return 0
        
        cur, pre = 1, 1
        
        for i in range(1, len(s)):
            tmp = cur
            if s[i] == '0':
                if s[i-1] == '1' or s[i-1] == '2':
                    cur = pre
                else:
                    return 0
            elif s[i-1] == '1' or (s[i-1] == '2' and 0 < int(s[i]) <= 6):
                cur = cur + pre
            pre = tmp
            
        return cur