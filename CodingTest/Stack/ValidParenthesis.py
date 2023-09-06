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

class Stack:
    def __init__(self, stk=[], top=0):
        self.stk = stk
        self.top = top
    def push(self, val):
        self.stk.append(val)
        self.top += 1
    def pop(self):
        if self.top == 0:
            return
        else:
            self.top -= 1
            return self.stk.pop()
    def traverse(self):
        for i in range(len(self.stk)):
            print(self.stk[i])

class ValidCheck(Stack):
    def __init__(self, val):
        self.valid_li = []
        if val is not None:
            super().__init__(stk=val.split(), top=len(val.split()))
        else:
            super().__init__()
    def pair_check(self, val):
        if val == '(':
            if self.valid_li[-1] == ')':
                self.valid_li.pop()
            else: # not valid pair
                return False
        elif val == '[':
            if self.valid_li[-1] == ']':
                self.valid_li.pop()
            else: # not valid pair
                return False              
        elif val == '{':
            if self.valid_li[-1] == '}':
                self.valid_li.pop()
            else: # not valid pair
                return False
        return True
    def valid_check(self):
        while self.top > 0:
            pop_val = self.stk.pop()
            self.top -= 1 #self.top이 44번째줄에 재선언되어서 pop시 원함수의 self.top를 줄이는 것에 영향을 주지 못함
            if pop_val in [')', '}', ']']:
                self.valid_li.append(pop_val)
            else:
                if not self.valid_li: #check empty lists / check open parenthesis count > close parenthesis count
                    return False
                else:
                    if self.pair_check(pop_val) is False:
                        return False                           
        if self.valid_li: #check close parenthesis count > open parenthesis count
            return False
        return True

    
s=input()
stack = ValidCheck(s)
print(stack.valid_check())