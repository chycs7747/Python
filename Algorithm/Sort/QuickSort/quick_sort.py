def quick_sort(arr):
    def sort(low, high):
        if high <= low:
            return

        mid = partition(low, high)
        sort(low,  mid - 1)
        sort(mid, high)

    def partition(low, high):
        count1 = 1
        count2 = 1
        pivot = arr[(low + high) // 2]
        while low <= high:
            while arr[low] < pivot: #low 3 ->low 6
                low += 1 
            while arr[high] > pivot: #high 6 -> high 5
                high -= 1
            if low <= high:
                arr[low], arr[high] = arr[high], arr[low]
                low, high = low + 1, high - 1
                #low 4 high 5
            print("[count]:", count1, "low:",low, " high:",high, "로 다시 시작")
            count1 += 1
        print("--end--")
        print("[count]:", count2, "번째 큰 정렬 완료. low:",low," high:",high)
        count2 +=1
        print("pivot:",pivot)
        print(arr)
        return low

    return sort(0, len(arr) - 1)

arr = [0,1,2,9,7,5,4]
quick_sort(arr)
print(arr)

#백준 11004