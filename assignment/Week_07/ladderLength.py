# 127. 单词接龙
# https://leetcode-cn.com/problems/word-ladder/
# 给定两个单词（beginWord 和 endWord）和一个字典，找到从 beginWord 到 endWord 的最短转换序列的长度。转换需遵循如下规则：

# 每次转换只能改变一个字母。
# 转换过程中的中间单词必须是字典中的单词。

# Double ended BFS:
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList: return 0
        front = {beginWord}
        back = {endWord}
        dist = 1
        wordList = set(wordList)
        len_word = len(beginWord)
        
        while front:
            dist += 1
            next_front = set()
            for word in front:
                for i in range(len_word):
                    for c in string.ascii_lowercase:
                        new_word = word[:i] + c + word[i+1:]
                        if new_word in back:
                            return dist
                        if new_word in wordList:
                            next_front.add(new_word)
                            wordList.remove(new_word)
            front = next_front
            
        if len(front) > len(back):
            front, back = back, front
            
        return 0