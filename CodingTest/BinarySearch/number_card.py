# https://www.acmicpc.net/problem/10815
"""
N = int(input())
answers = list(map(int, input().split()))
M = int(input())
cards = list(map(int, input().split()))
"""

"""
1 '2' 3  -> mid < card : 3 '3' 3 / mid > card : 1 '1' 1
2 '2' 3 -> 3 '3' 3  /
3 '3' 3

"""

N = 5
answers = [6, 3, 2, 10, -10]
M = 8
cards = [10, 9, -5, 2, 3, 4, 5, -10]
answers.sort()
answer_li = []
for card in cards:
    isfound = False
    left = 0
    right = len(answers) - 1
    
    while left <= right:
        mid = (left + right) // 2   
        #print(left, mid, right)
        if answers[mid] > card:
        #    print(1)
            right = mid - 1
        elif answers[mid] < card:
        #    print(2)
            left = mid + 1
        else:       
            isfound = True
            break
    
    if isfound:
        answer_li.append(1)
        isfound = False
    else:
        answer_li.append(0)
    #print(answer_li)
    
print(answer_li)
# [-10, 2, 3, 6, 10] 
# [-10, -5, 2, 3, 4, 5, 9, 10]