import numpy as np

# Linear Equations
# 3x - y = 0
# x + y = 100

A = np.array([[3,-1],[1,1]])
B = np.array([0, 100])
result = np.linalg.solve(A, B)

x = result[0]
y = result[1]

print("x = ", x)
print("y = ", y)
