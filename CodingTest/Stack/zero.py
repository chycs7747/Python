K = int(input())
#nums = [int(input()) for _ in range(K)]
nums = []
for i in range(K):
    num = int(input())
    if num == 0:
        nums.pop()
    else:
        nums.append(num)

print(sum(nums))

