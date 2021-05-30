import numpy as np

def jacobi(a, b, tol, kmax):
    
    n = a.shape[0]
    x = np.zeros(n)
    k = 1

    while k < kmax:
        for i in range(n):
            suma = 0
            for j in range(n):
                if j != i:
                    suma += a[i,j]*x[j]
            x[i] = (b[i] - suma) / a[i,i]        
        k += 1
    print("Número de iteraciones: ", k)
    return x

A = np.array([[10., -1., 2., 0.],
              [-1., 11., -1., 3.],
              [2., -1., 10., -1.],
              [0.0, 3., -1., 8.]])
# initialize the RHS vector
b = np.array([6., 25., -11., 15.])
x = jacobi(A, b, 0.000001, 500)
print(x)