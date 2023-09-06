# https://www.acmicpc.net/problem/1662

def compress_stk(expression):
    dem = 0
    flag = 0
    ans = [0] * len(expression)
    for ch in expression[::-1]:
        if ch == ')':
            dem += 1
            ans[dem] = 0
        elif ch.isdigit():
            if flag == 1:
                dem -= 1
                ans[dem] = ans[dem] + ans[dem+1] * int(ch)
                flag = 0
            else:
                ans[dem] += 1
        else:
            flag = 1
            continue
    return ans[0]


print(compress_stk("15(22)13(92(1111)42(222))123(1)45"))

"""

def compress(expression, idx):
    ans = 0
    prev_num = 0
    start_i = 0
    for i in range(idx, len(expression)):
        if start_i != 0 and start_i >= i:
            continue
        print('cur_ch:', expression[i])
        if expression[i] == ')':
            return i, ans
        elif expression[i] == '(':
            ans -= 1
            start_i, ans = compress(expression, idx)
            ans = prev_num * ans
        else:
            ans += 1
            prev_num = int(expression[i])
    return ans

"""
