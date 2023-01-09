li = [2,5,1,2,7]
n = len(li)
"""
n-1 == 4
0,1,2,3     x-0==4
0,1,2       x-1==3
0,1         x-2==2
0           x-3==1 ==>x=4
"""
for i in range(n-1): #n-1:4
    for j in range(0, (n-1)-i, 1):
        if li[j]>li[j+1]:
            li[j], li[j+1] = li[j+1], li[j]

print(li)
