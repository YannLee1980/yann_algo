# 190. 颠倒二进制位
# 颠倒给定的 32 位无符号整数的二进制位。
# https://leetcode-cn.com/problems/reverse-bits/

class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0
        for _ in range(32):
            ans = (ans << 1) + (n & 1)
            n >>= 1
        return ans