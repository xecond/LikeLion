N, X = map(int, input().split())
numlist = list(map(int, input().split()))
ans = []
for num in numlist:
    if num > X:
        ans.append(num)

print(*ans)