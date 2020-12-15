# 人体需要四种营养(category) : 卡路里(calories),蛋白质(protein),脂肪(fat), 钠(sodium)
# 食物来源（foods）:  hamburger, chicken, hot dog, fries, macaroni, pizza, salad, milk, ice cream
# 四种营养吸收每天有上限和下限
# 单位重量食物价格不同
# 单位重量食物所含营养成分不同
# 求达到足够营养的最小花费

import gurobipy as gp
from gurobipy import GRB

# Nutrition guidelines, based on
# USDA Dietary Guidelines for Americans, 2005
# http://www.health.gov/DietaryGuidelines/dga2005/

# multidict 生成了多重字典

# ROUTINE:
#   multidict(data)
#   PURPOSE:
#     Split a single dictionary into multiple dictionaries.
#   ARGUMENTS:
#     data: A dictionary that maps each key to a list of 'n' values.
#   RETURN VALUE:
#     A list of the shared keys, followed by individual tupledicts.
#   EXAMPLE:
#     (keys, dict1, dict2) = multidict( {
#              'key1': [1, 2],
#              'key2': [1, 3],
#              'key3': [1, 4] } )

categories, minNutrition, maxNutrition = gp.multidict({
    'calories': [1800, 2200],
    'protein': [91, GRB.INFINITY],
    'fat': [0, 65],
    'sodium': [0, 1779]})

foods, cost = gp.multidict({
    'hamburger': 2.49,
    'chicken': 2.89,
    'hot dog': 1.50,
    'fries': 1.89,
    'macaroni': 2.09,
    'pizza': 1.99,
    'salad': 2.49,
    'milk': 0.89,
    'ice cream': 1.59})

# Nutrition values for the foods
nutritionValues = {
    ('hamburger', 'calories'): 410,
    ('hamburger', 'protein'): 24,
    ('hamburger', 'fat'): 26,
    ('hamburger', 'sodium'): 730,
    ('chicken', 'calories'): 420,
    ('chicken', 'protein'): 32,
    ('chicken', 'fat'): 10,
    ('chicken', 'sodium'): 1190,
    ('hot dog', 'calories'): 560,
    ('hot dog', 'protein'): 20,
    ('hot dog', 'fat'): 32,
    ('hot dog', 'sodium'): 1800,
    ('fries', 'calories'): 380,
    ('fries', 'protein'): 4,
    ('fries', 'fat'): 19,
    ('fries', 'sodium'): 270,
    ('macaroni', 'calories'): 320,
    ('macaroni', 'protein'): 12,
    ('macaroni', 'fat'): 10,
    ('macaroni', 'sodium'): 930,
    ('pizza', 'calories'): 320,
    ('pizza', 'protein'): 15,
    ('pizza', 'fat'): 12,
    ('pizza', 'sodium'): 820,
    ('salad', 'calories'): 320,
    ('salad', 'protein'): 31,
    ('salad', 'fat'): 12,
    ('salad', 'sodium'): 1230,
    ('milk', 'calories'): 100,
    ('milk', 'protein'): 8,
    ('milk', 'fat'): 2.5,
    ('milk', 'sodium'): 125,
    ('ice cream', 'calories'): 330,
    ('ice cream', 'protein'): 8,
    ('ice cream', 'fat'): 10,
    ('ice cream', 'sodium'): 180}

# Model
m = gp.Model("diet")

# Create decision variables for the foods to buy
buy = m.addVars(foods, name="buy")

# You could use Python looping constructs and m.addVar() to create
# these decision variables instead.  The following would be equivalent
#
# buy = {}
# for f in foods:
#   buy[f] = m.addVar(name=f)

# The objective is to minimize the costs
m.setObjective(buy.prod(cost), GRB.MINIMIZE)

# Using looping constructs, the preceding statement would be:
#
# m.setObjective(sum(buy[f]*cost[f] for f in foods), GRB.MINIMIZE)

# Nutrition constraints
m.addConstrs((gp.quicksum(nutritionValues[f, c] * buy[f] for f in foods)
              == [minNutrition[c], maxNutrition[c]]
              for c in categories), name='Nutrition')


# Using looping constructs, the preceding statement would be:
#
# for c in categories:
#     m.addRange(sum(nutritionValues[f, c] * buy[f] for f in foods),
#                minNutrition[c], maxNutrition[c], c)


def printSolution():
    if m.status == GRB.OPTIMAL:
        print('\nCost: %g' % m.objVal)
        print('\nBuy:')
        for f in foods:
            if buy[f].x > 0.0001:
                print('%s %g' % (f, buy[f].x))
    else:
        print('No solution')


m.write('diet.lp')
# Solve
m.optimize()
printSolution()

print('\nAdding constraint: at most 6 servings of dairy')
m.addConstr(buy.sum(['milk', 'ice cream']) <= 6, "limit_dairy")

# Solve
m.optimize()
printSolution()
