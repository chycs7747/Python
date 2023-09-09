import math

def solution(r1, r2):
    answer = 0
    for x in range(1, r2):
        if x < r1:
            if int(math.sqrt(r1**2 - x**2)) == math.sqrt(r1**2 - x**2):
                answer += 1
            answer += int(math.sqrt(r2**2 - x**2)) - int(math.sqrt(r1**2 - x**2))
        else:
            answer += int(math.sqrt(r2**2 - x**2))
        
    answer = 4*(answer + r2-r1+1)
    return answer