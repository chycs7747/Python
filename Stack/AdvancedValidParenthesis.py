# https://leetcode.com/problems/valid-parentheses/
# () {} [] 가 올바른 쌍을 갖으며 열고 닫히는지 확인하는 문제

"""
input : s = ") ("
output : false

input : s = "( [ ] }"
output : false

input : s = "{ ( ) [ ] }"
output : true
"""

"""
algorithm
init_stk = "{()[]}"
1. } ] [
2. } ) (
3. } {
"""

def isvalid(s): #괄호 사이에 공백 없다 가정
    stack = []
    for p in s:
        if p == "(":
            stack.append(")")
        elif p == "{":
            stack.append("}")
        elif p == "[":
            stack.append("]")
        elif not stack or stack.pop() != p:
            return False
    return not stack

s=input()
print(isvalid(s))