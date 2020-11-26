# 205. 同构字符串
# 给定两个字符串 s 和 t，判断它们是否是同构的。

# 如果 s 中的字符可以被替换得到 t ，那么这两个字符串是同构的。

# 所有出现的字符都必须用另一个字符替换，同时保留字符的顺序。两个字符不能映射到同一个字符上，但字符可以映射自己本身。

# https://leetcode-cn.com/problems/isomorphic-strings/

# s,t要满足一一对应对关系，所以要正反调用
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        def _helper(s, t):
            st_dict = {}
            for i in range(len(s)):
                if s[i] not in st_dict:
                    st_dict[s[i]] = t[i]
                elif st_dict[s[i]] != t[i]:
                    return False
            return True
        
        if len(s) != len(t): return False
        if not s and not t: return True
        return _helper(s, t) and _helper(t, s)