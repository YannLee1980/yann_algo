# 231. 2的幂
# 给定一个整数，编写一个函数来判断它是否是 2 的幂次方。
# https://leetcode-cn.com/problems/power-of-two/

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and bin(n).count('1') == 1