from sympy import symbols, Eq, solve

class EquationSolver:
    def __init__(self):
        self.A, self.B, self.C, self.D = symbols('A B C D')
        self.eq1 = Eq(self.C - self.A, 10)
        self.eq2 = Eq(self.D - self.B, 15)
        self.eq3 = Eq(self.D - self.A, 22)
        
    def solve(self):
        solutions = solve([self.eq1, self.eq2, self.eq3], [self.A, self.B, self.C, self.D])
        CB = solutions[self.C] - solutions[self.B]
        return CB

# Create an instance of EquationSolver
equation_solver = EquationSolver()

# Solve the equations and calculate C - B
result = equation_solver.solve()

print(f"The value of C - B is: {result}")
'''
Add in the class to receive constants
'''
