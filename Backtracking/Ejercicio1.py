def subset_sum_backtracking(nums, target):
    def backtrack(start, target, path):
        if target == 0:
            result.append(path)
            return
        for i in range(start, len(nums)):
            if target - nums[i] >= 0:
                backtrack(i + 1, target - nums[i], path + [nums[i]])
    result = []
    backtrack(0, target, [])
    return result