"""Universidad de las Fuerzas Armadas ESPE
Integrantes: Carriel Pamela, Ortiz Bryan
NRC:9898
Fecha: miércoles 19 de julio del 2023
""" 
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
