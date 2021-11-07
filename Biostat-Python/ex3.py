import numpy as np

def FindClosest(X,centers):

    arr = []
    for i in range(len(X)): # number of rows
        row = []
        for j in range(len(centers)): # number of columns
            element = (X[i,0] -centers[j,0])**2 + (X[i,1] - centers[j,1])**2
            row.append(element)
        row.append(np.where(row[0]<=row[1],0,1)) # determine index of minimum value
        arr.append(row) # add each row to array
    newarr = np.array(arr)
    return newarr

A = np.array([[1,2], [3,4], [5,6]]) # A is a 3 x 2 matrix
B = np.array([[1, 0], [2, 5]]) # B is a 2 x 2 matrix
print( FindClosest(A, B))

# A1 = np.linspace(0,2,num=12).reshape(6, 2)
# B1 = np.array([[1, 3], [-1, 2]])
# print( FindClosest(A1, B1) )

# A2 = np.random.normal(size=8).reshape(4,2)
# B2 = np.random.normal(size=6).reshape(3,2)
# print( FindClosest(A2, B2) )


