li = []
n = int(input("요소 수 입력: "))

for i in range(n):
    li.append(int(input("요소 입력: ")))

print(li)

# 일반적인 방식 (Unpacking이 지원 안되는 경우)

for j in range(1, n, 1): #li[1..n-1]까지 (1번인덱스부터 n-1인덱스까지)
    key = li[j] #li[j]를 key에 저장해 둠. (덮어쓰기 이후 이 값을 기억해서 쓰기 위함) ..ㄱ
    i = j-1 #j보다 1작은 인덱스 즉,0번 인덱스부터 n-2인덱스까지
    #li에서 li[j]는 li[0..j-1]까지 반복 수행하며 정렬된다.
    while i>=0 and li[i]>key: #li의 j-1번 인덱스부터 0번인덱스까지 하나씩 내려가며 key값이 i번째 인덱스보다 커지는 순간을 구함(못구하면 i==-1로 while문 탈출)
        li[i+1] = li[i] #이 때 li[j] ㄱ의 상황이 발생함
        i = i-1
    li[i+1] = key #key값을 이용해 i+1번째에 대입

print(li)

for j in range(1, n, 1): #li[1..n-1]까지 (1번인덱스부터 n-1인덱스까지)
    key = li[j] #li[j]를 key에 저장해 둘 필요가 없음(by unpacking)
    i = j-1 #j보다 1작은 인덱스 즉,0번 인덱스부터 n-2인덱스까지
    #li에서 li[j]는 li[0..j-1]까지 반복 수행하며 정렬된다.
    while i>=0 and li[i]>key: #li의 j-1번 인덱스부터 0번인덱스까지 하나씩 내려가며 key값이 i번째 인덱스보다 커지는 순간을 구함(못구하면 i==-1로 while문 탈출)
        li[i+1], li[i] = li[i], li[i+1] #unpacking 이용
        i = i-1
    #li[i+1] = key #key값을 이용해 i+1번째에 대입할 필요가 없음

print(li)

#어떤 방식이 더 효율적? 
##big-O는 버블소트와 마찬가지로 O(n^2)이다. why?
###big-O는 같은데 버블소트와 비교하면 어떤 것을 쓰는게 더 좋을까? 





#코드는 아래가 짧지만 그래도 위의 방법이 더 좋다고 생각함. unpacking자체가 우측의 값을 tuple형으로 바꾸고 tuple의 unpacking을 거친건데 너무 비효율적임.
#또한 같이 개발하는 입장에서 위에가 더 직관적임.


##index를 하나씩 증가시키면서 그 전 요소를 하나씩 비교, 이는 2중 for문의 느낌과 같다.

###최선의 경우를 보아라. 버블소트는 기본적으로 최선의 시간복잡도 W(n^2)이지만, 삽입정렬의 최선의 시간복잡도는 O(n)이므로 버블소트에 비해 효과적인 sorting방법이라고 할 수 있다.