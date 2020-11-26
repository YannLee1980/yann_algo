# 433. 最小基因变化
# https://leetcode-cn.com/problems/minimum-genetic-mutation/

# Doubel ended BFS:
class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        if end not in bank:
            return -1
        front = {start}
        back = {end}
        dist = 0
        bank = set(bank)
        len_gene = len(start)
        
        while front:
            dist += 1
            next_front = set()
            for gene in front:
                for i in range(len_gene):
                    for c in 'ACGT':
                        new_gene = gene[:i] + c + gene[i+1:]
                        if new_gene in back:
                            return dist
                        if new_gene in bank:
                            next_front.add(new_gene)
                            bank.remove(new_gene)
            front = next_front
            
        if len(front) > len(back):
            front, back = back, front
        
        return -1