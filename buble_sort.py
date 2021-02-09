def bubleSort(A):
    length = len(A);
    flag = 0
    for i in range(1,length):
        for j in range(0, length-i):
            if A[j] > A[j+1]:
                temp = A[j]
                A[j] = A[j+1]
                A[j+1] = temp
                flag = 1
        if flag == 0:
            break
    return A
    
res = bubleSort([3,2,5,1])
print(res)
