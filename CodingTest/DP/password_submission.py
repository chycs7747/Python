# https://leetcode.com/problems/strong-password-checker/description/?source=submission-ac

from collections import Counter

class Solution:
    def strongPasswordChecker(self, password):
        # Data Processing
        answer = 0
        case = {}
        prev = password[0]
        dup_num = 0
        dup_list = []
        eraise_list = []
        for i, char in enumerate(password):
            if prev == char:
                dup_num += 1
            else:
                dup_list.append(dup_num)
                prev = char
                dup_num = 1
            if i == len(password) - 1:
                dup_list.append(dup_num)

            if 'A' <= char <= 'Z':
                if 'upper' not in case:
                    case['upper'] = True
            elif 'a' <= char <= 'z':
                if 'lower' not in case:
                    case['lower'] = True
            elif '0' <= char <= '9':
                if 'digit' not in case:
                    case['digit'] = True
        
            
        # Algorithm
        if len(password) < 6:
            if 6 - len(password) > 3 - len(case):
                return 6 - len(password)
            else:
                return 3 - len(case)
        elif 6 <= len(password) <= 20:
            required_edit = 0
            for dup in dup_list:
                required_edit += dup // 3
            if required_edit > 3 - len(case):
                return required_edit
            else:
                return 3 - len(case)
        else:
            after_length = len(password)
            for i, dup in enumerate(dup_list):
                if dup >= 3:
                    rem = (dup - 2) % 3
                    if rem == 0:
                        eraise_list.append((i, 3))
                    else:
                        eraise_list.append((i, rem))
            
            eraise_list.sort(key=lambda x: x[1])
            
            after_length = len(password)
            for i, num in eraise_list:
                if after_length - num >= 20:
                    dup_list[i] -= num
                    after_length -= num
                    answer += num
                else:
                    break
            
            for i, dup in enumerate(dup_list):
                while after_length - 3 >= 20:
                    if dup >= 3:
                        after_length -= 3
                        answer += 3
                        dup_list[i] -= 3
                    else:
                        break
                else:
                    break

            answer += after_length - 20
            dup_edit_num = 0
            for i, dup in enumerate(dup_list):
                dup_edit_num += dup // 3
            
            if (3- len(case)) > dup_edit_num:
                return answer + (3 - len(case))
            else:
                return answer + dup_edit_num
