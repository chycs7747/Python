def insertsion_sort(arr):
    for j in range(1, len(arr)):
        key = arr[j]
        i = j-1
        while(i>=0 and arr[i]>key):
            arr[i+1] = arr[i]
            i -= 1
        arr[i+1] = key
    return arr
arr = [9,3,5,7,1]
result = insertsion_sort(arr)
print(result)