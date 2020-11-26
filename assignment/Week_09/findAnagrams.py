# 438. 找到字符串中所有字母异位词
# 给定一个字符串 s 和一个非空字符串 p，找到 s 中所有是 p 的字母异位词的子串，返回这些子串的起始索引。
# https://leetcode-cn.com/problems/find-all-anagrams-in-a-string/

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if not s or not p: return None
        
        res = []
        p_dict = {}
        win_dict = {}
        
        for c in p:
            p_dict[c] = p_dict.get(c, 0) + 1
        
        left, right = 0, 0
        s_len, p_len = len(s), len(p)
        while right < s_len:
            c = s[right]
            if c not in p_dict:
                win_dict.clear()
                left = right = right + 1
            else:
                win_dict[c] = win_dict.get(c, 0) + 1
                if right - left + 1 == p_len:
                    if win_dict == p_dict:
                        res.append(left)
                    win_dict[s[left]] -= 1
                    left += 1
                right += 1
                
        return res