import numpy as np

def jacobi(A, b, tolerance=0.000001, max_iterations=500):
    count = 0
    x = np.zeros_like(b, dtype=np.double)
    
    T = A - np.diag(np.diagonal(A))
    
    for k in range(max_iterations):
        
        x_old  = x.copy()
        
        x[:] = (b - np.dot(T, x)) / np.diagonal(A)
        
        count= count+1
        if np.linalg.norm(x - x_old, ord=np.inf) / np.linalg.norm(x, ord=np.inf) < tolerance:
            print(count)
            print(k)
            break
            
    return x


A = np.array([[10., -1., 2., 0.],
              [-1., 11., -1., 3.],
              [2., -1., 10., -1.],
              [0.0, 3., -1., 8.]])
# initialize the RHS vector
b = np.array([6., 25., -11., 15.])

x = jacobi(A, b, 100)
print(x)