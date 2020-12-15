## 真实世界的复杂问题

所有员工可得的工作时间及每小时薪资。
每个员工每班最少所需工作时数及最多可工作时数。
每小时最低需求人数。

图一：员工信息

![图一](https://gw.alipayobjects.com/zos/antfincdn/3A8c7Bdnt1/10106ed7-3578-4901-a8f8-fc87a828c2bd.png)

图二：每小时最少所需人数

![图二](https://gw.alipayobjects.com/zos/antfincdn/UbU6eILN8Q/ba50bc0f-84a3-4621-bd9b-d84f507d72dc.png)

目标：最小化每日需支付给员工的薪水。

限制:
1. 需满足每小时所需人数的最低需求。
2. 每位员工每天只能工作一个班次
3. 员工只能在他们可得的时间上班。
4. 如果该员工需上班，则他必须满足他最少所需上班的时数且不得大于他最多能上班时数

### 数学模型
符号：
员工总人数 E，某个员工e（e=1,2,3,...E)
总时刻数 I，某个时刻 i（i=0,1,2,...I）
员工e可以上班的班次 Ke, 某个班次 ke(k=1,2,...Ke)
参数：
- 员工e最小工作时间He_min，最大工作时间 He_max
- 员工e时薪We
- 员工e可以上班的班次 ke,该班次起始时间点 Ske 和结束时间 Eke
- i时刻需要的员工数 Ri

变量：
- 员工e实际工作时间 He
- 员工e在时刻i的排班情况 Tei  
  
  Tei = 1 （如果员工 e 在 i 时刻上班）
 
  Tei = 0 （如果员工 e 不在 i 时刻上班）

- 员工 e 上班的班次 Sek
  Sek = 1 （如果员工在 k 班次上班）
  Sek = 0 （如果员工不在 k 班次上班）

约束：
- He_min * SUM(Sek) <= He * SUM(Sek) <=He_max * SUM(Sek)
- He = SUM(Tei) (i=0,1,...,I)
- 1 >= SUM(Sek) (k=1,2,...K)
- Ri <= SUM(Tei) (e=1,2,3,...E)
- Ske <= ei <=Eke

目标：
C= SUM（We * He）(e=1,2,...N)
最小