import numpy as np

def factor_converg(m):
    result = [sum(abs(m[:, i] ) for i in range (len(m) ) ) ]

    return max(result[0] )

def diag_pred(a):
    result = [abs(a[i][j] / a[i][i] )  for i in range(len(a) ) for j in range(len(a[i, ] ) ) if j != i]

    print( (np.array(result) < 1).all() )

a = np.array( [ [7, 3, 1],
                [2, -6, 3],
                [-1, 2, 5] ] )

m = np.array( [ [0, 0.75, -1.25],
                [-1.5, 0, -1],
                [-1.333, 0.666, 0] ] )

print(factor_converg(m) )
diag_pred(a)