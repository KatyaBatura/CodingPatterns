"""
        1. Brute force soln is to iterate through the list, and comepare with the rest of the values in a nested for loop
        2. Sort and Compare the adjacent values
        3. Add values to hashset, checking if it already exists in
                               1.          2.             3.
        Time Complexity        O(n^2)      O(nlog(n))     O(n)         
        Space Complexity       O(1)        O(1)           O(n)
         
"""


class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        hashset = set()
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        
        return False
        
        
