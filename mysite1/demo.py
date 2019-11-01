def maxProduct(nums):
    n = len(nums)
    res= tmax = tmin = nums[0]
    for i in range(1, n):
        if nums[i] < 0:
            tmax, tmin = tmin, tmax
        tmax = max(nums[i], tmax * nums[i])
        tmin = min(nums[i], tmin * nums[i])
        if tmax >res:
            res = tmax
    return res
print(maxProduct([2,3,-2,4]))