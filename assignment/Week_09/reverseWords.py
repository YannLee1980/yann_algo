# 151. 翻转字符串里的单词
# 给定一个字符串，逐个翻转字符串中的每个单词。
# https://leetcode-cn.com/problems/reverse-words-in-a-string/

class Solution:
    def reverseWords(self, s: str) -> str:
        if not s: return ""
        ls = s.split()
        ls = reversed(ls)
        return " ".join(ls)