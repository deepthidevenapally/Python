def superSet(nums):
    ans = [[]]
    for i in nums:
        ans += [j + [i] for j in ans]
    return ans

print(superSet([1, 2, 3]))

