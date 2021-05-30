import numpy as np
import time

def gauss_seidel(matrixA, vectorB, limit):
    b = vectorB
    A = matrixA
    
    # prints the system
    print("System:")
    for i in range(A.shape[0]):
        row = ["{}*x{}".format(A[i, j], j + 1) for j in range(A.shape[0])]
        print(" + ".join(row), "=", b[i])
    print()
    t0 = time.time()
    x = np.zeros_like(b) #inicializo un vector de 0s
    for it_count in range(limit):
        #if it_count != 0:
            #print("Iteration {0}: {1}".format(it_count, x))
        x_new = np.zeros_like(x) #creo un nuevo vector de 0s

        for i in range(A.shape[0]):
            #Se tiene s1 y s2 para cumplir con la condición de j != i
            s1 = np.dot(A[i, :i], x[:i]) #Suma 1: Producto punto entre 2 vectores de 1 Dimension
            s2 = np.dot(A[i, i + 1:], x[i + 1:]) #Suma 2: Producto punto entre 2 vectores de 1 Dimension
            x_new[i] = (b[i] - (s1 + s2)) / A[i, i] #Hayamos x(k+1) , suma = s1 + s2
            if x_new[i] == x_new[i-1]:
                break

        if np.allclose(x, x_new, rtol=0., atol=1e-10): #Si se cumple que: absolute(a - b) <= (atol + rtol * absolute(b)) -> Convergencia
            break

        x = x_new
    t1 = time.time()

    total = t1-t0
    print(total)  
    print("Solution:")
    print(x)
    error = np.dot(A, x) - b
    print("Error:")
    print(error)


# initialize the matrix
A = np.array([[10., -1., 2., 0.],
              [-1., 11., -1., 3.],
              [2., -1., 10., -1.],
              [0.0, 3., -1., 8.]])
# initialize the RHS vector
b = np.array([6., 25., -11., 15.])

x = gauss_seidel(A, b, 100)