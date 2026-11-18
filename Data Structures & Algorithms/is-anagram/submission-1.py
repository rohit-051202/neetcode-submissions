class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        hash={}
        for i in range (0,len(s)):
            hash[s[i]]=hash.get(s[i],0)+1
            hash[t[i]]=hash.get(t[i],0)-1
        for val in hash.values():
            if val != 0:
                return False
        return True