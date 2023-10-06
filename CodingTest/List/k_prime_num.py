# 코딩테스트 연습 > 2022 KAKAO BLIND RECRUITMENT > k진수에서 소수 개수 구하기
# url - https://school.programmers.co.kr/learn/courses/30/lessons/92335

def is_prime(num):
    i = 2
    while i**2 <= num:
        if num % i == 0:
            return False
        i += 1
    return True

def solution(n, k):
    # k진수
    answer = 0
    remainder = ''
    num = n
    while num >= k:
        remainder += str(num % k)
        num //= k
    if num != 0:
        remainder += str(num)
    remainder = remainder[::-1]
    prime_li = remainder.split('0')

    for num in prime_li:
        if num != '' and int(num) >= 2:
            if is_prime(int(num)):
                answer += 1

    return answer
