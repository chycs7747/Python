# https://leetcode.com/problems/two-sum/
array = [4, 1, 9, 7, 5, 3, 16]
n = int(input("input number:"))


def TwoSum():
    for i in range(len(array)-1):
        for j in range(i+1, len(array), 1):
            if array[i] + array[j] == n:
                print("{} + {}" .format(array[i], array[j]))
                return 1
    return 0


if TwoSum():
    print("True")
else:
    print("False")
