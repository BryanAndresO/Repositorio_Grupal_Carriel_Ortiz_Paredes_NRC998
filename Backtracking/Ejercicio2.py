def permutations_backtracking(nums):
    def backtrack(path):
        if len(path) == len(nums):
            result.append(path)
            return
        for num in nums:
            if num not in path:
                backtrack(path + [num])
    result = []
    backtrack([])
    return result
