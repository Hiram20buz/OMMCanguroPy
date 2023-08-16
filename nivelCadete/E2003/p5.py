'''
X * X = 99 + (X * L)
Z * Z = 81
X = Z + L
'''
from sympy import symbols, Eq, solve

# Define the variables
X, L, Z = symbols('X L Z')

# Define the equations
equation_1 = Eq(X * X, 99 + (X * L))
equation_2 = Eq(Z * Z, 81)
equation_3 = Eq(X, Z + L)

# Solve the equations
solutions = solve((equation_1, equation_2, equation_3), (X, L, Z))

# Print the solutions
for sol in solutions:
    print(sol)
