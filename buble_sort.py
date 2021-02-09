def bubleSort(A):
    length = len(A);
    
    for i in range(0,length):
        for j in range(0, length-1):
            if A[j] > A[j+1]:
                temp = A[j]
                A[j] = A[j+1]
                A[j+1] = temp
    
    return A
    
res = bubleSort([3,2,5,1])
print(res)
