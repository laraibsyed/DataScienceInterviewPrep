from math import sqrt
from statistics import mean

def standard_deviation(numbers):
    if len(numbers) > 1:
        avg = mean(numbers)
        var = sum((i - avg) ** 2 for i in numbers) / (len(numbers) - 1)
        std = sqrt(var)
        return std
    return float('NaN')

nums = [1, 2, 3, 4]

results = standard_deviation(nums)

print(results)