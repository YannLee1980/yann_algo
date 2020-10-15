class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list) -> int:
        if endWord not in wordList or not beginWord or not wordList:
            return 0
        
        queue = [(beginWord, 1)]
        wordList = set(wordList)
    
        while queue:
            current_w, level = queue.pop(0)
            if current_w == endWord:
                return level + 1
            for i in range(len(current_w)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    new_w = current_w[:i] + c + current_w[i+1:]
                    if new_w in wordList:
                        print(new_w)
                        queue.append((new_w, level+1))
            wordList -= set([new_w])
    
        return 0


s = Solution()
print(s.ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog"]))
