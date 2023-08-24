def fibo(n):
    print(n)
    if n == 1 or n == 2:
        return n
    
    return fibo(n-2) + fibo(n-1)

fibo(6)

"""
output:
6
4
2
3
1
2
5
3
1
2
4
2
3
1
2
-> 왼쪽 fibo부터 파고들음(like dfs)
"""