import numpy as np

class LinearEquationSolver:
    def __init__(self, coefficients, constants):
        self.coefficients = coefficients
        self.constants = constants
    
    def solve(self):
        solution = np.linalg.solve(self.coefficients, self.constants)
        return solution

# Coefficients matrix (A)
A = np.array([[1, 1], [0, 1]])

# Constants vector (b)
b = np.array([18, 8])

# Create an instance of LinearEquationSolver
equation_solver = LinearEquationSolver(A, b)

# Solve the linear system Ax = b
solution = equation_solver.solve()

print("Solution:")
print("A =", solution[0])
print("B =", solution[1])
