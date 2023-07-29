fibo_arr = [0,1] #len(fibo_arr)=2
#피보나치 : 0, 1, 1, 2, 3, 5, 8, 13, ...

def fibo_dp_td(n):
    if n < len(fibo_arr):
        print("up:",fibo_arr[n])
        return fibo_arr[n]
    else:
        print("down:",n)
        #n=7
        fibo_tmp = fibo_dp_td(n-1) + fibo_dp_td(n-2)
        fibo_arr.append(fibo_tmp)
        return fibo_tmp

print(fibo_dp_td(7))
    
"""
can cause stack overflow
#down case
case n:7 <down:7> fibo_dp_td(7-1)
case n:6 <down:6> fibo_dp_td(6-1)
case n:5 <down:5> fibo_dp_td(5-1)
case n:4 <down:4> fibo_dp_td(4-1)
case n:3 <down:3> fibo_dp_td(3-1)
case n:2 <down:2> fibo_dp_td(2-1) - fibo(1) - escape
#up case
case n:2 <1(up:1),0(up:0)> - fibo_arr.append(1+0), return fibo_tmp(1+0) - fibo_arr = [0,1,1]
case n:3 <2(ret:1),1(up:1)> - fibo_arr.append(1+1), return fibo_tmp(1+1) - fibo_arr = [0,1,1,2]
case n:4 <3(ret:2),2(up:1)> - fibo_arr.append(2+1), return fibo_tmp(2+1) - fibo_arr = [0,1,1,2,3]
case n:5 <4(ret:3),3(up:2)> - fibo_arr.append(3+2), return fibo_tmp(3+2) - fibo_arr = [0,1,1,2,3,5]
case n:6 <5(ret:5),4(up:3)> - fibo_arr.append(5+3), return fibo_tmp(5+3) - fibo_arr = [0,1,1,2,3,5,8]
case n:7 <6(ret:8),5(up:5)> - fibo_arr.append(8+5), return fibo_tmp(8+5) - fibo_arr = [0,1,1,2,3,5,8,13]
"""