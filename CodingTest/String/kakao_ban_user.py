# 프로그래머스 > 코딩테스트 연습 > 2022 KAKAO BLIND RECRUITMENT > 신고 결과 받기

def solution(id_list, report, k):
    ban_memo = {}
    ban_mail = {}
    answer = [0] * len(id_list)
    for id in id_list:
        ban_memo[id] = []
        ban_mail[id] = 0
    for usr_ban in report:
        user_id, ban_id = usr_ban.split(' ')
        if ban_id not in ban_memo[user_id]:
            ban_memo[user_id].append(ban_id)
            ban_mail[ban_id] += 1
    for ban_id, ban_num in ban_mail.items():
        if ban_num >= k:
            for i, ban_li in enumerate(ban_memo.values()):
                if ban_id in ban_li:
                    answer[i] += 1        
    
    return answer
