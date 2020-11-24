# 活动问题
# 有x、y、z三个活动想在同一天举办。
# 1. 场地总时间只有四个小时可使用；
# 2. 活动z的价值为活动x及y的两倍；
# 3. 活动x与活动y至少要选一个举办；
# 4. 活动x需花费1小时；
# 5. 活动y需花费2小时；
# 6. 活动z需花费3小时；
#
# 问：举办哪几个活动可以使价值最大化?


# 知识点
# - 真实问题的数学建模
# - 0 1 变量的定义
# - vtype=GRB.BINARY 定义布尔类型变量


import gurobipy as gb
from gurobipy import GRB

# 常数：时间限制
timeLimit = 4

# 参数：活动所需用时
hours = [1, 2, 3]
# 参数：活动的价值
value = [1, 1, 2]

# 建模
m = gb.Model('Activity')

# 添加变量：是否举办活动
used = m.addVars(3, vtype=GRB.BINARY, name='used')

# 添加约束：必须举办 x 或 y
m.addConstr(used[0] + used[1] >= 1, 'mustXorY')

# 添加约束：时间只有 4 小时
m.addConstr(used.prod(hours) == timeLimit, 'timeLimit')

# 添加目标：总价值最大
m.setObjective(used.prod(value), GRB.MAXIMIZE)

m.write('activity.lp')

# 不显示输出的求解过程
m.setParam('OutputFlag', 0)

m.optimize()

print("目标值：", m.objVal)

for v in m.getVars():
    print(f"{v.varName}：{v.x}")
