import scipy.sparse as spa
from  scipy.sparse.linalg import svds as svd
import json
import numpy as np

with open('data/large_files/w_to_n')as r:
    w_to_n = json.loads(r.read())

leng = len(w_to_n)
X = spa.lil_matrix((leng,leng))
for line in open('data/large_files/file84'):
    t, c, x = line.split()
    t = w_to_n[t]
    c = w_to_n[c]
    x = float(x)
    X[t,c] = x
X = X.tocsr()
del w_to_n


print('start')
for num in range(300):
    U, s, Vt = svd(X, k=1)
    print(f'{num} svd')
    ####################################
    for i in range(len(U)):
        for j in range(len(U[0])):
            if -1e-10 < U[i,j] < 1e-10:
                U[i,j] = 0
    U = spa.csr_matrix(U)
    for i in range(len(Vt)):
        for j in range(len(Vt[0])):
            if -1e-10 < Vt[i,j] < 1e-10:
                Vt[i,j] = 0
    Vt = spa.csr_matrix(Vt)
    print(f'{num} toSparse')
    #####################################
    U = U.dot(spa.csr_matrix(np.diag(s)))
    del s
    spa.save_npz(f'data/large_files/dir85/{num}.npz', U)
    del U
    print(f'{num} save')
    #####################################
    if num == 299:
        break
    #####################################
    V = Vt.T.tocsr()
    #print('V')
    Y = X.dot(V)
    print('Y')
    del V
    #Z = Y.dot(Vt) #ここのメモリがすごいことになる
    #Z = Y * Vt
    Z = spa.lil_matrix((leng,leng))
    for i in range(leng):
        for j in range(leng):
            Z[i,j] = (Y.getrow(i) * Vt.getcol(j))[0,0]
    Z = Z.tocsr()
    print('Z')
    del Y
    del Vt
    X = X - Z
    print(f'{num} newX')
    del Z
    X = X.tolil()
    r,c = X.nonzero()
    for i, j in zip(r, c):
        if -1e-10 < X[i,j] < 1e-10:
            X[i,j] = 0
    X = X.tocsr()
    print(f'{num} end')

