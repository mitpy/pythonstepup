#sparse matrix

import numpy as np
from scipy import sparse
mat=np.array([[10,20],[0,2],[3,0],[4,5]])
print(mat)
print(mat.size)
print(mat.ndim)
print(mat.shape)
print(mat.shape[0])
mat_sparse=sparse.csr_matrix(mat)
print(mat_sparse)

