# 191. 位1的个数
# 编写一个函数，输入是一个无符号整数，返回其二进制表达式中数字位数为 ‘1’ 的个数（也被称为汉明重量）。
# https://leetcode-cn.com/problems/number-of-1-bits/

class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n != 0:
            n &= n - 1
            count += 1
        return count