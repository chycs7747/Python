# 코딩테스트 연습 > 2022 KAKAO BLIND RECRUITMENT > 주차 요금 계산
# url - https://school.programmers.co.kr/learn/courses/30/lessons/92341

def solution(fees, records): 
    memo = {}
    car_time = {}
    result = {}
    tmp = []
    answer = []
    for record in records:
        time, car_num, flag = record.split(' ')
        time_li = time.split(':')
        minutes = int(time_li[0]) * 60 + int(time_li[1])
        

        if car_num not in memo:
            memo[car_num] = minutes
            car_time[car_num] = 0
            result[car_num] = 0
        else:
            if memo[car_num] != -1:
                car_time[car_num] += (minutes - memo[car_num])
                memo[car_num] = -1 # 출차 후 -1로 초기화
            else: # 한번 입출차 후 처음 입차
                memo[car_num] = minutes

    for car_num, time in memo.items():
        if time != -1: # 입차만 있고 출차가 없는 경우
            car_time[car_num] += 1439 - time # 1439 = 23:59

    for car_num, time in car_time.items():
        if time - fees[0] <= 0:
            result[car_num] = fees[1]
        elif (car_time[car_num] - fees[0]) % fees[2] != 0:
            result[car_num] = fees[1] + (((car_time[car_num] - fees[0]) // fees[2] + 1) * fees[3])
        elif (car_time[car_num] - fees[0]) % fees[2] == 0:
            result[car_num] = fees[1] + (((car_time[car_num] - fees[0]) // fees[2]) * fees[3])

    for car_num, money in result.items():
        tmp.append([car_num, money])
    
    tmp.sort()
    
    for car_money in tmp:
        answer.append(car_money[1])
            
    return answer


"""
Algorithm

@ 차량번호가 작은 자동차부터 청구, 주의 - 누적시간
@ stack의 원리를 이용, but append,pop이 아닌 해쉬 접근을 통해 시간복잡도 이점
fees: 기본 시간, 기본 요금, 단위 시간, 단위 요금
records: 시각, 차량번호, 내역

car_time 딕셔너리: 차량 당 누적 이용시간
memo 딕셔너리: 현재 차량의 입,출차기록 관리 (출차 시 -1로 초기화)
money
1. fees + ((내역(out) 시각 - 내역(in) 시각) - 기본 시간) 이 1미만 → fees
2. fees + ((내역(out) 시각 - 내역(in) 시각) - 기본 시간) 이 1초과
→ money = fees +  [((내역(out) 시각 - 내역(in) 시각) - 기본 시간) % 단위 시간 != 0이면],
        fees + (((내역(out) 시각 - 내역(in) 시각) - 기본 시간)//10 + 1) * 단위 요금
→ money = fees +  [((내역(out) 시각 - 내역(in) 시각) - 기본 시간) % 단위 시간 == 0이면],
        fees + (((내역(out) 시각 - 내역(in) 시각) - 기본 시간)//10) * 단위 요금
"""