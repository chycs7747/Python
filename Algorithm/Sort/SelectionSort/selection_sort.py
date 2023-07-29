li = [3, 5, 4, 2, 1]

def selection_sort(arr):
    for i in range(len(li)-1): #방의 개수 - 1 까지 돌면 정렬 완료상태
        min = li[i]
        target = i
        for j in range(i+1, len(li)): 
            if li[j] < min:
                min = li[j]
                target = j
        li[i], li[target] = li[target], li[i]

selection_sort(li)
print(li)


li = [3, 5, 4, 2, 1]
def selection_sort2(arr):
    for i in range(len(arr) - 1):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

selection_sort2(li)
print(li)