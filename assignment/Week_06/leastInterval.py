# 621. 任务调度器
# https://leetcode-cn.com/problems/task-scheduler/
# 给定一个用字符数组表示的 CPU 需要执行的任务列表。其中包含使用大写的 A - Z 字母表示的26 种不同种类的任务。任务可以以任意顺序执行，并且每个任务都可以在 1 个单位时间内执行完。CPU 在任何一个单位时间内都可以执行一个任务，或者在待命状态。

# 然而，两个相同种类的任务之间必须有长度为 n 的冷却时间，因此至少有连续 n 个单位时间内 CPU 在执行不同的任务，或者在待命状态。

# 你需要计算完成所有任务所需要的最短时间。

# 1.先考虑出现次数最大的任务；
# 2.再考虑和间隔次数组成的空间：总数 = (任务 A 出现的次数 - 1) * (n + 1) + (出现次数最多的任务个数)
# 3.如果在安排某一个任务时，遇到了剩余的空闲时间不够的情况，那么答案一定就等于任务的总数。
# 参考：https://leetcode-cn.com/problems/task-scheduler/solution/python-xiang-jie-by-jalan/；https://leetcode-cn.com/problems/task-scheduler/solution/ren-wu-diao-du-qi-by-leetcode/

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        tasks_len = len(tasks)
        if tasks_len <= 1: return tasks_len
        
        tasks_dict = {}
        for task in tasks:
            tasks_dict[task] = tasks_dict.get(task, 0) + 1
            
        tasks_sort = sorted(tasks_dict.items(), key = lambda x: x[1], reverse = True)
        
        task_max_count = tasks_sort[0][1]
        
        res = (task_max_count - 1) * (n + 1)
        
        for task in tasks_sort:
            if task[1] == task_max_count:
                res += 1
                
        return res if tasks_len <= res else tasks_len