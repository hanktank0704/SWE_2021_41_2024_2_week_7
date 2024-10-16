from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    # Your Codes
    searchin = {}
    ## Do not use input() or print() in your function
    ## Inputs (nums, target) will given as arguments and the output as
    ## return value

    for i, num in enumerate(nums):
        a = target - num

        if a in searchin:
            return [searchin[a], i]

        searchin[num] = i

    return []

###
'''
nums = [2,7,11,15]
target = 9
result = twoSum(nums, target)
print(result)

nums = [3,2,4]
target = 6
result = twoSum(nums, target)
print(result)

nums = [3,3]
target = 6
result = twoSum(nums, target)
print(result)

nums = [100, 1, 10, 12 , 15]
target = 25
result = twoSum(nums, target)
print(result)
'''
