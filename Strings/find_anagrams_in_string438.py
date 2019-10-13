def checkAnagram(s, t):
        dict_s = {}
        dict_t = {}
        for i in range(len(s)):
            if s[i] in dict_s:
                dict_s[s[i]] += 1
            else:
                dict_s[s[i]] = 1
            
            if t[i] in dict_t:
                dict_t[t[i]] += 1
            else:
                dict_t[t[i]] = 1
        
        for key in dict_s:
            if key not in dict_t or not dict_s[key] == dict_t[key]:
                return False
        return True

def findAnagrams(s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        answer = []
        for i in range(len(s)-len(p)+1):
            curstring = s[i:i+len(p)]
            if checkAnagram(curstring, p):
                answer.append(i)
        return answer

print(findAnagrams("cbaebabacd", "abc"))
