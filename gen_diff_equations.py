import generator
from sympy import *
import pandas as pd
import numpy as np

x = symbols('x')
f = symbols('f', cls=Function)
counter = 0
total = 5
length = 10

eqs = []
solves = []
for i in range(total):
    print()
    equation = generator.parse_depth(length)
    symp_eq = sympify(equation)
    while symp_eq.is_constant():
        print('here')
        equation = generator.parse_depth(length)
        symp_eq = sympify(equation)
    try:
        diffeq = Eq(sympify(equation), 0)
        solve = dsolve(diffeq, f(x))
        solves.append(str(solve.args[1]))
        eqs.append(equation)

        print("{} ----> {}".format(equation, solve.args[1]))

    except:
        print("{} ----> CAN'T SOLVE".format(equation))
        counter += 1
    print()

df = pd.DataFrame(data=np.asarray([eqs,solves]).T, columns=['diff','eq'])

print(df.head())

df.to_csv('gen_eq.csv', sep=';', encoding='utf-8')


print(counter/total)

