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

print('done1')
U, s, _ = svd(X, k=150, return_singular_vectors='u')
print('done2')

del X
T = U.dot(np.diag(s))

print('done3')

del U
del s

with open('data/large_files/file85', 'w'):
    pass
with open('data/large_files/file85', 'a')as a:
    for i in T:
        a.write(' '.join([str(j) for j in i]) + '\n')
