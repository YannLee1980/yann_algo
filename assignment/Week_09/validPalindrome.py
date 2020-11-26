# 680. 验证回文字符串 Ⅱ
# 给定一个非空字符串 s，最多删除一个字符。判断是否能成为回文字符串。
# https://leetcode-cn.com/problems/valid-palindrome-ii/

class Solution:
    def validPalindrome(self, s: str) -> bool:
        if not s: return False
        isPalin = lambda x: x == x[::-1]
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return isPalin(s[left:right]) or isPalin(s[left+1:right+1])
        return True