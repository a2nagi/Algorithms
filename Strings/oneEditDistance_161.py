class Solution:
    
    def replace(self, s, t):
        length = len(s)
        count = 0
        for i in range(length):
            if s[i] != t[i]:
                count += 1
        return count == 1
    
    def insert(self, s, t):
        minlength = min(len(s), len(t))
        if minlength == len(s):
            for i in range(minlength):
                if s[i] != t[i]:
                    temp = t[:i] + t[i+1:]
                    return temp == s
        
        else:
            for i in range(minlength):
                if s[i] != t[i]:
                    temp = s[:i] + s[i+1:]
                    return temp == t
        return True
    
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if s == t:
            return False
        
        if (len(s) == 0 and len(t) == 1) or (len(t) == 0 and len(s) == 1):
            return True
        
        maxlength = max(len(s), len(t))
        minlength = min(len(s), len(t))
        if maxlength - minlength > 1:
            return False
        
        if len(s) == len(t):
            return self.replace(s, t)
       
        return self.insert(s, t) 
