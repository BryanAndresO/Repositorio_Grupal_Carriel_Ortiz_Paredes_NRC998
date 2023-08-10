def all_permutations_exhaustive(nums):
    def backtrack(start):
        if start == len(nums) - 1:
            permutations.append(nums[:])
            return
        for i in range(start, len(nums)):
            nums[start], nums[i] = nums[i], nums[start]
            backtrack(start + 1)
            nums[start], nums[i] = nums[i], nums[start]

    permutations = []
    backtrack(0)
    return permutations

# Ejemplo de uso para analizar la notación asintótica
nums = [1, 2, 3]
result = all_permutations_exhaustive(nums)
print("Todas las permutaciones posibles:", result)
