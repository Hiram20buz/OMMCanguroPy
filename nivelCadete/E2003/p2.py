import numpy as np

# Coefficients matrix (A)
A = np.array([[1, 1], [0, 1]])

# Constants vector (b)
b = np.array([18, 8])

# Solve the linear system Ax = b
x = np.linalg.solve(A, b)

print("Solution:")
print("A =", x[0])
print("B =", x[1])

'''
A + B + 37 = 55
B + 47 = 55

1A + 1B = 18
0A + 1B = 8

'''
