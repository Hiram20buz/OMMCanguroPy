from sympy import symbols, Eq, solve

class EquationSolver:
    def __init__(self):
        self.X, self.L, self.Z = symbols('X L Z')

        self.equation_1 = Eq(self.X * self.X, 99 + (self.X * self.L))
        self.equation_2 = Eq(self.Z * self.Z, 81)
        self.equation_3 = Eq(self.X, self.Z + self.L)

    def solve_equations(self):
        solutions = solve((self.equation_1, self.equation_2, self.equation_3), (self.X, self.L, self.Z))
        return solutions

# Create an instance of the EquationSolver class
solver = EquationSolver()

# Solve the equations
solutions = solver.solve_equations()

# Print the solutions
for sol in solutions:
    print(sol)
