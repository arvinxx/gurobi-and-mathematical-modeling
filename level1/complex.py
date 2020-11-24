# 复杂一点的线性规划
# 已知变量 x1 x2 x3 x4 x5 x6
# ​1. 12x1​ +  9x2 + 25x3​ + 20x4​ + 17x5​ + 13x6 ​≥ 60
# 2. 35x1​ + 42x2​ + 18x3​ + 31x4​ + 56x5​ + 49x6 ​≥ 150
# 3. 37x1​ + 53x2​ + 28x3​ + 24x4​ + 29x5​ + 20x6 ​≥ 125
# 4. 0 ≤ xj​ ≤ 1, j= 1,2,⋯,6​
#
# 目标方程 ​Z = 8x1​ + 10x2​ + 7x3​ + 6x4​ + 11x5​ + 9x6
# 求 Z 的最小值

# 相关知识点：
# - prod 参数与变量相乘的方法
# - addVars 批量添加变量方法
# - addConstrs 批量添加约束方法



import gurobipy as gb
from gurobipy import GRB

# 定义目标方程的参数
c = [8, 10, 6, 6, 11, 9]

# 定义约束的参数
p = [[12, 9, 25, 20, 17, 13],
     [35, 42, 18, 31, 56, 49],
     [37, 53, 28, 24, 29, 20]]

# 定义约束极值
r = [60, 150, 125]

m = gb.Model('Complex Model')

# 创建变量 下界 0 上界 1
x = m.addVars(6, lb=0, ub=1, name='x')

# 创建约束条件
# x.prod(c) 等于 sum(xi * ci)
m.setObjective(x.prod(c), GRB.MINIMIZE)

# 添加约束条件
# 方法 addConstrs 可以添加多组约束
# 这里利用了 for i in range(3)
# 进行了 3 次循环,从而分别添加了
# x.prod(p[1]) >= r[1]
# x.prod(p[2]) >= r[2]
# x.prod(p[3]) >= r[3]
# 这三组关系式
m.addConstrs(x.prod(p[i]) >= r[i] for i in range(3))

m.write('complex.lp')

m.optimize()

print("目标值：", m.objVal)

for v in m.getVars():
    print(f"{v.varName}：{v.x}")
