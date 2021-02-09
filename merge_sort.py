def merge(left_arr, right_arr, A):
    length_left = len(left_arr)
    length_right = len(right_arr)
    i = 0
    j = 0
    k = 0
    
    while i < length_left and j < length_right:
        if left_arr[i] < right_arr[j]:
            A[k] = left_arr[i]
            i+=1
        else:
            A[k] = right_arr[j]
            j +=1
        k+=1
    while i < length_left:
        A[k] = left_arr[i]
        i +=1
        k +=1
    while j < length_right:
        A[k] = right_arr[j]
        k+=1
        j+=1
        
    return A
        
def mergeSort(A):
    length = len(A)
    if length < 2:
        return A
    
    mid = int(length/2)
    left = []
    right = []
    for i in range(0,mid):
        left.append(A[i])
    for j in range(mid, length):
        right.append(A[j])
    
    left = mergeSort(left)
    right = mergeSort(right)
    A = merge(left, right, A)
    return A

res = mergeSort([3,1,2,5])
print(res)    
    
    
