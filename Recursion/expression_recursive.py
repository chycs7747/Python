def solution(expression):
    test_case = ['* + -', "- * +", "+ - *", "* - +", "+ * -", "- + *"]
    answer_case = []

    def calc(expression, operator_list, weight):
        operator = operator_list[weight]
        split_expression = expression.split(operator)
        print(split_expression)
        if weight == 2:  # base case
            sum = int(split_expression[0]) 
            for i in range(1, len(split_expression)):
                if operator == "*":
                    sum *= int(split_expression[i])
                elif operator == "+":
                    sum += int(split_expression[i])
                elif operator == "-":
                    sum -= int(split_expression[i])
            return sum

        rtn_val = -1
        for sub_expression in split_expression:
            if rtn_val == -1:
                rtn_val = calc(sub_expression, operator_list, weight+1)
            else:
                if operator == "*":
                    rtn_val *= calc(sub_expression, operator_list, weight+1)
                elif operator == "+":
                    rtn_val += calc(sub_expression, operator_list, weight+1)
                elif operator == "-":
                    rtn_val -= calc(sub_expression, operator_list, weight+1)
        return rtn_val

    for case in test_case:
        case = case.split()
        answer_case.append(abs(calc(expression, case, 0)))
    return max(answer_case)


ans = solution("177-661*999*99-133+221+334+555-166-144-551-166*166-166*166-133\
*88*55-11*4+55*888*454*12+11-66+444*99")
print(ans)

"""
factorial같은 재귀는 인자에 n-1과 같이 수식을 적을 수 있었다.
하지만, 연산자는 이와같은 방식이 불가능하다. 따라서 생각을 한 방식이 인덱스+a 를 통한 인자 전달 방식이다.
계산은 돌아오면서 하므로, 우선순위가 낮을수록 먼저 호출된다.
-> permutation(순열) iterationtools로 symbol table을 구현 가능한 것 같다.
"""
