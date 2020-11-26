# 557. 反转字符串中的单词 III
# 给定一个字符串，你需要反转字符串中每个单词的字符顺序，同时仍保留空格和单词的初始顺序。
# https://leetcode-cn.com/problems/reverse-words-in-a-string-iii/


class Solution:
    def reverseWords(self, s: str) -> str:
        if not s: return ""
        ls = s.split()
        res = []
        for word in ls:
            word = list(word)
            word[:] = reversed(word)
            res.append(''.join(word))
        return ' '.join(res)
            