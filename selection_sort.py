
unsorted_arr = [4,2,5,1,6]
length_arr = len(unsorted_arr)

def selectionSort(arr, length_arr):
    for i in range(0, length_arr-1):
        i_min = i
        for j in range(i+1, length_arr):
            if arr[i] > arr[j]:
                i_min = j
        temp = arr[i]
        arr[i] = arr[i_min]
        arr[i_min] = temp

    return arr

print(unsorted_arr)
res = selectionSort(unsorted_arr, length_arr)
print("After Sorting :")
print(res)
