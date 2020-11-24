#
# level1 - 一个简单的数学模型
#
# 请听题
# 已知：
# 1： x + 2y + 3z <= 4
# 2： x + y >= 1
# 求：
# x + y + 2z 的最大值


import gurobipy as gp
from gurobipy import GRB

try:
    # 创建模型
    m = gp.Model('mip1')

    # 添加变量
    x = m.addVar(vtype=GRB.BINARY, name="x")
    y = m.addVar(vtype=GRB.BINARY, name="y")
    z = m.addVar(vtype=GRB.BINARY, name="z")

    # 设定模型目标
    # x + y + 2z 的最大值
    m.setObjective(x + y + 2 * z, GRB.MAXIMIZE)

    # 添加约束
    # x + 2y + 3z <= 4
    m.addConstr(x + 2 * y + 3 * z <= 4, "c0")
    # x + y >= 1
    m.addConstr(x + y >= 1, "c1")
    m.write('math.lp')
    m.optimize()

    # 输出结果
    print("最大值: %g" % m.objVal)
    for v in m.getVars():
        print("%s: %g" % (v.varName, v.x))


except GurobiError as e:
    print("Error code" + str(e.errno) + ": " + str(e))

except AttributeError:
    print("Encountered an attribute error")
