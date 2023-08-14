from sympy import symbols, Eq, solve

# Definir las variables
A, B, C, D = symbols('A B C D')

# Definir las ecuaciones
eq1 = Eq(C - A, 10)
eq2 = Eq(D - B, 15)
eq3 = Eq(D - A, 22)

# Resolver para D en términos de A
solutions = solve([eq1, eq2, eq3], [A, B, C, D])

# Calcular C - B
CB = solutions[C] - solutions[B]

print(f"The value of C - B is: {CB}")
