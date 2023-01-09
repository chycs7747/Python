li = []
n = int(input("요소 수 입력: "))
for i in range(n):
    li.append(int(input("요소 입력: ")))

print(len(li))

li=[3,2,1,5]
n=6
for i in range(n-1):  # n-1 == 3
    for j in range(n-1, i, -1): #i가 n-2값까지 들어가면 두번째 for문 최대값은 i+1
        # n-1:3 / i:0   3, 2, 1
        # n-1:3 / i:1   3, 2
        # n-1:3 / i:2   3
        if li[j-1] > li[j]:
            li[j], li[j-1] = li[j-1], li[j]

print(li)

# n=4

# 3 2 1 '5' 
# 3 2 '1' 5
# 3 '1' 2 5
# "1" 3 2 5

# "1" 3 2 '5'
# "1" 3 '2' 5
# "1" "2" 3 5

# "1" "2" 3 '5'
# "1" "2" "3" 5 : (n-1)까지 블록되면 끝

"""
시간복잡도 기초
<1>
print(1) : big-O : O(1)

<2>
for i in range(5):  시간복잡도: 6
    if i==3: 시간복잡도: 5
        pass  시간복잡도: 5

for i in range(n): 시간복잡도: n+1
    if i==3: 시간복잡도: n
        pass 시간복잡도: n

-> 시간복잡도: big-O(C1(n+1) + C2(n) + C3(n)) => O(n)
"""

"""
n=5

C2
1. i=1)  5,4,3,2,cond   -> 5
2. i=2) 5,4,3,cond        ->4
3. i=3) 5,4,cond           ->3
4. i=4) 5,cond              -> 2
5. i=5) cond                 -> 1 
big-O notation : O(1부터 5의 합)

C3: 4 + 3 + 2 + 1
big-O notation: O(1부터 4의 합)
"""