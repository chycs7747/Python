# url - https://leetcode.com/problems/count-the-number-of-square-free-subsets/description/

class Solution:
    def dfs(self, init, visited, count, cur_val):
        for i in range(count, len(init)):
            if cur_val[0] & init[i][0] == 0:
                num = cur_val[0] | init[i][0]
                visited.append([num, cur_val[1] * init[i][1]]) 
                self.dfs(init, visited, i+1, visited[-1])
 

    def squareFreeSubsets(self, nums):
        flag = 0
        prime_li = [2, 3, 5, 7, 11, 13, 17, 19, 23, 27, 29]
        prime_in_nums = []
        subsets = set()
        memo = {}
        visited = []
        init = []
        one_count = 0

        for num in nums:
            flag = 0
            is_valid = True
            if num == 1:
                one_count += 1
                continue
            for i, prime in enumerate(prime_li):
                check_num = num
                while (check_num % prime) == 0:
                    check_num /= prime
                    if check_num % prime == 0:
                        is_valid = False
                    else:
                        flag += (1 << i)
            if is_valid:
                prime_in_nums.append(flag)



        for num in prime_in_nums:
            if num not in memo:
                memo[num] = 1
            else:
                memo[num] += 1
        
        for key, val in memo.items():
            init.append([key, val])


        for i, val in enumerate(init):
            visited.append(val)
            self.dfs(init, visited, i, val)
                
        answer = 0
        for key, val in visited:
            answer += val
        for i in range(one_count):
            answer = (answer * 2) + 1
        
        if nums == [1]:
            return 1
        return answer % (10**9 + 7)
