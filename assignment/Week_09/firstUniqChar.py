# 387. 字符串中的第一个唯一字符
# https://leetcode-cn.com/problems/first-unique-character-in-a-string/

# 给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。

class Solution:
    def firstUniqChar(self, s: str) -> int:
        n = len(s)
        if n == 0: return -1
        if n == 1: return 0
        
        visited = {}
        for c in s:
            visited[c] = visited.get(c, 0) + 1
        for i in range(n):
            if visited[s[i]] == 1:
                return i
        
        return -1
