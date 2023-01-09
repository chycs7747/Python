li = []
n = int(input("요소 수 입력: "))
for i in range(n):
    li.append(int(input("요소 입력: ")))

print(len(li))

for i in range(n-1):
    exchange = 0
    for j in range(n-1, i, -1): #i가 n-2값까지 들어가면 두번째 for문 최대값은 i+1
        if li[j-1] > li[j]:
            li[j], li[j-1] = li[j-1], li[j]
            exchange += 1
    if exchange == 0:
        break

print(li)

#고촬: O(n^2)에는 변함이 없다. 그런데, W는 W(n^2)->W(n) [in best case]이다. 따라서 경우에 따라서는 큰 효과를 볼 수 있다.
#하지만 개발자가 보통 보는 것은 big-O이다. 어떻게 보면, 최악의 상태에서의 big-O는 n^2으로 그대로지만, 불필요한 연산과정이 추가되었다고 생각할 수 있다.
#즉, 케이스에 따라선 불필요한 연산이 추가된 것일 수 있다.. 과연 최선의 상황에 근접하게 나올 확률이 클까? 평균적인 상황에서는 더 느릴 수도 있지 않을까?