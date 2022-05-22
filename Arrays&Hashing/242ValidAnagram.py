"""
        Goal: Count the ocurance of each char in both strings
        
        1.We choose to use hashmap, where the 'KEY' is the char, and 'VALUE' stores the  number of times the key(char) occurs.
        2. We compare the length of the 2 strings, as if they are the same,we only need to iterate through one of the hashmaps ie, we can assume there are no extra char in the second string
        
        Time Complexity        O(s+t)              
        Space Complexity       O(s+t) 
        
        Btw, if we have a sorted string, we would just need to compare if they are equal as they would be the same, the time complxity of sorting could be O(nlog(n))
        
"""

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        if len(s) != len(t):
            return False
    
        mapS, mapT = {}, {}
        
        "Building hashmaps for both strings"
        for i in range (len(s)):
            mapS[s[i]] = 1 + mapS.get(s[i],0)
            mapT[t[i]] = 1 + mapT.get(t[i],0)
        
        "Making sure counts are same by iterating through Key ch"
        for ch in mapS:
            if mapS[ch] != mapT.get(ch,0):
                return False        
        
        return True
