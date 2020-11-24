# Level 2

能够初步解决 level1 的问题之后

level2 进入了需要解决真实世界的问题

## 真实世界的问题

有x、y、z三个活动想在同一天举办。
1. 场地总时间只有四个小时可使用；
2. 活动z的价值为活动x及y的两倍；
3. 活动x与活动y至少要选一个举办；
4. 活动x需花费1小时；
5. 活动y需花费2小时；
6. 活动z需花费3小时；

问：举办哪几个活动可以使价值最大化?

第一步： 转换成数学问题

1. 定义三个活动的用时参数 Hx Hy Hz
2. 定义三个活动的价值 Vx Vy Vz
3. 定于变量是否举办活动 Ux Uy Uz(如果举办则为 1，否则为 0)

```
约束1：Hx*Ux + Hy*Uy + Hz*Uz = 4
约束2：Vz = 2Vx; Vz = 2Vy
约束3：Ux+Uy>=1
约束4：Hx=1
约束5：Hy=2
约束6：Hz=3
```
举办活动的价值 Z=Ux * Vx + Uy * Vy + Uz * Vz 

目标：求 Z 的最大值

参数：
活动用时 Hi (i= 1,2,3)
活动价值 Vi (i= 1,2,3)

变量：
是否举办活动 Ui (i=1,2,3) 
Ui =1（如果举办）
Ui =0（如果不举办）

约束：
SUM(Hi * Ui) = 4 (i=i,2,3)
U1+U2 >= 1

Z = SUM(Vi * Ui)(i=1,2,3)


最终结果：
```
目标值： 3.0
used[0]：1.0
used[1]：0.0
used[2]：1.0
```

### 知识点
1. 真实问题的数学建模
2. 0 1 变量的定义
3. vtype=GRB.BINARY 定义布尔类型变量
4. setParam('OutputFlag',0 | 1) 控制是否输求解过程

本题来源：[Python+Gurobi建模](https://github.com/wurmen/Gurobi-Python/blob/master/python-gurobi%20%20model/Python+Gurobi%E5%BB%BA%E6%A8%A1.md)