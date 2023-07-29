def fibo_dp_bu(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    fibo_arr = [0,1]

    for i in range(2, n+1):
       fibo_tmp =  fibo_arr[i-1] + fibo_arr[i-2]
       fibo_arr.append(fibo_tmp)
    
    return fibo_arr[n]

"""
if n=7
case i:2 [(0,1)] - fibo_tmp = (0+1) - fibo_arr = [0,1,1]
case i:3 [0,(1,1)] - fibo_tmp = (1,1) - fibo_arr = [0,1,1,2]
...
case i:7 [0,1,1,2,3,(5,8)] - fibo_tmp = (5+8) - fibo_arr = [0,1,1,2,3,5,8,'13']
result : 13
"""