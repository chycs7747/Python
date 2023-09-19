# https://school.programmers.co.kr/learn/courses/30/lessons/17681
def solution(n, arr1, arr2):
    secret_map = []
    count = 0

    for i in range(n):
        secret_map.append(arr1[i] | arr2[i])

    for i in range(len(secret_map)):
        secret_map[i] = bin(secret_map[i])[2:]
        secret_map[i] = secret_map[i].replace('1', '#')
        secret_map[i] = secret_map[i].replace('0', ' ')

    for i in range(len(secret_map)):
        for j in range(n - len(secret_map[i])):
            secret_map[i] = " " + secret_map[i]

    return secret_map


solution(5, arr1=[9, 20, 28, 18, 11], arr2=[30, 1, 21, 17, 28])
