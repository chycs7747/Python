import math

#failed
def solution(r1, r2):
    answer = 0

    for i in range(int(r1*math.sqrt(2)/2), r2):
        for j in range(1, i):
            if r1*r1<= i*i + j*j <= r2*r2:
                print(j, i)
                answer += 1
    print("==========")
    print(answer)
    print("==========")
    answer *= 8
    
    x_equal_y = 0
    for i in range(r2):
        if r1*r1 <= i*i*2 and i*i*2 <=r2*r2:
            print("i", i)
            x_equal_y += 1
        
            
    answer += x_equal_y * 4
    print("x_equal_y:", x_equal_y)
    
    xy = 0
    for i in range(r1, r2+1):
        xy += 1
    answer += xy * 4
    print("xy:", xy)
    #바깥원의 점과 중복되는 점 제거해야 함
    
    print(answer)
    
    
    
    """
    duplicate = 0
    for i in range(r1, r2):
        for j in range(1, i): # 0 ~ (r1 to r2사이의 점)
            if j*j + i*i == r2*r2:
                print("i, j", i, j)
                duplicate += 1
    print("dup", duplicate)
    answer -= duplicate * 8
    """
    return answer
    