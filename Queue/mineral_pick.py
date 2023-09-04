from collections import deque


def solution(picks, minerals):
    cost = {"diamond": 25, "iron": 5, "stone": 1}
    answer = 0
    pick_num = 0

    for n in picks:
        pick_num += n
    while len(minerals) > pick_num*5:
        minerals.pop()

    minerals = deque(minerals)
    mineral_bag = []
    tmp = []
    count = 5
    while minerals:
        if count > 0:
            tmp.append(minerals.popleft())
            count -= 1
        else:
            mineral_bag.append(tmp)
            count = 5
            tmp = []
    mineral_bag.append(tmp)

    value = 0
    cost_bag = []
    for bag in mineral_bag:
        for mineral in bag:
            value += cost[mineral]
        cost_bag.append(value)
        value = 0

    dia_pick = picks[0]
    iron_pick = picks[1]
    stone_pick = picks[2]

    while cost_bag and (dia_pick or iron_pick or stone_pick):
        cost = max(cost_bag)
        idx = cost_bag.index(cost)
        cost_bag.remove(cost)
        if dia_pick > 0:
            for mineral in mineral_bag[idx]:
                answer += 1
            dia_pick -= 1
        elif iron_pick > 0:
            for mineral in mineral_bag[idx]:
                if mineral == "diamond":
                    answer += 5
                else:
                    answer += 1
            iron_pick -= 1
        elif stone_pick > 0:
            for mineral in mineral_bag[idx]:
                if mineral == "diamond":
                    answer += 25
                elif mineral == "iron":
                    answer += 5
                else:
                    answer += 1
            stone_pick -= 1
        mineral_bag.remove(mineral_bag[idx])
    return answer


print(solution(
    [1, 3, 2], 
    ["diamond", "diamond", "diamond", "iron", "iron", "diamond", "iron", "stone"])
    )
