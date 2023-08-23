# https://leetcode.com/problems/two-sum/
array = [4,1,9,7,5,3,16]
array.sort()
n = int(input("input number:"))
def TwoSum():
    start = 0
    end = len(array)-1
    while start != end:
        if array[start] + array[end] > n:
            end = end - 1
        elif array[start] + array[end] < n:
            start = start + 1
        else:
            return True
    return False

print(TwoSum())