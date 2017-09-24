import numpy as np
N = 3
A = np.eye(N)
b=np.c_[A, np.ones(N)]
print(b)
