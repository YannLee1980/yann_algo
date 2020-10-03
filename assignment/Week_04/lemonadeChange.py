# 860. 柠檬水找零
# https://leetcode-cn.com/problems/lemonade-change/
# 在柠檬水摊上，每一杯柠檬水的售价为 5 美元。

# 顾客排队购买你的产品，（按账单 bills 支付的顺序）一次购买一杯。

# 每位顾客只买一杯柠檬水，然后向你付 5 美元、10 美元或 20 美元。你必须给每个顾客正确找零，也就是说净交易是每位顾客向你支付 5 美元。

# 注意，一开始你手头没有任何零钱。

# 如果你能给每位顾客正确找零，返回 true ，否则返回 false 。

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five , ten = 0 , 0
        for bill in bills:
            if bill == 5:
                five += 1
            if bill == 10:
                five -= 1
                ten += 1
            if bill == 20:
                if ten >= 1:
                    ten -= 1
                    five -= 1
                else:
                    five -= 3
            if five < 0 or ten < 0:
                return False
        if five >= 0 and ten >= 0:
            return True

