def bubleSort(A):
    length = len(A);
    
    for i in range(1,length):
        print(A)
        for j in range(0, length-i):
            if A[j] > A[j+1]:
                temp = A[j]
                A[j] = A[j+1]
                A[j+1] = temp
    
    return A
    
res = bubleSort([3,2,5,1])
print(res)
