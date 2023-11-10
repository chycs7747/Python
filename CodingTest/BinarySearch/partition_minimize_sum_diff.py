# https://leetcode.com/problems/partition-array-into-two-arrays-to-minimize-sum-difference

import bisect

class Solution:
    def minimumDifference(self, nums):
        def make_subset(nums):
            nums.sort(key=lambda x: abs(x), reverse=True)
            memo = set()
            sub = [[0]]
            for num in nums:
                for li in sub[:]:
                    if sum(li) + num not in memo:
                        if num != 0:
                            memo.add(sum(li) + num)
                        tmp = li[:]
                        tmp.append(num)
                        sub.append(tmp)
            subsetsum = {}
            for i in range(0,len(nums)+1):
                subsetsum[i] = []
            for arr in sub:
                subsetsum[len(arr)-1].append(sum(arr))
            return subsetsum

        left = make_subset(nums[:(len(nums)//2)])
        right = make_subset(nums[(len(nums)//2):])
        N = (len(nums)//2)
        half = sum(nums)//2
        ans = inf

        for i in range(N):
            left_sums = left[i]
            right_sums = right[N-i]
            right_sums.sort()
            for j in left_sums:
                diff = half - j
                k = bisect_left(right_sums, diff)
                for q in [k, k-1]:
                    if 0 <= q < len(right_sums):
                        left_ans = j + right_sums[q]
                        right_ans = sum(nums) - left_ans
                        ans = min(ans, abs(left_ans - right_ans))
        return ans