N, K = map(int, input().split())
li = list(map(int, input().split()))

def selection_sort(arr, K=K):
    for i in range(len(li)-1, 0, -1): #방의 개수 - 1 까지 돌면 정렬 완료상태
        max = li[i]
        target = i
        tmp = target
        for j in range(i-1, -1, -1): 
            if li[j] > max:
                max = li[j]
                target = j
        if tmp != target:
            li[i], li[target] = li[target], li[i]
            K-=1
        if K==0:
            return arr
    return -1

answer = selection_sort(li)
if type(answer) == list:
    for i in answer:
        print(i, end = ' ')
    print()
else:
    print(answer)