N, K = map(int, input().split())
Point = list(map(int, input().split()))

answer = 0
tmp = Point[:]
memo = [0]
answer_idx_li = []
for i in range(len(Point)):
    memo.append(memo[-1] + Point[i])
memo = memo[1:]
memo.sort(reverse=True)
print(sum(memo[0:K]))
