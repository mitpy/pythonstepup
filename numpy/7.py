from matplotlib.pyplot import axis
import numpy as np 

mat =np.array([[1,2,3],[4,5,6],[7,8,9]])
print(mat)
print(np.max(mat))
print(np.min(mat))

print(np.max(mat, axis=0))
print(np.min(mat, axis=0))

print(np.max(mat, axis=1))
print(np.min(mat, axis=1))