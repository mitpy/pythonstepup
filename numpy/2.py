#single row
import numpy as np

vector_row=np.array([2,5,0,10,100])
print(type(vector_row))
print(vector_row)
print(vector_row[0])
print(vector_row[1])
print(vector_row[2])
print(vector_row[2:5])
print(vector_row[:])

#single column

vector_col=np.array([[10],[1],[5],[3]])
print(vector_col)
print(vector_col[0])
print(vector_col[1])
