"""
        Goal: For each integer var in the list we need to check if the '(TARGET-VAR)' exists in the list, until we find the single soln.
        
        1. In the brute force soln, we have a double nested loop, the first to calculate the '(TARGET-VAR)' for each VAR, and the second that checks if '(TARGET-VAR)'            exists in the remaining list.
        
        2. To optimise accessing the VARS, implement hashmap, mapping the value to index of that value. And, to prevent the VAR from using itself to sum up to the                TARGET, we add the VAR to the hashmap after compare, ie, we find the solution onlu if one of the two addends already exists in the hashmap.
         
                                 1.          2.
        Time Complexity        O(n^2)        O(n)
        Space Complexity       O(1)          O(n)
                
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        map_nums = {}
       
        for i,n  in enumerate(nums):
            
            diff = target - n
            if diff in map_nums:
                return [map_nums[diff], i]
            map_nums[n] = i
