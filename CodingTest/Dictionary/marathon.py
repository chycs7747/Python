# 코딩테스트 연습 > 해시 > 완주하지 못한 선수
# url : https://school.programmers.co.kr/learn/courses/30/lessons/42576

import collections

def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]

"""
def solution(participant, completion):
    names = {}
    for name in participant:
        if name not in names:
            names[name] = 1
        else:
            names[name] += 1
    
    for name in completion:
        names[name] -= 1
    
    for name, num in names.items():
        if num == 1:
            return name
"""